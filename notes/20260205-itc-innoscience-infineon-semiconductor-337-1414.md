# ITC 337-TA-1414 semiconductor exclusion rail – Infineon vs Innoscience (FR Doc. 2026-02297)

## Discovery path

- **Date surfaced:** 2026-02-05 via `scripts/fr_discovery_helper.py` for documents published 2026-02-05.
- **Federal Register document:**
  - Title: *"Certain Semiconductor Devices and Products Containing the Same; Notice of a Commission Determination To Review in Part a Final Initial Determination Finding a Violation; Request for Written Submissions on Remedy, the Public Interest, and Bonding"*
  - Citation: **91 FR 5259–5261 (Feb. 5, 2026)**.
  - FR Doc. No. **2026-02297**.
  - Docket: **Investigation No. 337-TA-1414** (U.S. International Trade Commission).
  - JSON: `https://www.federalregister.gov/api/v1/documents/2026-02297.json`.
  - Text: `sources/fedreg-20260205-2026-02297-itc-semiconductor-devices-337-1414.txt`.
  - PDF:  `sources/fedreg-20260205-2026-02297-itc-semiconductor-devices-337-1414.pdf`.

## What the notice does

- Announces that the **ITC Commission** has decided to **review in part** the **Final Initial Determination (Final ID)** in Investigation **337-TA-1414**, involving "certain semiconductor devices and products containing the same."
- Confirms that the ALJ found a **violation of section 337** by **Innoscience** with respect to **Infineon**'s **'481 patent** (U.S. Patent No. 9,899,481) and **no violation** as to the **'755 patent** (U.S. Patent No. 9,070,755).
- Notes the ALJ's **recommended determination (RD)** that, if the Commission ultimately finds a violation, it should issue:
  - A **limited exclusion order (LEO)**; and
  - **Cease and desist orders (CDOs)** against Innoscience entities, based on significant U.S. inventory and operations.
- Announces that the Commission will **review** portions of the Final ID relating to the '481 patent, including:
  - **Claim construction** of "lateral transistor devices";
  - **Infringement** findings;
  - **Domestic industry** (technical and economic prongs);
  - **Validity** (including obviousness over prior art like Nega + Roberts).
- Requests **written submissions** from parties, interested government agencies, and third parties on:
  - The reviewed patent issues (obviousness, domestic industry evidence);
  - **Remedy** (scope/structure of any exclusion and cease-and-desist orders);
  - **Public interest**; and
  - **Bonding** (level of bond for imports during the Presidential review period).
- Sets detailed **briefing deadlines and page limits**:
  - Initial submissions (including proposed remedial orders) due **February 17, 2026**;
  - Reply submissions due **February 24, 2026**;
  - Page caps: 30 pages (opening), 15 pages (reply) for parties; 10 pages for third parties/agencies.
- Asks specific questions on:
  - **Obviousness** of claims 1–3 and 6 of the '481 patent in light of Nega + Roberts, including whether Infineon's packaging-complexity arguments undermine a prima facie showing;
  - How to properly do a **quantitative/qualitative assessment** of domestic-industry investments, including incorporation of non-U.S. activities (e.g., via value-added analysis or domestic vs foreign investment comparisons), and use of confidential exhibit **CDX-0005C.25**.
- Flags that any eventual remedy could be subject to **Presidential (USTR) review** under the standard 60‑day process, with entries during that period subject to **bond** determined by the Commission.

## Structural significance

### 1. A live exclusion rail on power-semiconductor supply

- Investigation **337-TA-1414** pits **Infineon** (complainant) against **Innoscience** (respondent) over **semiconductor devices**, very likely **GaN power transistors / power ICs** given the named patents and known product lines.
- The ALJ's recommended **limited exclusion order** and **cease and desist orders** would, if adopted, create a **hard gate** on importing Innoscience products into the U.S., with direct implications for:
  - **Power electronics** in **data centers, EVs, fast chargers, industrial drives, and consumer electronics**;
  - **Design-in strategies** for OEMs who may have qualified Innoscience devices as second-source or cost-down alternatives.
- The Commission's partial review means the **exclusion rail is live but not yet locked in**. Depending on how it resolves claim construction, validity, and domestic-industry issues, the Commission could:
  - Uphold a full violation finding and adopt the LEO/CDOs;
  - Narrow the scope of violation and remedy; or
  - Reverse on all or part of the '481 patent claims, materially changing the trajectory for Innoscience's U.S. market access.

### 2. Patent-claim construction as infrastructure control

- The Commission's decision to review **"lateral transistor devices"** claim construction is not a narrow legal curiosity; it effectively decides **which classes of GaN/power device architectures fall under Infineon's exclusion perimeter**.
- A more expansive construction:
  - Broadens the set of Innoscience (and potentially third-party) devices that could be excluded or enjoined.
  - Raises the risk that **follow-on ITC complaints** might invoke similar claim interpretations against additional respondents.
- A narrower construction:
  - Preserves more design/architecture options for GaN device makers seeking to avoid Infineon's patent fence.
  - Limits the reach of any eventual exclusion order, constraining its impact on the broader supply topology.
- In other words, the **semantics of a single phrase in the '481 patent** materially affects the **shape of the global GaN device design space** for products entering the U.S. market.

### 3. Domestic-industry calculus and offshored fabrication

- The Commission explicitly asks how to evaluate Infineon's **domestic-industry investments** when substantial manufacturing and other activities occur **outside** the U.S.
- It gestures toward **value-added and comparative investment analyses**:
  - Comparing domestic vs. foreign investments;
  - Relating domestic investments to total product value or revenues;
  - Using confidential data (e.g., CDX-0005C.25) to quantify the U.S. share of the economic activity around DI products.
- This is structurally important because it helps set **how much U.S.-based activity is required** to wield section 337 as a trade-enforcement tool when fabrication and assembly are largely offshore.
  - A **lenient domestic-industry threshold** makes it easier for IP owners with limited U.S. physical footprint to secure exclusion orders.
  - A **stricter, quantitatively grounded threshold** could narrow access to the ITC remedy for firms whose U.S. presence is more sales/marketing than manufacturing/engineering.
- As more semiconductor companies restructure around **globalized fabs and contract manufacturing**, the way the Commission resolves this question will influence **who can credibly threaten exclusion** in future ITC power‑device disputes.

### 4. Overlap with prior GaN ITC remedies and stacking risk

- The Commission explicitly asks parties to identify **which accused '481 patent products are already subject to remedial orders in Investigation No. 337-TA-1366**, and to quantify:
  - Market shares of the accused products (including those not subject to 1366 remedies);
  - Market share of Infineon's domestic-industry products; and
  - Whether competitors can **backfill U.S. demand** if new exclusion orders issue.
- That signals concern about **stacked or overlapping exclusion orders** in the same product space:
  - If 337‑TA‑1366 already constrains a major slice of GaN/power devices, adding a fresh LEO/CDOs here could **concentrate supply** in very few hands.
  - The Commission is trying to quantify **public-interest impacts**: Would another exclusion order materially constrict U.S. access to high‑efficiency power devices?
- This is effectively a **supply-chain risk analysis** embedded in the trade‑remedy process, and it will influence how aggressively IP holders can use the ITC to reshape GaN/power‑device markets.

### 5. Remedy design, Presidential review, and bond as operational dials

- The notice walks through the **standard ITC remedy menu** and **Presidential (USTR) review window**, but in a context where:
  - Accused products are likely integrated into **critical infrastructure** (data centers, EVs, industrial power, etc.);
  - There is an existing backdrop of **another GaN-related ITC investigation (337‑TA‑1366)**.
- The Commission explicitly invites submissions on:
  - **Form of remedy** (scope of LEO, CDOs, any carve‑outs or grace periods);
  - **Bond level** during the Presidential review period.
- For OEMs and integrators, the **bond amount and any carve‑outs** can decide whether they:
  - Continue importing Innoscience-based assemblies at a (possibly large) financial cost while the remedy is under review; or
  - Rush to **requalify alternate suppliers**, with all the accompanying redesign and validation risks.
- This makes the 2026‑02‑17 and 2026‑02‑24 submissions windows a **live policy lever** for industry coalitions to argue about:
  - Supply‑chain resilience / national‑security implications of exclusion;
  - Transition timelines needed to avoid sudden shortages in key sectors.

## Coverage / likely under‑coverage

- FR JSON `page_views.count` is **44** as of 2026‑02‑05 16:15 ET – very low for a notice that could materially affect **semiconductor supply chains** and **ITC remedy doctrine**.
- ITC 337 remedy and domestic‑industry questions are typically covered only by:
  - Specialized trade/IP outlets;
  - Paywalled legal trade publications.
- Mainstream tech and business press tend to cover ITC cases **only at final remedy** (e.g., "ITC bans imports of X"), not at this **critical pre‑remedy briefing stage** where:
  - Claim construction and domestic‑industry framing are still in flux; and
  - Third‑party comments on public interest and supply-chain effects are actively solicited.
- Given search‑result scraping constraints and typical media behavior, this notice is **very likely under‑covered**, especially from a **semiconductor‑infrastructure and remedy‑design** perspective.

## Provisional bulletin angle

Working title for a future bulletin (likely **Bulletin #28**):

> **ITC opens a live exclusion rail on GaN power semiconductors: Infineon vs Innoscience, with domestic‑industry math and prior GaN remedies under review**

Core framing:

- Treat Investigation **337‑TA‑1414** as a **control lever** over which GaN/power‑semiconductor architectures and suppliers can serve the U.S. market.
- Emphasize that the Commission is actively asking for input on:
  - How far Infineon's patent fence should reach ("lateral transistor devices");
  - How to score domestic‑industry investments when fabrication is offshore;
  - How to avoid stacking exclusion orders that over‑concentrate supply.
- Highlight that the **comment and reply windows (through Feb. 24, 2026)** are the main remaining opportunities for:
  - OEMs, system integrators, and industry groups to document concrete **supply‑chain impacts**;
  - Policymakers to reconcile **IP enforcement** with **semiconductor‑resilience goals**.

If elevated, the bulletin should map this ITC proceeding into the broader **power‑electronics infrastructure** story: who controls the **switching devices** at the heart of EVs, cloud power shelves, and high‑efficiency chargers, and how trade remedies can quietly redraw that map.
