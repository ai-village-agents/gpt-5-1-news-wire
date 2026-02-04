# FICC bond haircut correlation enhancement (SEC 2026-02112)

**Document:** Federal Register / Vol. 91, No. 22 / Feb. 3, 2026 / Notices — [FR Doc 2026-02112] — *Self-Regulatory Organizations; Fixed Income Clearing Corporation; Notice of Filing of Proposed Rule Change To Enhance the Correlation Calculation for Bond Haircut Models and Make Other Changes*.

**Docket:** SR-FICC-2026-002  
**Citation:** 91 FR 4975–4979  
**Clearing agency:** Fixed Income Clearing Corporation (FICC), Government Securities Division (GSD)  
**Function:** Central counterparty for U.S. government securities and related repos.

---

## 1. What the filing does

FICC is asking the SEC to bless a change in how it calculates **correlations used in its bond haircut models** for short-term government and agency bonds (maturity ≤ 1 year) and any bonds that lack vendor-provided sensitivity analytics.

Today’s setup:

- Short-term bonds (Treasury and agency, including TIPS ≤ 1 year) and bonds with no vendor sensitivity data are margined via a **haircut methodology**, not full sensitivity VaR.
- Bonds are slotted into **maturity buckets**, and FICC applies **correlation parameters** across buckets to reflect diversification or concentration.
- Correlations are derived from **fixed income indices** provided by a **designated third‑party vendor**.
- The vendor **does not provide indices** for:
  - Treasury 0–6 months,
  - Treasury 6–12 months,
  - TIPS 0–12 months.
- Where vendor indices are missing, **FICC currently hard‑codes correlations to zero** for any bucket involving those three short-term segments.

This zero‑correlation assumption is conservative about **diversification benefit** but can actually **understate required margin** for directional portfolios that straddle adjacent short-term buckets (e.g., 5‑month and 7‑month Treasuries) because **historically those buckets are highly inter‑correlated**.

Proposed change:

- Amend the **QRM Methodology Document – GSD Initial Market Risk Margin Model** so that:
  - When the designated index vendor lacks data for a bucket, **FICC may use index data from an alternate vendor** to estimate correlations.
  - Remove explicit language that **sets correlations to zero** for Treasury 0–6 months, Treasury 6–12 months, and TIPS 0–12 months.
  - Make a minor **technical correction** to a section reference.

In effect, FICC is turning a previously "dead" part of the correlation matrix (zeros due to missing indices) into a **live, data‑driven correlation structure** using a secondary data source.

---

## 2. Quantitative impact (Impact Study)

FICC ran an **impact study** for **Sept. 1, 2024 – Aug. 31, 2025** on the relevant short‑term buckets using alternate‑vendor index data.

### 2.1 Aggregate GSD VaR Charges

If the new correlations had been in place:

- **Base VaR model (no Margin Proxy deployed):**
  - Average **increase in aggregate VaR Charges:** ≈ **$46 million** (**0.09%**).
  - **Maximum** increase over the period: ≈ **$85 million** (**0.15%**).
  - **Backtesting coverage** would have remained at **99.85%**.

- **If Margin Proxy had been deployed** during the study period:
  - Average **increase in aggregate VaR Charges:** ≈ **$88 million** (**0.16%**).
  - **Maximum** increase: ≈ **$163 million** (**0.38%**).
  - **Backtesting coverage** would have remained at **99.92%**.

So this is a **small percentage increase** in total margin but **tightly focused** on portfolios with exposure to the short‑term buckets that previously had zero correlations.

### 2.2 Member‑level effects

At the **Member Margin Portfolio** level during the impact period:

- Without Margin Proxy:
  - Average **SOD VaR Charge** increase: ≈ **$0.22 million** (**0.09%**).
  - **Largest average % increase** for any portfolio: **14.52%** (≈ **$0.38 million**).
  - **Largest average $ increase** for any portfolio: ≈ **$5.91 million** (≈ **0.79%**).

- With Margin Proxy deployed:
  - Average **SOD VaR Charge** increase: ≈ **$0.42 million** (**0.16%**).
  - **Largest average % increase**: **23.18%** (≈ **$0.59 million**).
  - **Largest average $ increase**: ≈ **$17.35 million** (≈ **0.34%**).

Interpretation:

- **System‑wide impact** is tiny in percentage terms, but individual portfolios that were exploiting (or exposed to) the zero‑correlation assumption in the shortest buckets see **non‑trivial relative increases** in required margin.
- The change is explicitly framed as **margin resilience** for directional short‑term books: portfolios with concentrated exposure around the front of the curve will now be charged in line with the empirically high inter‑correlation of those tenors.

---

## 3. Regulatory framing

FICC grounds the change in:

- **Exchange Act §17A(b)(3)(F)** — safeguarding securities and funds in the clearing agency’s custody or control.
- **Rule 17ad‑22(e)(4)(i)** — maintaining sufficient financial resources to cover credit exposures to each participant with a high degree of confidence.
- **Rule 17ad‑22(e)(6)(i)** — risk‑based margin system producing margin levels commensurate with the risks and attributes of each portfolio and product.

Key arguments:

- Allowing use of **alternate vendor index data** to populate correlations:
  - Improves FICC’s ability to **identify, measure, monitor, and manage** credit exposure from short‑term bonds.
  - Helps ensure margin is **commensurate with risk**, especially where short‑term buckets are empirically highly correlated.
- The small upward drift in aggregate margin is justified as **necessary to safeguard** the fund and non‑defaulting members.
- The technical edit to the QRM Methodology Document is presented as a pure **accuracy/housekeeping** fix that supports correct implementation.

Competition impact:

- FICC concedes the change may **raise Required Fund Deposits and Segregated Customer Margin Requirements** for some participants.
- This could burden firms with **lower operating margins or higher funding costs**, but FICC argues:
  - Any burden is **risk‑aligned** (higher for riskier portfolios).
  - Portfolios with similar risk profiles face similar effects regardless of participant type.
  - Therefore, any competitive impact is **necessary and appropriate** to meet statutory risk‑management obligations.

---

## 4. Structural interpretation

### 4.1 Plugging a data‑driven gap in the curve

Previously, FICC’s bond haircut models **treated segments of the very front end of the curve as uncorrelated** whenever the primary index vendor lacked data. That created a structural blind spot:

- Directional or basis portfolios concentrated in **0–12 month Treasuries/TIPS** could, under certain configurations, face **less margin than warranted** by historical co‑movement.
- This is a classic **"data availability as risk"** problem: a missing vendor index leads to a hard‑coded assumption (zero correlation) that is **known to be wrong** but is used for consistency.

By allowing an **alternate index vendor** to fill in, FICC:

- Restores a **continuous correlation surface** across the short end of the curve.
- Reduces the incentive (or accidental opportunity) to **concentrate risk in the data gap**.
- Moves a previously brittle part of its margin methodology toward a more **robust, multi‑source data architecture**.

### 4.2 Subtle re‑pricing of front‑end funding trades

The affected buckets (0–12 month Treasuries and short‑dated TIPS) are where many **funding, liquidity, and collateral upgrade trades** live.

- Even a 0.1–0.4% increase in aggregate VaR charges, targeted at front‑end exposures, can:
  - Nudge **repo haircuts and financing costs** higher for concentrated short‑term positions.
  - Marginally **discourage crowded directional trades** in the very front of the curve.
- This is especially relevant in stress regimes where **short‑end dislocations** (e.g., bill supply shocks, T‑bill money‑fund dynamics, cash‑management pivots) can transmit quickly through the system.

### 4.3 Quiet coupling of vendor dependency and model governance

The filing is a small but clear trace of how a systemically important CCP:

- Acknowledges its dependence on a **single market‑data vendor** for key model inputs.
- Formalizes a path to **multi‑vendor sourcing** when the primary vendor is incomplete.

This is a structural move toward **resilience against data‑vendor outages or gaps**:

- In steady state: richer coverage of short‑term buckets and better risk alignment.
- In stress: more room to switch or blend data sources without having to re‑write the entire methodology or accept zero‑correlation defaults.

---

## 5. Scoop / coverage check plan

Before promoting this to a bulletin:

- Search for the exact FR title string and key phrases:
  - "Enhance the Correlation Calculation for Bond Haircut Models" + FICC.
  - "SR-FICC-2026-002".
- Scan search‑result HTML for major wires/outlets:
  - `Reuters`, `Bloomberg`, `Associated Press`, `AP News`, `Dow Jones`, `Wall Street Journal`, `WSJ`, `New York Times`, `NYTimes`, `BBC`, `Guardian`.
- If results are limited to **SEC/DTCC primary postings, law‑firm client alerts, niche clearing blogs**, treat as pre‑mainstream and proceed.

If coverage emerges later, this analysis will still serve as a **structural background note** to combine with:

- **Bulletin #11** (DTC liquidity‑linked net debit caps), and
- **Bulletin #12** (FICC–CME Treasury cross‑margining),

into a composite view of how **clearing‑house margining and liquidity constraints** across the DTC/FICC/CME complex are being tuned in 2024–2026.

