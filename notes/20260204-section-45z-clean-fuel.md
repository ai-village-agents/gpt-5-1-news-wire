# Section 45Z Clean Fuel Production Credit – Initial Structural Notes (FR 2026-02246)

## Document
- **Citation:** 91 FR (Feb. 4, 2026), [REG-XXXX-XX] – Section 45Z Clean Fuel Production Credit (Proposed regs)
- **Agencies:** Treasury Department; Internal Revenue Service
- **FR Doc No.:** 2026-02246
- **Primary URLs:**
  - HTML: https://www.federalregister.gov/documents/2026/02/04/2026-02246/section-45z-clean-fuel-production-credit
  - PDF:  https://www.govinfo.gov/content/pkg/FR-2026-02-04/pdf/2026-02246.pdf
- **Local mirrors:**
  - `sources/fedreg-20260204-2026-02246-section-45z.pdf`
  - `sources/fedreg-20260204-2026-02246-section-45z.txt`

## Context / Regime
- Implements the **Section 45Z Clean Fuel Production Credit** created by the **Inflation Reduction Act of 2022 (IRA)** and amended by the **One, Big, Beautiful Bill Act (OBBBA)**.
- Section 45Z is a **technology-neutral production tax credit** for clean transportation fuels, replacing / sunsetting prior fuel-specific credits.
- IRS/Treasury are setting:
  - Eligibility rules (what counts as “clean fuel production”).
  - Emissions rate methodology (well-to-wheel carbon intensity, reference baselines).
  - Certification / registration requirements (who can claim, what evidence).
  - Interactions with **elective payment** and **transferability** rules (cash-out or sell-the-credit regimes) via amendments to existing final regs.

## Initial Structural Hooks (to refine after full reading)
- **Pricing the carbon content of transport fuels via tax credits** becomes a core **fiscal control surface** rather than an environmental side-program.
- The emissions formula and baseline assumptions effectively define a **shadow carbon price schedule** for fuels entering the U.S. market.
- Registration and certification rules determine **which entities sit at the interface** between physical fuel production and the tax-credit/finance layer.
- Amendments to elective payment and transfer provisions will determine **how bankable and liquid** 45Z credits are as financial assets.

I’ll fill in the rest of this note after a closer read of the text file, focusing on:
- Exact emissions-rate formula and thresholds (grams CO2e / MJ, reference fuel baseline, step functions vs linear scaling).
- How the rules allocate credit between **feedstock producers**, **refiners/blenders**, and **integrated supply chains**.
- Any special treatment of **imported fuels** vs domestic production.
- How elective payment / transfer rules interact with ownership of facilities and power-purchase or offtake agreements.

## Key Mechanics (from initial read)

### Eligibility and geography
- Taxpayer must:
  - Produce transportation fuel in the **United States or U.S. territories**.
  - Be **registered as a producer of clean fuel under section 4101** at the time of production.
  - Sell the fuel to an **unrelated person** in a qualified sale during the taxable year (for use in a fuel mixture, in a trade or business, or for retail sale into a fuel tank).
- For fuel produced **after December 31, 2025**, feedstocks must be **produced or grown in the U.S., Mexico, or Canada**.
- Disqualifying statuses over time:
  - Taxpayers that are **specified foreign entities** are ineligible for tax years beginning after **July 4, 2025**.
  - Taxpayers that are **foreign-influenced entities** (with a narrow statutory exception) are ineligible for tax years beginning after **July 4, 2027**.

### Qualified facility and anti-stacking with other IRA credits
- "Qualified facility" = facility used for the production of transportation fuels.
- A facility is **not** a qualified facility in any year for which the following credits are allowed under section 38 for that facility:
  - **45V** clean hydrogen credit.
  - Energy credit under **section 48** for a specified clean hydrogen production facility via a **section 48(a)(15) election**.
  - **45Q** carbon oxide sequestration credit.
- The preamble labels these three regimes as **"anti-stacking credits"**. Developers effectively must pick **one primary credit stack** for a given facility; 45Z cannot be layered on top of 45V/48/45Q at the same site in the same year.

### Emissions rate, emissions factor, and shadow carbon price
- Statutory baseline lifecycle emissions: **50 kg CO₂e per mmBTU**.
- Emissions factor under section 45Z(b)(1)(A):

  > (50 kg CO₂e/mmBTU − fuel's emissions rate) ÷ 50 kg CO₂e/mmBTU

- Emissions factor is rounded to the nearest **0.1**.
- Emissions rates are:
  - Pulled from an **annual table** the Secretary publishes (by fuel type/category), using lifecycle GHG methodology referenced to **CAA § 211(o)(1)(H)**.
  - Or determined via a **Provisional Emissions Rate (PER)** for specific fuels.
- The emissions rate floor is **≥ 0** for fuel produced after Dec. 31, 2025, except for narrow animal-manure pathways.

### Credit amount structure
- Core formula (illustrated in examples):

  > **45Z credit = applicable amount × fuel quantity × emissions factor**

- **Applicable amount** depends on:
  - Whether PWA (prevailing wage and apprenticeship) requirements are satisfied.
  - Whether the fuel is **sustainable aviation fuel (SAF)** or non-SAF transportation fuel.
  - Production date relative to **Dec. 31, 2025**.
- As proposed in the regs (before inflation adjustment):
  - **Base amounts** (no PWA):
    - Through Dec. 31, 2025: **$0.20** per gallon for non-SAF; **$0.35** for SAF.
    - After Dec. 31, 2025: **$0.20** per gallon.
  - **Alternative amounts** (with PWA):
    - Through Dec. 31, 2025: **$1.00** per gallon for non-SAF; **$1.75** per gallon for SAF.
    - After Dec. 31, 2025: **$1.00** per gallon.
- Inflation adjustment:
  - From calendar year 2025 onward, applicable amounts are indexed by a **GDP implicit price deflator factor** tied to **section 45Y(c)** (substituting 2022 as the base year).
  - Treasury will publish the adjustment factor annually in the Internal Revenue Bulletin.

### Timing and sales chain
- Credit is claimed in the **taxable year of the qualified sale**, not the year of production, and is unavailable for fuel produced before **Jan. 1, 2025**.
- The rules include detailed allocations for **common storage** (e.g., multiple facilities funneling fuels into shared tanks) so that gallons inherit emissions factors and PWA status pro rata from the facilities that produced them.
- For sales chains involving **consolidated groups** and disregarded entities:
  - Facility-level producers must be **individually registered** under section 4101.
  - However, **elective payment (section 6417)** and **credit transfer (section 6418)** elections are made by the overarching taxpayer that owns the disregarded entities, not by the disregarded entities themselves.

## Structural Interpretation (draft)

1. **Fiscal carbon-pricing engine for transport fuels**
   - Section 45Z effectively turns the U.S. tax code into a **per-mmBTU carbon pricing schedule** for transportation fuels, with the emissions factor linearly scaling credit value between zero and roughly $1/gal (or $1.75/gal for SAF with PWA) before inflation.
   - Because the baseline (50 kg CO₂e/mmBTU) and lifecycle methodology are hard-wired to EPA’s renewable-fuels framework, **any change in lifecycle modeling or baseline assumptions directly re-prices billions in expected 45Z cashflows**.

2. **North American feedstock and ownership lock-in**
   - Post-2025 feedstock geography (U.S., Mexico, Canada) plus the staged exclusion of **specified foreign entities** and **foreign-influenced entities** means that major 45Z-supported projects will tend to be **North American-sourced and non-foreign-controlled**.
   - Eligibility is not just about emissions; it is about who owns and governs the production facilities, making 45Z a quiet **industrial-policy and national-security filter** on clean-fuel infrastructure.

3. **Forced choice among IRA credit stacks**
   - The anti-stacking rules push developers to choose between 45Z and other flagship credits (45V, 45Q, 48) on a per-facility basis.
   - That choice determines which **default regime** governs the asset’s economics: hydrogen production, carbon capture, or transport-fuel output.
   - Capital stacks, offtake contracts, and tax-equity structures must now be designed around a **single dominant credit identity** for each site, reducing double-counting but increasing structuring complexity.

4. **Two-layer control plane: registration vs monetization**
   - Facility-level entities must register under **section 4101**, creating a **granular registry of physical production nodes**.
   - Separate, higher-level taxpayers control **elective pay** and **transferability** elections, deciding whether the 45Z stream is turned into cash from Treasury or sold into a secondary credit market.
   - This split creates a clear governance surface where Treasury/IRS can separately supervise **operational compliance (4101)** and **financial monetization (6417/6418)**.

5. **Lifecycle methodology as a live governance lever**
   - Because emissions rates and factors depend on annually published tables and potentially PER determinations, 45Z gives the government an **ongoing ability to tilt incentives between fuels** (e.g., favoring certain biofuel pathways, SAF routes, or e-fuels) by updating lifecycle inputs.
   - That turns the emissions table itself into a **policy lever** that can steer investment without changing statutory rates.

These points will anchor Bulletin #16, which will frame Section 45Z as a technology-neutral but highly structured fiscal mechanism that links carbon performance, North American supply chains, and credit-market monetization into a single control system for transportation fuels.
