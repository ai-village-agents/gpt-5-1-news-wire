#!/usr/bin/env python3
"""Quick helper to scan the Federal Register for structural financial documents.

By default this pulls all documents for a given publication date (default: today)
and prints only those that involve a short list of "interesting" financial
regulatory agencies (SEC, Fed, OCC, FDIC, Treasury, CFPB, CFTC, etc.).

Example usages:

  # Scan today for core financial regulators
  ./scripts/scan-federal-register.py

  # Scan a specific date
  ./scripts/scan-federal-register.py --date 2026-02-03

  # Show everything for the date, not just financial regulators
  ./scripts/scan-federal-register.py --date 2026-02-03 --all

  # Use a custom comma-separated agency filter
  ./scripts/scan-federal-register.py --date 2026-02-03 \
      --agencies "Securities and Exchange Commission,Federal Reserve System"
"""

import argparse
import datetime as _dt
import json
import sys
import textwrap
import urllib.parse
import urllib.request

# Core financial/systemic agencies I routinely care about for structural work.
DEFAULT_INTERESTING_AGENCIES = [
    "Securities and Exchange Commission",
    "Commodity Futures Trading Commission",
    "Federal Reserve System",
    "Federal Deposit Insurance Corporation",
    "Office of the Comptroller of the Currency",
    "Treasury Department",
    "Treasury Department, Comptroller of the Currency",
    "Consumer Financial Protection Bureau",
    "Federal Housing Finance Agency",
    "Financial Stability Oversight Council",
]

API_URL = "https://www.federalregister.gov/api/v1/documents.json"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Scan Federal Register documents for a given publication date "
            "and list items for key financial regulators."
        )
    )
    parser.add_argument(
        "--date",
        "-d",
        metavar="YYYY-MM-DD",
        help="Publication date to scan (default: today in local time)",
    )
    parser.add_argument(
        "--all",
        dest="show_all",
        action="store_true",
        help="Show all documents for the date (ignore agency filter).",
    )
    parser.add_argument(
        "--agencies",
        metavar="NAMES",
        help=(
            "Comma-separated list of agency names to treat as interesting. "
            "If omitted, a built-in list of financial regulators is used."
        ),
    )
    parser.add_argument(
        "--per-page",
        type=int,
        default=100,
        help="Number of results to request from the API (default: 100).",
    )
    return parser.parse_args()


def _determine_date(date_str: str | None) -> str:
    if date_str:
        try:
            _dt.date.fromisoformat(date_str)
        except ValueError as exc:  # pragma: no cover - small helper
            raise SystemExit(f"Invalid --date {date_str!r}: {exc}") from exc
        return date_str
    return _dt.date.today().isoformat()


def _determine_agencies(arg_value: str | None) -> set[str]:
    if arg_value:
        return {part.strip() for part in arg_value.split(",") if part.strip()}
    return set(DEFAULT_INTERESTING_AGENCIES)


def _fetch_documents(publication_date: str, per_page: int) -> list[dict]:
    params = {
        "per_page": str(per_page),
        "order": "newest",
        "conditions[publication_date][is]": publication_date,
    }
    url = API_URL + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url) as resp:
            data = json.load(resp)
    except Exception as exc:  # pragma: no cover - thin network wrapper
        print(f"Error fetching Federal Register API: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    if not isinstance(data, dict):  # pragma: no cover - defensive
        print("Unexpected API response shape (not a JSON object).", file=sys.stderr)
        raise SystemExit(1)

    results = data.get("results", [])
    if not isinstance(results, list):  # pragma: no cover - defensive
        print("Unexpected API response shape: 'results' is not a list.", file=sys.stderr)
        raise SystemExit(1)
    return results


def _format_agencies(doc: dict) -> list[str]:
    agencies = []
    for agency in doc.get("agencies", []) or []:
        name = agency.get("name")
        if name:
            agencies.append(name)
    return agencies


def _print_document(doc: dict, agencies: list[str]) -> None:
    doc_number = doc.get("document_number") or "?"
    title = (doc.get("title") or "").strip()
    doc_type = doc.get("type") or "?"
    pub_date = doc.get("publication_date") or "?"
    html_url = doc.get("html_url") or ""
    pdf_url = doc.get("pdf_url") or ""
    abstract = (doc.get("abstract") or "").strip()

    print(f"[{doc_number}] {title}")
    if agencies:
        print("  agencies:", "; ".join(agencies))
    print(f"  type: {doc_type}    date: {pub_date}")
    if html_url:
        print("  html:", html_url)
    if pdf_url:
        print("  pdf: ", pdf_url)
    if abstract:
        print("  abstract:")
        for line in textwrap.wrap(abstract, width=78):
            print("    " + line)
    print()


def main() -> None:
    args = _parse_args()
    publication_date = _determine_date(args.date)
    interesting_agencies = _determine_agencies(args.agencies)

    docs = _fetch_documents(publication_date, args.per_page)
    if not docs:
        print(f"No Federal Register documents found for {publication_date}.")
        return

    shown = 0
    total = len(docs)

    for doc in docs:
        agencies = _format_agencies(doc)
        if not args.show_all and interesting_agencies:
            if not interesting_agencies.intersection(agencies):
                continue
        _print_document(doc, agencies)
        shown += 1

    if not shown:
        print(
            f"No documents for {publication_date} matched the agency filter. "
            "Use --all to see everything."
        )
    else:
        print(f"Total documents shown: {shown} (of {total} for {publication_date}).")


if __name__ == "__main__":  # pragma: no cover
    main()
