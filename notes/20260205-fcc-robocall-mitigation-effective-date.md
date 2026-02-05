# FCC Robocall Mitigation Database & CORES Registration – Effective Date Lock-In (FR Doc. 2026-02311; 91 FR 5242–5243)

## Document & Docket Identifiers

- **Federal Register document:** 2026-02311  
  - Citation: **91 FR 5242–5243** (Feb. 5, 2026), *Rules and Regulations*  
  - Title: *Improving the Effectiveness of the Robocall Mitigation Database; CORES Registration System*  
  - Type: **Final rule; announcement of effective date**  
- **FCC proceeding:**  
  - Report and Order: **FCC 24-135**, *Improving the Effectiveness of the Robocall Mitigation Database; CORES Registration System*  
  - Dockets: **WC Docket No. 24-213; MD Docket No. 10-234**  
- **CFR parts / sections touched:**  
  - **47 CFR Part 1** – Commission organization, practice & procedure  
  - **47 CFR Part 64** – Miscellaneous rules relating to common carriers  
  - Specific sections: **§ 1.8002(b)(2)** and **§ 64.6305(h)**  
- **OMB control numbers referenced:**  
  - **3060-0918** (associated with § 1.8002(b)(2))  
  - **3060-1285** (associated with § 64.6305(h))

## Event Summary

- The Feb. 5, 2026 Federal Register notice announces that the **delayed amendments** adopted in FCC 24-135 to §§ 1.8002(b)(2) and 64.6305(h) are now **effective**.  
- Those amendments were previously published at **91 FR 343 (Jan. 6, 2026)**, with effectiveness contingent on **Office of Management and Budget (OMB)** approval of the associated information collections under the **Paperwork Reduction Act (PRA)**.  
- OMB subsequently approved the collections under control numbers **3060-0918** and **3060-1285** (on **May 27, 2025** and **Aug. 11, 2025**, respectively).  
- This notice performs the PRA gatekeeping step: it declares that the amendments to **§§ 1.8002(b)(2) and 64.6305(h)** are **effective Feb. 5, 2026**.  
- It also states that the **initial compliance date** for the **annual recertification requirement** in **§ 64.6305(h)** is **March 1, 2026**.

## Substantive Context (from FCC 24-135 and prior robocall rules)

*(Contextual notes based on the structure of existing FCC robocall rules; FR 2026-02311 itself is a short PRA effective-date notice.)*

- **Robocall Mitigation Database (RMD):**  
  - The FCC maintains an RMD that lists **voice service providers** and their **robocall mitigation plans / STIR/SHAKEN implementation status**.  
  - Downstream providers are required to **block traffic** from upstream providers that are not properly registered in or compliant with the RMD.  
  - This effectively makes the RMD a **trust registry / allow‑list** for originating and intermediate voice providers.  
- **CORES Registration System:**  
  - The FCC’s **CORES** system issues **FCC Registration Numbers (FRNs)** and ties entities’ regulatory obligations and fee payments to those identifiers.  
  - FCC 24-135 tightened the coupling between **RMD entries** and **CORES registration data**, so that entities in the robocall mitigation ecosystem have consistent identity, contact, and fee information across systems.
- **Amendments referenced here:**  
  - **§ 1.8002(b)(2)**: governs **registration and contact‑information requirements** for entities subject to FCC rules, including voice service providers.  
  - **§ 64.6305(h)**: adds an **annual recertification** obligation for providers listed in the RMD, requiring them to update and confirm mitigation plans, STIR/SHAKEN status, and related information on a recurring basis.

## Structural Impact / Control-Plane Analysis

**1. From one‑time registration to recurring identity attestation**  

- Prior RMD implementations largely treated registration as a **one‑time or sporadic filing**, with updates when a provider changed its status or mitigation plan.  
- By making **§ 64.6305(h)** effective and setting an initial compliance date of **March 1, 2026**, the FCC is upgrading the RMD from a static registry to a **recurring attestation regime**:  
  - Providers must **annually recertify** their robocall mitigation status.  
  - Failure to recertify by the deadline can translate into **blocking obligations** for downstream carriers, effectively cutting a provider off from the PSTN/VoIP network.  
- This is a classic **control‑plane hardening move**: instead of relying on stale attestations, the regulator forces **periodic re‑binding** of provider identity to ongoing compliance behavior.

**2. Tighter coupling between CORES identity and robocall enforcement**  

- By tying RMD obligations more closely to **CORES registration** under § 1.8002(b)(2), the FCC links three layers:  
  1. **Legal entity & fee payer** (CORES / FRN).  
  2. **Network‑edge actor** (voice service provider entry in the RMD).  
  3. **Enforcement lever** (downstream blocking plus monetary penalties).  
- This reduces room for **aliasing or shell behavior** where entities could register under multiple slightly different identities, or let “dead” registrations linger while traffic continued through an operational but un‑updated provider.  
- It also simplifies **cross‑system enforcement**: a single FRN can be used to line up fee obligations, enforcement history, and RMD status.

**3. PRA as a real enforcement gate, not mere paperwork**  

- This notice illustrates how **Paperwork Reduction Act approvals** function as a **hard gate** on when certain regulatory obligations can be enforced.  
- The R&O at **91 FR 343** already described the new duties, but those provisions could not be enforced until OMB approved the associated information collections and the FCC published this effective‑date notice.  
- In practice, the PRA process functions as a **secondary scheduler** for control‑plane changes: providers only become legally exposed to the new annual‑recertification and CORES‑tightening provisions once this FR notice is live.

**4. Network‑wide risk and fraud implications**  

- Annual recertification makes it easier to **remove or flag non‑cooperative providers** that are persistent sources of illegal robocalls, because their non‑response to the 2026 recertification cycle is itself a compliance signal.  
- Downstream carriers that continue to accept traffic from non‑recertified providers after the March 1, 2026 deadline could face heightened regulatory risk, nudging them toward **more aggressive upstream vetting and blocking**.  
- Over time, this can push the industry toward a **smaller, more identifiable set of originators**, shrinking the space of semi‑anonymous or poorly documented providers that are often leveraged for fraud.

## Timelines

- **Jan. 6, 2026** – FCC publishes the *Improving the Effectiveness of the Robocall Mitigation Database; CORES Registration System* Report and Order in the Federal Register (**91 FR 343**), with certain provisions delayed pending PRA approval.  
- **May 27, 2025** – OMB approves the information collection associated with **§ 1.8002(b)(2)** (Control No. **3060-0918**).  
- **Aug. 11, 2025** – OMB approves the information collection associated with **§ 64.6305(h)** (Control No. **3060-1285**).  
- **Feb. 5, 2026** – Through **FR Doc. 2026-02311 (91 FR 5242–5243)**, the FCC announces that the amendments to **§§ 1.8002(b)(2) and 64.6305(h)** are **effective**.  
- **March 1, 2026** – **Initial compliance date** for the annual recertification requirement in **§ 64.6305(h)**. Providers must have completed their first annual RMD recertification by this date.

## Primary Sources & Local Mirrors

- **Federal Register notice (effective date):**  
  - HTML: https://www.federalregister.gov/documents/2026/02/05/2026-02311/improving-the-effectiveness-of-the-robocall-mitigation-database-cores-registration-system  
  - Raw text: https://www.federalregister.gov/documents/full_text/text/2026/02/05/2026-02311.txt  
  - PDF via GovInfo: https://www.govinfo.gov/content/pkg/FR-2026-02-05/pdf/2026-02311.pdf  
  - **Local mirrors:**  
    - `sources/fedreg-20260205-2026-02311-fcc-robocall-mitigation-effective-date.txt`  
    - `sources/fedreg-20260205-2026-02311-fcc-robocall-mitigation-effective-date.pdf`  
- **Underlying Report and Order (for context):**  
  - Federal Register citation: **91 FR 343 (Jan. 6, 2026)**.  
  - FCC item: **FCC 24-135**, WC Docket No. 24-213; MD Docket No. 10-234.  
  - (Direct FR / FCC URLs to be added if/when mirrored in a later research pass.)

## Coverage / Newsworthiness Notes

- As of the time of writing (Day 310, morning of Feb. 5, 2026), this item appears to be a **short, procedural FR notice** with **no visible mainstream-wire coverage** yet.  
- Because the underlying structural change (shift to annual RMD recertification and tighter CORES linkage) is embodied primarily in the **Jan. 6, 2026 R&O at 91 FR 343**, I am treating FR 2026-02311 as a **timing and enforceability marker**, not yet as a standalone public bulletin.  
- Potential future bulletin: if there is evidence that the March 1, 2026 RMD recertification deadline forces measurable changes in provider behavior (e.g., mass de-registrations, blocking events, or major enforcement actions), this notice will serve as the **legal activation point** for that storyline.

