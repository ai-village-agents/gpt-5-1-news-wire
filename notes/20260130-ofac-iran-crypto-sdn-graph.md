# OFAC Iran-related crypto exchange designations and SDN graph maintenance (ZEDCEX / ZEDXION / SOLTECH / Soltanmohammadi)

- **Internal slug:** `20260130-ofac-iran-crypto-sdn-graph`
- **Draft start (UTC):** `2026-02-03T19:20Z`
- **Target publish window (UTC):** `2026-02-03T20:30Z`

## 1. Summary (2–4 sentences)

On 30 January 2026, the U.S. Treasurys Office of Foreign Assets Control (OFAC) used an Iran-related action to designate two UK-registered crypto exchanges, ZEDCEX and ZEDXION, as Specially Designated Global Terrorists tied to the IRGC, explicitly sanctioning associated TRON wallet addresses alongside the corporate entities. In the same action, OFAC deleted multiple SOLTECH corporate entries from the SDN List and re-linked Iranian procurement figure Mohammad Soltanmohammadi to HODA TRADING, effectively refactoring part of its non-proliferation sanctions graph. Together, the moves show sanctions policy treating exchange operators plus their on‑chain infrastructure as a single control surface, while continuing quiet maintenance of the SDN graph for older proliferation networks.

## 2. Evidence & primary sources

- [ ] OFAC Recent Actions daily page for 30 Jan 2026  Iran-related designations; counter-terrorism designations; non-proliferation update and removal  https://ofac.treasury.gov/recent-actions/20260130
- [ ] OFAC press release on Iran-related sanctions targeting IRGC-linked crypto exchanges and repression actors (to be confirmed)  https://home.treasury.gov/news/press-releases/sb0375
- [ ] Consolidated SDN List extract / release notes capturing ZEDCEX / ZEDXION additions and SOLTECH / Soltanmohammadi changes (CSV / PDF)  https://ofac.treasury.gov/recent-actions/20260130

## 3. Pre‑mainstream check

- [ ] Searched major wire services (Reuters, AP, Bloomberg, AFP, etc.) for:
      - "ZEDCEX"; "ZEDXION"; "ZEDXION EXCHANGE"; "ZEDCEX EXCHANGE";
      - "IRGC crypto exchange" with date filter around 30 Jan 2026;
      - "Soltanmohammadi" + "Hoda Trading" and "Soltech".
- [ ] Searched at least 2 large general news aggregators for the same terms.
- [ ] No matching or clearly derivative coverage found as of: `2026-02-03T19:45Z`.

Notes:

- Expect some general Iran sanctions coverage focused on human-rights abuses and IRGC regional commanders; this bulletin is scoped narrowly to the structural treatment of crypto exchanges and SDN graph maintenance, which appears unreported.

## 4. Verification checklist

- [ ] Entity names and identifiers:
      - ZEDCEX EXCHANGE LTD (London address; website; any company number) match OFAC entry.
      - ZEDXION EXCHANGE LTD / ZEDXION LIMITED (London address; website; UK company number 13404089) match OFAC entry.
      - Mohammad Soltanmohammadi romanizations and HODA TRADING references match SDN update.
- [ ] Program tags and authorities:
      - Confirm SDGT / IFSR / IRAN-EO13902 tagging for ZEDCEX / ZEDXION and "Subject to Secondary Sanctions" language.
      - Confirm NPWMD / IFSR tagging and secondary sanctions for Soltanmohammadi / HODA TRADING.
- [ ] Crypto infrastructure:
      - Verify that OFAC lists specific TRON (TRX) wallet addresses for ZEDCEX / ZEDXION in the SDN List or associated annex.
- [ ] List maintenance:
      - Confirm that SOLTECH corporate entries are removed and that Soltanmohammadi is re-linked to HODA TRADING rather than SOLTECH in the updated SDN list.
- [ ] Dates and jurisdictions:
      - Action date 2026-01-30 and UK jurisdiction for the exchanges are correctly captured.

## 5. Risk & harm analysis (brief)

- [ ] Considered potential harms of publication (privacy, safety, market manipulation, etc.).
- [ ] Story avoids sharing sensitive personal data beyond what is already public in OFAC materials.
- [ ] No speculative financial advice or trading recommendations.

Short notes:

> The story summarizes official U.S. sanctions actions and does not identify private individuals beyond what OFAC has already published. It avoids referencing non-OFAC on-chain data or suggesting trading strategies; focus is on compliance and structural governance implications.

## 6. Publication record

To be filled in when publishing:

- **Git commit hash (content):** `...`
- **Git commit hash (index.html update):** `...`
- **First GitHub push with story:** `2026-02-03T..:..Z` (UTC)
- **GitHub Pages build complete:** `2026-02-03T..:..Z` (UTC, from Actions/Pages UI)
- **Optional external archive URL:** `https://web.archive.org/...`
