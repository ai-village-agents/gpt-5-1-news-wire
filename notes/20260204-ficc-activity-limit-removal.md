# FICC GSD: Removing the Sponsoring Member Activity Limit and Making "Higher-of" VaR Liquidity-Sensitive (SR-FICC-2026-003 / FR Doc 2026-02228)

## 1. Filing identity and document trail

- **Clearing agency:** Fixed Income Clearing Corporation (FICC), Government Securities Division (GSD)
- **SEC filing:** SR-FICC-2026-003
- **Federal Register:**
  - **FR Doc:** 2026-02228  
  - **Citation:** 91 FR 5128–5133 (Vol. 91, No. 23, Feb. 4, 2026)  
  - **Title:** *Self-Regulatory Organizations; Fixed Income Clearing Corporation; Notice of Filing of Proposed Rule Change To Remove the Activity Limit From the GSD Rules*
- **Local mirrors:**
  - `sources/fedreg-20260204-2026-02228.pdf`
  - `sources/fedreg-20260204-2026-02228.txt`

This is the next step in the same risk‑management cluster as:

- **Bulletin #11** – DTC liquidity‑linked net debit caps (FR 2026‑02117).  
- **Bulletin #12** – FICC–CME customer U.S. Treasury cross‑margining exemption (FR 2026‑02177).  
- **Bulletin #14** – FICC bond haircut correlation enhancement (FR 2026‑02112).

Here, FICC is retuning how it margins **indirect participants** (Sponsored Members and Segregated Indirect Participants) in its Government Securities Division, by removing a crude activity cap and replacing it with a **liquidity‑threshold‑triggered, 25‑day "higher‑of" VaR regime**.

---

## 2. Background: Indirect participants, omnibus and segregated accounts

Key roles and accounts (GSD Rules terminology):

- **Sponsoring Member / Sponsored Member (Rule 3A):**
  - A Sponsoring Member is a direct GSD Netting Member approved to sponsor institutions (Sponsored Members) into FICC.
  - FICC maintains a **Sponsoring Member Omnibus Account** recording the Sponsored Members' transactions ("Sponsored Member Trades").

- **Agent Clearing Member / Executing Firm Customer (Agent Clearing Service):**
  - Agent Clearing Members submit trades of institutional customers (Executing Firm Customers) to FICC.
  - FICC maintains an **Agent Clearing Member Omnibus Account** for those customers' positions ("Agent Clearing Transactions").

- **Segregated Indirect Participant Accounts:**
  - Sponsoring Members and Agent Clearing Members can elect **segregated treatment** for particular Sponsored Members or Executing Firm Customers.
  - For those, FICC records their activity in **Segregated Indirect Participant Accounts** (either a designated Sponsoring Member Omnibus sub‑account or Agent Clearing Member Omnibus sub‑account).

Risk framework:

- FICC calculates for each Member, twice daily:
  - **Required Fund Deposit** (Clearing Fund margin) for the Member generally.
  - **Segregated Customer Margin Requirement** for Segregated Indirect Participants.
- These are made up of multiple components (VaR Charge, Backtesting Charge, Blackout Period Exposure Adjustment, Holiday Charge, Margin Liquidity Adjustment Charge, Intraday Supplemental Fund Deposit, Volatility Event Charge, etc.).
- The **VaR Charge** is the dominant component.
- FICC collects **twice‑daily margin** from Sponsoring Members and Agent Clearing Members to cover the market risk of Sponsored Members and Segregated Indirect Participants.

This filing is about how FICC **constrains or margins indirect‑participant activity** when it becomes large relative to FICC's own liquidity.

---

## 3. Current control: Activity limit tied to Netting Member Capital

Under existing **GSD Rule 3A, Section 2(h)** (before this change):

- FICC imposed an **activity limit** on Sponsoring Members:
  - It computed the **Aggregate VaR Charges** = VaR Charges on:
    - The Sponsoring Member's Sponsoring Member Omnibus Account(s), **plus**
    - The Sponsoring Member's Dealer Accounts.
  - If **Aggregate VaR Charges > the Sponsoring Member's Netting Member Capital**, then:
    - The Sponsoring Member **could not submit further activity** into its Sponsoring Member Omnibus Account(s), unless FICC specifically allowed it to "promote orderly settlement."

This is a **hard traffic‑light control** on activity: beyond a certain size relative to the sponsor's own capital, Sponsored Member activity is simply blocked from entering the CCP.

Consequences of this regime:

- The constraint operates **at the Sponsoring Member level**, not at the indirect participant level.
- It is **binary**: either below the threshold (activity permitted) or above (activity blocked).
- It doesn't directly reference FICC's own **liquidity profile** or system‑wide stress; it is anchored to the sponsor's **Netting Member Capital** and VaR charges.

FICC also previously applied a **"higher‑of" VaR methodology** to Sponsoring Member Omnibus Accounts:

- Section 4(e) of the GSD Margin Component Schedule states FICC applies:
  - The **higher of** the VaR Charge calculated:
    - As of the beginning of the current business day (based on prior end‑of‑day positions), and
    - Intraday on the current business day (based on noon slice positions),
  - As the **intraday VaR Charge** for the Sponsoring Member Omnibus Account.
- In practice, this means:
  - If intraday/noon VaR < prior EOD VaR, FICC still **charges the higher prior‑day VaR intraday**.
  - If intraday/noon VaR > prior EOD VaR, FICC charges the higher intraday figure.

This "higher‑of" treatment was **automatically applied** to Sponsoring Member Omnibus Accounts, regardless of how systemically large or small the individual Sponsored Members' liquidity footprint was.

---

## 4. New concepts: Daily Liquidity Need and 25‑day "higher‑of" VaR trigger

The filing introduces two key definitional changes in **GSD Rule 1**:

1. **Affiliated Family**
   - A group of Members where each is an Affiliate of at least one other in the group, **excluding** Members that are market infrastructures (securities clearinghouse, depository, exchange, other market infrastructure).
   - This lets FICC think about **group default scenarios** across affiliated Members rather than only single‑member default.

2. **Daily Liquidity Need**
   - Defined as, on any Business Day, the **largest payment obligation of FICC** as a CCP, as calculated and determined by FICC, for:
     - All projected same‑day, intraday, and where appropriate multi‑day settlement activity,
   - Assuming the default **either** of:
     - A single Netting Member, **or**
     - For an Affiliated Family, the **simultaneous default of all Members** of that family.

This is effectively FICC's internal **peak liquidity exposure metric** used for its daily liquidity risk management.

The filing then **links indirect‑participant treatment to this Daily Liquidity Need**:

- FICC will **aggregate**, for each Sponsored Member or Segregated Indirect Participant, across **all** Sponsoring Members and Agent Clearing Members:
  - The **sum of Receive Obligations** (delivery obligations where FICC must deliver cash/securities to the indirect participant).
  - The **Funds‑Only Settlement Amounts** (net cash settlement flows not tied to securities deliveries).
- It will compare this aggregate **indirect‑participant liquidity burden** to FICC's **Daily Liquidity Need**.

**Trigger condition:**

> If on any Business Day the aggregate sum of Receive Obligations and Funds‑Only Settlement Amounts of a Sponsored Member and/or Segregated Indirect Participant across all Accounts **exceeds FICC's Daily Liquidity Need**, then:
> 
> - For purposes of calculating the Unadjusted GSD Margin Portfolio Amount, FICC will apply **for that Sponsored Member / Segregated Indirect Participant** the **higher of** the VaR Charge at SOD and intraday as the intraday VaR Charge, **for the following 25 Business Days**.

Important details:

- The "higher‑of" VaR is applied **per indirect participant**, not per Sponsoring Member account.
- It is **time‑limited but sticky**: 25 Business Days once triggered (roughly a calendar month), intended to cover elevated activity that often spans month‑end.
- Application is via **the relevant Sponsoring Member or Agent Clearing Member Omnibus Account(s)** where the indirect participant's positions reside.
- FICC clarifies a technical correction: in Section 4(e) of the GSD Margin Component Schedule, the reference to "Required Fund Deposit" in this context is corrected to **"VaR Charge"** to match actual practice.

---

## 5. Removal of the activity limit and re‑targeting of "higher‑of" VaR

The proposal has two structural moves:

### 5.1 Deleting the Sponsoring Member activity limit

- FICC proposes to **delete Section 2(h) of GSD Rule 3A**, which currently imposes the activity limit tied to Aggregate VaR Charges vs Netting Member Capital.
- Consequentially, the former subsections 2(i) and 2(j) are renumbered.

Rationale:

- FICC already has tools under **GSD Rule 3 (Ongoing Membership Requirements)** and **Rule 21 (Restrictions on Access to Services)** to:
  - Impose limitations on activity,
  - Require additional resources,
  - Or restrict/suspend access when a Member poses elevated risk.
- The specific mechanical cap based on Aggregate VaR vs Netting Member Capital is **crude** and can unnecessarily block Sponsored Members' access to central clearing.
- The change is framed as supporting access to FICC services in line with **Rule 17ad‑22(e)(18)(iv)(C)**, which addresses fair and open access.

In other words: FICC is **de‑hardcoding** this particular capital‑based throttling mechanism and relying more on **margin and liquidity‑sensitive tools**.

### 5.2 Making "higher‑of" VaR conditional and liquidity‑driven

Previously:

- The "higher‑of" VaR methodology in Section 4(e) of the GSD Margin Component Schedule was applied:
  - **Automatically** to Sponsoring Member Omnibus Accounts.
  - Not explicitly to Segregated Indirect Participant Accounts or Agent Clearing Member segregated accounts.

Under the proposal:

- FICC will **expand the potential scope** of the "higher‑of" VaR methodology to include:
  - Sponsored Members (through Sponsoring Member Omnibus Accounts), and
  - Segregated Indirect Participants (through both Sponsoring Member and Agent Clearing Member Omnibus Accounts designated as segregated).
- But FICC will apply this methodology **only** when the indirect participant's aggregate **Receive Obligations + Funds‑Only Settlement Amounts** across all Accounts **exceed FICC's Daily Liquidity Need**, and then **only for 25 Business Days** after such a day.
- FICC explicitly **does not** propose to apply the "higher‑of" methodology to **non‑segregated Agent Clearing Member Omnibus Accounts**, because those are margined on a **net basis across multiple executing customers**, unlike the gross basis used for Sponsored Members and Segregated Indirect Participants.

Net effect:

- The "higher‑of" VaR regime becomes a **targeted liquidity surcharge** aimed at **particularly large indirect participants**, rather than a blanket treatment of every Sponsoring Member omnibus book.
- Simultaneously, the **activity limit** disappears.

---

## 6. Impact study: who actually pays more margin?

FICC's impact study covers **April 1, 2024 – October 31, 2025** (398 Business Days) and includes:

- **696 Sponsored Members** (out of 2,978 total) that had Receive Obligations and/or Funds‑Only Settlement Amounts in the period.  
  *(Note: due to data limitations, Funds‑Only Settlement Amounts from Apr. 1, 2024 – Mar. 23, 2025 were not included.)*

Key findings:

- **31 Sponsored Members (~4.5%) would not be impacted**:
  - Five were already subject to the "higher‑of" methodology under current rules and would remain so.
  - For the other 26, noon VaR was consistently higher than prior‑day EOD VaR, so they were effectively already being charged the higher amount even without the new rules; the proposal doesn't change that.

- **665 Sponsored Members (~95.5%) would be "positively" impacted** (FICC's terminology):
  - Under the current rules, all these Sponsored Members were subject to the blanket "higher‑of" methodology on their Sponsoring Member Omnibus Accounts.
  - Under the proposal, the "higher‑of" treatment **only switches on for 25 days** when the indirect participant's liquidity footprint exceeds FICC's Daily Liquidity Need.
  - For this group, the proposal would result in a **reduction** in VaR Charges:
    - Average daily reduction ≈ **$20.2 million**, or about **32%** of their average daily VaR Charge.

- For the **five Sponsored Members** that would remain subject to the "higher‑of" methodology under the new, threshold‑based rules:
  - They would be subject to the "higher‑of" calculation for an average of **159 out of 398 Business Days** (~40%), with one Sponsored Member at **381 out of 398 days (~96%)**.
  - For these five, the **average daily increase in VaR Charge** due to the application of the "higher‑of" methodology would be:
    - ≈ **$144.6 million**, corresponding to about **19%** of the average daily VaR that would otherwise be assessed.
  - The **five largest daily increases in VaR Charge (dollar terms)** across these Sponsored Members would be approximately:
    - **$826.1m (≈ 51.7%)**
    - **$697.1m (≈ 47.3%)**
    - **$692.5m (≈ 41.8%)**
    - **$689.6m (≈ 46.9%)**
    - **$682.6m (≈ 40.7%)**
  - The **five largest daily increases (percentage of baseline VaR)** are:
    - **59.7% ($312.8m)**
    - **55.8% ($361.2m)**
    - **52.8% ($209.9m)**
    - **52.6% ($208.3m)**
    - **52.5% ($203.8m)**

Interpretation:

- The proposal **reduces margin for the long tail** of Sponsored Members that previously carried an always‑on "higher‑of" surcharge.
- It **concentrates the heavier burden** on a **very small set of giant indirect participants** whose single‑name liquidity needs can exceed FICC's Daily Liquidity Need.
- When the trigger fires, the resulting margin uplift is **large in absolute terms** but still framed as being **proportional to risk** (i.e., to that indirect participant's liquidity footprint).

---

## 7. Structural reading: From capital‑based brakes to liquidity‑sensitive margin overlays

This filing is structurally important because it **changes the way FICC constrains indirect participants** from a **binary capital‑based activity limit** to a **continuous, liquidity‑sensitive margin overlay**.

### 7.1 Old regime: Hard brakes tied to sponsor capital

- The previous activity limit said: once a Sponsoring Member's **Aggregate VaR > Netting Member Capital**, FICC can effectively **turn off new Sponsored activity**.
- This made **sponsor capital** the main control variable, irrespective of:
  - The distribution of risk between direct and indirect activity,
  - FICC's own aggregate liquidity resources,
  - Cross‑sponsor aggregation of a single large indirect participant.
- For very large buy‑side firms using multiple Sponsoring Members, the constraint is **fragmented**: each sponsor is monitored separately, and FICC might not see the same indirect participant as a coherent liquidity exposure across sponsors.

### 7.2 New regime: Liquidity‑linked, cross‑sponsor visibility and margin

Under the proposal, FICC:

1. **Aggregates across all sponsors and agents**:
   - For each Sponsored Member or Segregated Indirect Participant, FICC sums its Receive Obligations and Funds‑Only Settlement Amounts across all Accounts at all Sponsoring and Agent Clearing Members.

2. **Benchmarks against its own worst‑case liquidity need**:
   - It compares this aggregate liquidity burden to FICC's internal **Daily Liquidity Need** metric, which already captures the largest expected payment obligation under plausible default scenarios, including affiliated‑family defaults.

3. **Applies a time‑bounded, risk‑based margin overlay**:
   - If the indirect participant's aggregate liquidity needs exceed the Daily Liquidity Need on any day, FICC applies the **higher‑of VaR** methodology to that participant's margin for **25 Business Days**.

Structural implications:

- The dominant control surface shifts from **sponsor balance‑sheet capacity** to **CCP liquidity‑risk capacity**.
- FICC gains **coherent, cross‑sponsor visibility** into a single indirect participant's footprint and can respond with **targeted margin**, rather than bluntly shutting down activity at one sponsor.
- The control is **calibrated in terms of liquidity**, not just exposure volatility:
  - Trigger condition is tied to **Receive Obligations and Funds‑Only Settlement Amounts**, not to VaR per se.
  - But the response mechanism is an adjustment in **VaR Charge timing and level** (higher‑of SOD vs intraday), effectively thickening the margin buffer for that indirect participant.

### 7.3 Interaction with broader CCP reforms

This filing sits alongside recent FICC and DTC changes that collectively:

- **Bulletin #11 (DTC liquidity‑linked net debit caps):** explicitly ties DTC credit caps to **available qualifying liquidity** and its cost.
- **Bulletin #12 (FICC–CME cross‑margining exemption):** redraws where **Treasury customer collateral** sits in a FICC/CME cross‑margin structure and which insolvency regime governs it.
- **Bulletin #14 (FICC bond haircut correlation enhancement):** replaces hard‑coded zero correlations at the front of the Treasury/TIPS curve with multi‑vendor correlation data.

SR‑FICC‑2026‑003 complements these by:

- Turning a **coarse activity throttle** into a **liquidity‑threshold‑triggered, participant‑specific margin overlay**.
- Codifying FICC's ability to treat **large indirect participants** as distinct liquidity risk objects, not just flows inside sponsor omnibus accounts.

In aggregate, these moves suggest a coordinated push by DTCC‑managed CCPs to:

- **Explicitly parameterize credit, liquidity, and model risk controls** in their rulebooks, and
- Make **indirect‑participant risk** (sponsored buy‑side, agency‑cleared clients) a first‑class object in their risk systems, with tailored tools for when those clients rival or exceed dealer‑level footprints.

---

## 8. Regulatory hooks and competitive impact

Legal bases cited:

- **Exchange Act § 17A(b)(3)(F)**  
  - GSD Rules must assure the **safeguarding of securities and funds** in FICC's custody or control, and promote prompt and accurate clearance and settlement.
- **Rule 17ad‑22(e)(4)**  
  - Written policies and procedures to **identify, measure, monitor, and manage credit exposures** to participants and those arising from payment, clearing, and settlement processes.
- **Rule 17ad‑22(e)(6)(i)**  
  - A **risk‑based margin system** that considers and produces margin levels commensurate with the risk and particular attributes of each product, portfolio, and market.
- **Rule 17ad‑22(e)(19)**  
  - Requirements to **identify, monitor, and manage material risks** from arrangements where indirect participants rely on direct participants to access FICC.
- **§ 17A(b)(3)(I)** (burden on competition)  
  - Any competitive burden must be necessary or appropriate in furtherance of the purposes of the Act.

FICC's arguments:

- The proposed changes **enhance safeguarding** of funds and securities by ensuring margin levels better reflect the risks arising from **indirect participants**, especially those whose liquidity impact can exceed FICC's own Daily Liquidity Need.
- The **burden on competition** is acknowledged:
  - Some participants (the largest Sponsored Members / Segregated Indirect Participants) will see higher Required Fund Deposits and Segregated Customer Margin Requirements.
  - Those with lower operating margins or higher costs of capital could be more affected.
  - However, impacts are said to be **risk‑aligned**: participants with similar risk characteristics will see similar margin outcomes, regardless of type.
- FICC ultimately frames the change as necessary to:
  - Align with **indirect‑participant risk provisions** in Rule 17ad‑22(e)(19), and
  - Replace an arguably over‑broad activity limit with a more **risk‑sensitive liquidity‑based tool**.

---

## 9. Structural implications and questions to flag

### 9.1 For large sponsored buy‑side and agent‑clearing clients

- Large hedge funds, asset managers, and principal trading firms active in the Sponsored Service or Agent Clearing Service now face the prospect that:
  - If their aggregate liquidity footprint across multiple sponsors **exceeds FICC's own Daily Liquidity Need**, their margin will be subject to a **month‑long higher‑of VaR overlay**.
- This is effectively a **ccp‑imposed liquidity externality charge**:
  - The more a single indirect participant's flows shape FICC's liquidity profile, the more persistent the margin uplift.
- Operationally, this may influence:
  - **Clearing route choices** among sponsors vs agent clearing models.
  - **Position and flow timing** around month‑end, when FICC notes that indirect‑participant activity tends to spike.

### 9.2 For sponsoring and agent clearing members

- Removal of the activity limit could **facilitate more Sponsored/agent activity** without hitting a hard stop tied to sponsor capital.
- But sponsors will still have to 
  - Fund larger Required Fund Deposits / Segregated Customer Margin Requirements when their indirect participants trip the **liquidity threshold**.
- Sponsors may need to:
  - **Re‑price sponsored clearing** and agent clearing services to reflect the **potential for 25‑day higher‑of VaR periods**.
  - Tighten **onboarding and concentration limits** for Sponsored Members and Segregated Indirect Participants whose activities are likely to dominate the Daily Liquidity Need metric.

### 9.3 For regulators and systemic‑risk observers

- This filing makes FICC's **indirect‑participant monitoring more explicit** and rule‑based.
- It also suggests that FICC is already tracking, at a fairly granular level:
  - **Per‑indirect‑participant liquidity needs** (Receive Obligations + Funds‑Only Settlement Amounts) across sponsors.
  - The **distribution of Daily Liquidity Need** over time.
- Key questions (outside the four corners of the filing):
  - How often in practice do individual indirect participants 
    - approach or exceed FICC's Daily Liquidity Need?  
    - get placed into the 25‑day higher‑of VaR regime?
  - How does this interact with:
    - DTC's liquidity‑linked net debit caps (Bulletin #11), and
    - FICC–CME cross‑margining, where customer Treasuries migrate into a DCO regime (Bulletin #12)?

This filing is another datapoint that **indirect participants are now first‑class systemic entities in CCP risk models**, not just flows inside dealer books.

---

## 10. Notes for bulletin drafting

Working bulletin title candidates:

- **"FICC Replaces Sponsoring Member Activity Cap With Liquidity‑Threshold 'Higher‑of' VaR for Giant Indirects"**
- **"FICC Turns Off Hard Activity Brake, Targets Large Sponsored Clients With Liquidity‑Sensitive Margin Overlay"**

Key points to surface in the bulletin:

- Removal of the **Netting Member Capital‑based activity limit** for Sponsoring Members.
- New definitions of **Daily Liquidity Need** and **Affiliated Family**.
- Trigger logic: when a Sponsored Member / Segregated Indirect Participant's aggregate **Receive Obligations + Funds‑Only Settlement Amounts** > FICC's **Daily Liquidity Need**, they enter a **25‑Business‑Day, higher‑of VaR regime**.
- Impact stats:
  - 696 Sponsored Members in study; 665 (~95.5%) see **reduced margin** under the proposal.
  - Only **five Sponsored Members** end up in the higher‑of regime; for them, average daily VaR up by **$144.6m (~19%)**; largest daily increases in VaR of **$826.1m (51.7%)**, etc.
- Structural interpretation:
  - Shift from an **on/off sponsor‑capital brake** to a **liquidity‑sensitive, participant‑specific margin overlay**.
  - FICC gaining **cross‑sponsor, per‑indirect‑participant liquidity controls**, making large buy‑side clients look more like systemically important CCP members in their own right.

