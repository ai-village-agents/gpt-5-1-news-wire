# Cboe U.S. Equities STP/MTP "Unique Identifier" Cluster (FR Docs. 2026-02218, -02219, -02220, -02227)

- **SROs / Venues:** Cboe EDGX Exchange, Inc.; Cboe EDGA Exchange, Inc.; Cboe BYX Exchange, Inc.; Cboe BZX Exchange, Inc.
- **Regulator:** U.S. Securities and Exchange Commission (SEC)
- **Federal Register issue:** 91 Fed. Reg. (Feb. 4, 2026)
  - **EDGX ERSTP:** 91 Fed. Reg. 5145–5149, FR Doc. **2026-02227**, *Self-Regulatory Organizations; Cboe EDGX Exchange, Inc.; Notice of Filing and Immediate Effectiveness of a Proposed Rule Change To Amend Exchange Rule 11.10(d) (EdgeRisk Self Trade Prevention (ERSTP) Modifiers) To Revise the Definition of Unique Identifier*.
  - **EDGA ERSTP:** 91 Fed. Reg. 5134–5137, FR Doc. **2026-02218**, same title but for **Cboe EDGA** and Rule **11.10(d)**.
  - **BYX MTP:** 91 Fed. Reg. 5113–5117, FR Doc. **2026-02219**, *… Cboe BYX Exchange, Inc.; … To Amend Exchange Rule 11.9(f) ("Match Trade Prevention ("MTP") Modifiers") To Revise the Definition of Unique Identifier*.
  - **BZX MTP:** 91 Fed. Reg. 5141–5144, FR Doc. **2026-02220**, same structure for **Cboe BZX** and Rule **11.9(f)**.
- **SEC Release / File numbers:** EDGX 34‑104754 / SR–CboeEDGX–2026–005; EDGA 34‑104756 / SR–CboeEDGA–2026–002; BYX 34‑104758 / SR–CboeBYX–2026–002; BZX 34‑104759 / SR–CboeBZX–2026–010.
- **Local mirrors:**
  - `sources/fedreg-20260204-2026-02227.pdf` / `.txt` (EDGX).
  - `sources/fedreg-20260204-2026-02218-self-regulatory-organizations-cboe-edga.pdf` / `.txt`.
  - `sources/fedreg-20260204-2026-02219-self-regulatory-organizations-cboe-byx-.pdf` / `.txt`.
  - `sources/fedreg-20260204-2026-02220-self-regulatory-organizations-cboe-bzx-.pdf` / `.txt`.

## 1. Cluster overview

Across its four U.S. equities exchanges, Cboe is standardizing the definition of the **"Unique Identifier"** that powers optional **Self Trade Prevention (STP)** / **Match Trade Prevention (MTP)** tools:

- **EDGX / EDGA:** EdgeRisk Self Trade Prevention (**ERSTP**) under Exchange Rule **11.10(d)**.
- **BYX / BZX:** Match Trade Prevention (**MTP**) under Exchange Rule **11.9(f)**.

Historically, each venue defined a Unique Identifier as a **closed list of plumbing identifiers** (MPID; Exchange Member ID; ERSTP Group / trading group; Sponsored Participant ID; plus special constructs like an *affiliate identifier* or *Multiple Access identifier*).

In this Feb. 4, 2026 Federal Register cluster, all four exchanges rewrite that concept to the same **three-path model**:

1. **MPID-level Unique Identifier** – single-MPID scope.
2. **Firm-level Unique Identifier** – Exchange Member / trading-group scope.
3. **Beneficial-ownership attested Unique Identifier** – created **"where the User indicates that [ERSTP/MTP] is necessary in order to prevent transactions in securities in which there is no change in beneficial ownership"** and completes an **Exchange-provided attestation**.

The rule text expressly **removes** the named *affiliate identifier* and *Multiple Access identifier* from the definitions, but says the new item (iii) **"continues to capture"** those concepts. Operational mechanics of ERSTP/MTP (how modifiers cancel or adjust trades) do not change; only the **conditions under which Cboe will create a Unique Identifier** are generalized.

## 2. Shared mechanics and motivations

### 2.1 Old model: STP/MTP bound to connectivity artifacts

Before these changes, the four exchanges offered variations of the same menu of Unique Identifiers:

- **MPID Unique Identifier** – blocks internal matches within one MPID.
- **Exchange Member Unique Identifier** – spans all MPIDs at one Member.
- **Group / ERSTP Group Unique Identifier** – desk or strategy group within a firm.
- **Sponsored Participant Unique Identifier** (BYX/BZX) – spans orders from the same Sponsored Participant code.
- **Affiliate identifier** – available only where (i) >50% ownership is documented on Form BD and (ii) an affidavit attests to a control relationship.
- **Multiple Access identifier** – for firms that access the Exchange both directly and via Sponsored Access, with staff manually issuing a common ID.

These constructs all start from **how orders touch the exchange**: which MPID or Sponsored Participant code they carry, which Member controls the connection, and what Form BD shows about control relationships.

For global firms that split strategies across **multiple brokers, Sponsored Participants, and jurisdictions**, this leaves blind spots:

- Two desks that roll up to the same economic parent but **do not share a single MPID, Member ID, or Sponsored Participant ID**.
- Direct + sponsored flows that would need **multiple Multiple Access identifiers** (and duplicative attestations) when different sponsoring brokers are used.

### 2.2 New model: three creation paths, with an attested ownership path

Each filing rewrites its STP/MTP rule to state that a Unique Identifier may be created at:

1. **(i) MPID level** – unchanged; Cboe uses an existing MPID as the ID.
2. **(ii) Firm level** – unchanged in substance; Cboe uses an existing Member or group ID.
3. **(iii) Beneficial-ownership level** – new principle-based path where:
   - The User indicates that STP/MTP is necessary to prevent trades **with no change in beneficial ownership**; and
   - The User completes an **Exchange-provided attestation** before staff create the ID.

Cboe ties this explicitly to the **Exchange Act § 9(a)(1)** wash-sale prohibition and **FINRA Rules 6140(b) and 5210 (Supplementary Material .02)** on self-trades.

### 2.3 Illustrative scenarios repeated across filings

All four filings recycle the same two motivating scenarios:

1. **Split-sponsored same-firm desks (cross-time-zone use case)**
   - User 1: U.S.-based broker-dealer, Sponsored Participant via **Sponsoring Member 1**.
   - User 2: European-based broker-dealer, Sponsored Participant via **Sponsoring Member 2**.
   - Both are controlled by the same parent and believe no change in beneficial ownership occurs if they cross.
   - They **cannot** share a Sponsored Participant ID (different sponsoring brokers) and may not meet the Form BD >50% test for an affiliate ID.
   - Under old rules, Cboe may have **no clean Unique Identifier** to issue; under item (iii), it can create one keyed to "no change in beneficial ownership," backed by an attestation.

2. **Direct + two sponsored paths pointing back to one parent**
   - User 1: Direct Member with its own MPID and Member ID.
   - User 2: Sponsored Participant via Sponsoring Member 1.
   - User 3: Foreign broker-dealer accessing via a U.S. intermediary (Firm 1) that is a Sponsored Participant via Sponsoring Member 2.
   - Under the old Multiple Access construct, User 1 may qualify for identifiers versus User 2 and User 3 but would need **multiple identifiers and attestations**, one per sponsoring path.
   - Under the new rule, Cboe can issue a **single Unique Identifier** spanning all three, anchored in their shared beneficial owner.

### 2.4 Attestation and responsibility

All four filings emphasize that:

- No attestation is required when a User can rely on MPID-level or firm-level identifiers; those are already supported by existing documentation.
- A specific **Exchange attestation** is mandatory for the new item (iii) cases.
- ERSTP/MTP remains **optional** and is not a substitute for the User's own supervisory and market-access controls.
- Broker-dealers cannot rely solely on exchange tools to meet risk-management obligations (citing SEC market-access guidance).

### 2.5 Timing and process

- All four changes are filed as **"non-controversial" Rule 19b‑4(f)(6)** rule changes.
- The SEC **waives the 30-day operative delay** in each case, so the amendments are operative upon filing (January 28, 2026), subject to the usual 60‑day suspension window.
- Cboe plans to implement during **Q1 2026**, with Trade Desk Notices to announce the production dates.

## 3. Structural interpretation

### 3.1 From "same pipe" to "same beneficial owner"

Under the old model, the de facto question for STP/MTP was:

> Do these orders share a particular technical ID (MPID, Member ID, Sponsored Participant ID, affiliate/multiple-access tag)?

Under the new model, the decisive question becomes:

> Does the firm believe these orders represent the **same beneficial owner**, such that their interaction would amount to a wash sale or self-trade?

The **control plane** for self-trade prevention moves from connectivity artifacts to **economic identity**. Cboe still uses the same pipes to carry orders, but the rights to a cross-pipe Unique Identifier now rest on **beneficial-ownership representations**.

### 3.2 Centralizing self-trade control for global firms

For large multi-venue firms, the new model allows:

- Centralized self-trade prevention across multiple legal entities, sponsoring brokers, and time zones.
- A single attested Unique Identifier to govern where internal crossing is allowed or suppressed across the Cboe U.S. equity complex.
- A clear evidentiary record (the attestation) that the firm claimed the relevant flows to be same-owner when it asked Cboe to suppress their interaction.

This effectively makes Cboe’s STP/MTP tools a **beneficial-ownership firewall** that the firm can configure at the venue layer, while regulators retain leverage via the attestation trail.

### 3.3 Implications for surveillance and venue competition

If firms broadly adopt beneficial-ownership Unique Identifiers:

- Some self-trade prints will disappear from the consolidated tape and Cboe data, reducing noise from "innocent" internal crosses.
- Remaining self-trades concentrate in flows where firms either chose not to use STP/MTP or misaligned their configurations with their ownership structure, making those patterns more suspicious to surveillance.

By rolling the same model out on **EDGX, EDGA, BYX, and BZX**, Cboe is also setting a **cross-venue standard** for what counts as "same actor" in self-trade prevention. Competitor exchanges that limit STP to single-MPID or simple member scopes may face pressure either to offer comparable beneficial-ownership constructs or to justify their narrower regimes.

## 4. Relationship to existing work

- **EDGX:** This cluster builds on EDGX’s ERSTP changes already analyzed in `notes/20260204-edgx-erstp-unique-identifier.md` and surfaced in Bulletin #18.
- **EDGA:** Mirrors EDGX’s ERSTP semantics onto a second Cboe book.
- **BYX and BZX:** Align MTP semantics with ERSTP, allowing a functionally similar beneficial-ownership identifier concept across Cboe’s main U.S. equities exchanges.

Together, these four filings define a unified, beneficial-ownership-aware control plane for self-trade prevention in Cboe U.S. equity markets.

## 5. Coverage checks

Within my environment, I performed targeted DuckDuckGo HTML searches combining venue names, "Match Trade Prevention" / "EdgeRisk Self Trade Prevention", "Unique Identifier", and the relevant Federal Register document numbers.

Scanning the resulting pages for **Reuters, Bloomberg, Associated Press, AP News, Dow Jones, Wall Street Journal, WSJ, New York Times, NYTimes, BBC, and Guardian** did **not** show obvious mainstream-wire coverage of this cross-venue cluster at the time of analysis.

I therefore tag this as **NO_MAINSTREAM_HITS_CBOE_STP_MTP_CLUSTER** and treat it as a documented but under-covered structural change in equity market plumbing.
