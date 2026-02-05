#!/usr/bin/env python3
"""Lightweight Federal Register discovery helper.

Purpose
-------
This script is **for manual editorial discovery only**, not for bulk mining.
Given a publication date, it calls the Federal Register JSON API once,
then prints a small table of candidate documents (document number, type,
agencies, title) so a human editor can decide what to open in a browser.

Usage
-----
    python scripts/fr_discovery_helper.py --date 2026-02-04

Optional filters:
    --type RULE --type PRORULE --type NOTICE

Notes
-----
- This assumes that access to `https://www.federalregister.gov/api/v1/`
  is working. If the environment is behind a CAPTCHA or block page, the
  script will print an error summary instead of JSON results.
- Keep the per-page limit modest (default 50) to avoid looking like a
  scraper. This is a *discovery* tool, not an indexer.
"""

import argparse
import json
import sys
import textwrap
import urllib.parse
import urllib.request
from typing import Iterable, List

API_URL = "https://www.federalregister.gov/api/v1/documents.json"


def build_url(pub_date: str, types: List[str], per_page: int) -> str:
    params = {
        "per_page": str(per_page),
        "order": "newest",
        "conditions[publication_date][is]": pub_date,
    }
    # Encode type filters as conditions[type][]=...
    for t in types:
        params.setdefault("conditions[type][]", [])
        params["conditions[type][]"].append(t)

    # urllib.parse.urlencode cannot natively handle list values unless
    # we pass doseq=True.
    query = urllib.parse.urlencode(params, doseq=True)
    return f"{API_URL}?{query}"


def fetch(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "gpt-5-1-structural-wire/0.1 (discovery-helper)",
            "Accept": "application/json, */*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            content_type = resp.headers.get("Content-Type", "")
            body = resp.read()
    except Exception as e:  # pragma: no cover - simple CLI helper
        print(f"ERROR: request failed: {e}", file=sys.stderr)
        sys.exit(1)

    # If we get HTML instead of JSON, show the first chunk to help debug
    if "json" not in content_type.lower():
        snippet = body[:400].decode("utf-8", errors="replace")
        print("ERROR: expected JSON but got Content-Type=", content_type, file=sys.stderr)
        print("--- response snippet ---", file=sys.stderr)
        print(snippet, file=sys.stderr)
        sys.exit(1)

    try:
        return json.loads(body.decode("utf-8"))
    except json.JSONDecodeError as e:  # pragma: no cover
        print("ERROR: JSON decode failed:", e, file=sys.stderr)
        sys.exit(1)


def format_row(text: str, width: int = 80, indent: int = 4) -> str:
    return "\n".join(
        textwrap.wrap(text, width=width, subsequent_indent=" " * indent)
    )


def summarize(results: Iterable[dict]) -> None:
    for i, doc in enumerate(results, start=1):
        doc_no = doc.get("document_number") or "?"
        dtype = doc.get("type") or "?"
        title = (doc.get("title") or "").strip()
        agencies = ", ".join(a.get("name", "?") for a in doc.get("agencies", []))
        citation = doc.get("citation") or ""
        fr_pages = doc.get("page") or ""

        print(f"[{i}] {doc_no}  {dtype}")
        if agencies:
            print("    Agencies:", agencies)
        if citation or fr_pages:
            pieces = []
            if citation:
                pieces.append(citation)
            if fr_pages:
                pieces.append(f"pages {fr_pages}")
            print("    Citation:", "; ".join(pieces))
        if title:
            print("    Title:")
            print("    " + format_row(title, width=78, indent=4))
        print()


def main(argv: List[str]) -> None:
    parser = argparse.ArgumentParser(description="Federal Register discovery helper")
    parser.add_argument(
        "--date",
        required=True,
        help="Publication date (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--type",
        dest="types",
        action="append",
        default=[],
        help="Document type filter (e.g., RULE, PRORULE, NOTICE). Can be repeated.",
    )
    parser.add_argument(
        "--per-page",
        type=int,
        default=50,
        help="Max documents to request (default: 50; keep this modest).",
    )

    args = parser.parse_args(argv)

    types = args.types or ["RULE", "PRORULE", "NOTICE"]
    url = build_url(args.date, types, args.per_page)
    print("Requesting:", url, "\n", file=sys.stderr)

    data = fetch(url)
    results = data.get("results", [])

    print(f"Total results (API-reported): {data.get('count', len(results))}")
    print(f"Results in this page: {len(results)}")
    print()
    if not results:
        print("No documents returned.")
        return

    summarize(results)


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
