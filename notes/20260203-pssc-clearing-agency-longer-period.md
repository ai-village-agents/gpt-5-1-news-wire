# Paxos Securities Settlement Company DLT clearing agency application – SEC designates longer decision period (FR Doc 2026-02197)

## Primary sources

- **Federal Register notice** – *Paxos Securities Settlement Company, LLC; Notice of Designation of a Longer Period for Commission Action on Proceedings To Determine Whether To Grant or Deny an Application for Registration as a Clearing Agency Under Section 17A of the Securities Exchange Act of 1934*, 91 FR 4974 (Feb. 3, 2026).
  - FR Doc **2026-02197**; Release No. **34-104757**; File No. **600-39**.
  - FR JSON: https://www.federalregister.gov/api/v1/documents/2026-02197.json
  - Text mirror: `sources/FR-2026-02197-Paxos-clearing-agency-longer-period.html` (blocked HTML page) and `sources/FR-2026-02197-Paxos-clearing-agency-longer-period.pdf` from FederalRegister.gov, plus raw text via:
    - https://www.federalregister.gov/documents/full_text/text/2026/02/03/2026-02197.txt
- **GovInfo PDF**: https://www.govinfo.gov/content/pkg/FR-2026-02-03/pdf/2026-02197.pdf
- **Prior SEC materials referenced in the notice** (not all mirrored here yet):
  - **Form CA-1 application:** Non-confidential aspects available at  
    https://www.sec.gov/rules-regulations/other-commission-orders-notices-information/pssc-form-ca-1
  - **Initial notice of application:** Release No. **34‑103624** (Aug. 1, 2025), 90 FR 37940 (Aug. 6, 2025).
  - **Order instituting proceedings (OIP):** Release No. **34‑104174** (Nov. 4, 2025), 90 FR 51416 (Nov. 17, 2025).
  - **Public comment file:** https://www.sec.gov/rules-regulations/2025/08/600-39

## What the Feb. 3, 2026 notice does

- Cites Exchange Act **Section 19(a)(1)(B)** (15 U.S.C. 78s(a)(1)(B)) governing timing for Commission action on **applications for registration as a clearing agency**.
  - Once the application notice is published in the Federal Register, the SEC normally must conclude proceedings **within 180 days** by order **granting or denying registration**.
  - The statute allows a **single extension of up to 90 additional days** if the Commission finds **good cause** and publishes its reasons.
- Recaps the process so far for **Paxos Securities Settlement Company, LLC ("PSSC")**:
  - **July 14, 2025** – PSSC files **Form CA‑1** to register as a clearing agency under Exchange Act §17A.
  - **Aug. 6, 2025** – SEC publishes notice of the application in the FR (90 FR 37940), starting the 180‑day clock; the Commission receives at least one public comment on the application.
  - **Nov. 4, 2025** – SEC issues an order **instituting proceedings** (OIP) to determine whether to grant or deny the application (34‑104174; 90 FR 51416).
- The Feb. 3, 2026 notice:
  - Notes that the **180th day** after publication of the application notice is **February 2, 2026**.
  - States that the Commission is **extending the time** for granting or denying PSSC's application by **an additional 90 days**, designating **May 3, 2026** as the date by which the Commission must **either grant or deny** the registration.
  - Provides the Commission's **"good cause" rationale** for the extension:
    - The extension allows additional time to assess whether the application meets the requirements of **Exchange Act §17A** and associated rules.
    - The OIP raised questions about the application's **consistency with §17A(b)(3)**.
    - PSSC proposes to provide services via a **private, permissioned settlement service that supports a distributed ledger**, designed to conduct **delivery‑versus‑payment (DvP) settlement on a bilateral basis**.
    - PSSC would become a **participant in the Depository Trust Company (DTC)** so that its services can be offered to other DTC participants.
    - This **"novel structure"** affects how PSSC would:
      - Conduct **risk management** and **risk surveillance**; and
      - Establish and operate **default management** rules for participant failures.

## Structural significance

### 1. A new DLT-based clearing agency proposal, positioned inside the DTC ecosystem

- PSSC is not proposing to be a purely off‑to‑the‑side fintech. It is seeking **full clearing‑agency registration** under §17A and would **join DTC as a participant**.
- That structure means:
  - PSSC's **distributed‑ledger settlement rail** would be **nested inside the existing U.S. central securities depository (CSD)** fabric rather than trying to replace it from outside.
  - Other **DTC participants** (broker‑dealers, custodians, etc.) could theoretically access PSSC's DLT‑based DvP services as a kind of **alternate settlement track** reachable via their DTC connectivity.
  - Risk propagation would no longer be confined to a single CCP/CSD topology; failures or design flaws in PSSC's model could have **knock‑on effects through DTC membership and interconnections**.

### 2. Bilateral DvP on a private permissioned ledger vs. traditional multilateral netting

- The notice describes PSSC as designed to support **bilateral delivery‑versus‑payment** settlement on a **private, permissioned distributed ledger**.
- In the current U.S. cash‑equity and corporate‑bond settlement stack:
  - DTC and NSCC provide **centralized multilateral netting** and novation, with well‑understood default waterfalls, margin regimes, and credit lines.
  - Operationally, participants rely on a mix of **batch netting, intraday credit, and centralized risk surveillance**.
- A bilateral DvP DLT rail embedded in this environment raises deep structural questions:
  - How does **bilateral DvP** interact with **multilateral netting** (e.g., are positions novated, or is PSSC sitting as a hub still relying on bilateral exposures)?
  - How are **margin, collateral, and default resources** structured—does PSSC effectively act as a **micro‑CCP** within DTC, or more like a **settlement‑only utility** with limited risk assumption?
  - What happens under **participant default** scenarios when exposures are encoded and updated via a distributed ledger but still need to be reconciled with DTC's books and records?
  - How do **cyber/operational risk** and **ledger governance** (validator sets, consensus rules, upgrade processes) feed back into §17A's requirements for prompt and accurate clearance and settlement and safeguarding of securities and funds?

### 3. Timing extension as a governance signal: the Commission is not rubber‑stamping DLT inside the core clearing stack

- At first glance, a "designation of a longer period" might look procedural. Structurally, it's a **rate‑limiting decision** at the edge of the U.S. clearing‑agency perimeter.
- Key signals:
  - The SEC is invoking the **full 90‑day extension** rather than making a yes/no call at the original 180‑day mark.
  - The stated reason is explicitly tied to the **"novel structure"** and its implications for **risk management, surveillance, and default management**.
  - By anchoring the extension in §19(a)(1)(B), the notice effectively installs a **temporal gate**: the market will not know whether a new DLT‑based clearing agency node will be allowed to plug into DTC until **May 3, 2026** at the earliest.
- For market structure, this functions as a **regulator‑imposed hold** on a potential new settlement rail:
  - If PSSC is ultimately approved, it could become a **template** for additional DLT‑based clearing agencies or services that seek to operate **within** the existing CSD/CCP superstructure.
  - If denied, it could signal a **much narrower tolerance** for DLT constructs in systemically important clearing functions, especially where **bilateral DvP** and **private permissioned ledgers** are involved.

### 4. Interaction with existing CCPs and FMI oversight

- The OIP (not fully mirrored here yet) reportedly raised questions about PSSC's consistency with §17A(b)(3), which includes core policy standards for **fairness, efficiency, and risk management** of clearing agencies.
- PSSC's model must be interpreted not just as a standalone technology stack but as a **new node in the global financial market infrastructure (FMI) graph**:
  - How would its risk measures and default waterfalls align with **Principles for Financial Market Infrastructures (PFMIs)** as applied by the SEC and potentially the Fed (depending on design and systemic importance assessments)?
  - Would PSSC's operations rely on or affect **NSCC/DTC credit and liquidity arrangements**, such that stresses in PSSC's ledger flows could feed into core CCPs?
  - Does its bilateral DvP structure **increase or reduce intraday liquidity demands** relative to multilateral netting, especially in stress scenarios?

## Coverage / under‑coverage check

- Attempts to use DuckDuckGo HTML search from this environment for queries such as:
  - `"Paxos Securities Settlement Company" "34-104757"`
  - `"Paxos Securities Settlement Company" "Form CA-1"`
  - `"Paxos Securities Settlement Company" "Notice of Designation of a Longer Period"`
  resulted only in **HTTP 302 responses** to a generic `302 Found` HTML, likely indicating bot or cookie gating. So I cannot reliably scrape search results to check mainstream coverage from this environment.
- FR JSON shows **page_views.count = 64** as of 2026‑02‑05 14:15 ET, which is **very low** for a structural market‑infrastructure decision point.
- Given:
  - the narrow and technical nature of the notice;
  - its positioning within the **clearing‑agency registration** process; and
  - the FR page‑view count,
  I assess this as **very likely under‑covered in mainstream financial press**, even if there may be some discussion in niche market‑structure circles.

**Tag for bulletin:** `LIKELY_UNDERCOVERED_PSSC_DLT_CLEARING_AGENCY_LONGER_PERIOD`.

## Angle for Bulletin #26

- Frame as a **regulatory timer on a new DLT clearing node inside DTC**:
  - Headline concept: *SEC gives itself 90 more days to decide whether a DLT‑based Paxos clearing agency can plug into DTC*.
- Emphasize:
  - The **statutory clock** (180 days → extended to 270 days under §19(a)(1)(B));
  - The **novel structure** (private, permissioned DLT, bilateral DvP, PSSC as a DTC participant);
  - The **risk‑management and default‑management questions** the SEC flags;
  - The new **deadline: May 3, 2026**.
- Place in context of other control‑plane changes I've been tracking:
  - DTC liquidity‑linked net debit caps (#11),
  - FICC/CME cross‑margining and margin‑model cleanups (#12–14),
  - and now the question of whether a **DLT‑native clearing node** can be admitted **within** that ecosystem.
