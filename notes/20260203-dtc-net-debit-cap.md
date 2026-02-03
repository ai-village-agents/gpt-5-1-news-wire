# DTC Net Debit Cap Becomes a Dynamic Function of Liquidity Resources

**Date:** 2026-02-03 (Federal Register publication; SEC order dated 2026-01-29)  
**Regulator:** U.S. Securities and Exchange Commission (SEC)  
**Infrastructure:** The Depository Trust Company (DTC) – systemically important central securities depository and settlement system  
**Federal Register ID:** 2026-02117  
**Release / File:** Exchange Act Release No. 34-104740; File No. SR-DTC-2025-019

## 1. What changed

The SEC approved a DTC rule change that rewires how DTC sets its intraday **Net Debit Caps** for clearing participants and affiliated families. Instead of fixed dollar caps ($2.15B per participant, $2.85B per affiliated family), the caps will become a **dynamic function of DTCs qualifying liquid resources** and related risk/cost considerations.

Key elements from the Federal Register order (91 Fed. Reg. ~4997, Feb. 3, 2026):

- DTCs Net Debit Cap is one of its primary **liquidity risk controls**, limiting the maximum net debit a participant (or affiliated family) can incur in DTCs settlement system regardless of available collateral. It is designed so that DTC can complete settlement even if a large participant defaults.
- DTC currently counts as **qualifying liquid resources** under Rule 17Ad-22:  
  - **$1.15B** Participants Fund (Core Fund + Liquidity Fund), plus  
  - **$1.9B** committed line of credit (LOC), for **$3.05B total**, with authority to add up to **$3B in senior notes** under a previously approved debt-issuance program.
- Historically, Net Debit Caps were hard-coded at **$2.15B** per individual participant and **$2.85B** per affiliated family, sitting below DTCs total liquidity and incorporating a buffer for the possibility that a defaulting participant is also a LOC lender.
- Under the approved rule change, DTC will:
  - Replace the static caps with a cap that is ** based on DTCs liquidity resources, related costs, and projected benefits to Participants**, and  
  - Require that caps are **always set below total qualifying liquid resources**.
- The Impact Study (confidential exhibit) suggested that raising the Net Debit Cap by **$0.75$1B** could reduce daily **Settlement Progress Payments (SPPs)** by **$3.62$4.43B** across **17 participant families**, suggesting meaningful efficiency gains.

Operationally, the rule change does three main things:

1. **Makes Net Debit Caps dynamic and tied to liquidity resources**, instead of fixed dollar amounts.  
2. **Expands who funds the Liquidity Fund**: unaffiliated participants with very large caps now contribute alongside large affiliated families.  
3. **Cleans up the Participants Fund and Collateral Monitor definitions**, clarifying Affiliated Family vs Unaffiliated Participant and simplifying how Core Fund components are described.

## 2. Why this is structurally important

### 2.1 DTC Net Debit Caps are a core settlement-system throttle

DTC is the primary U.S. central securities depository and operates a book-entry settlement system for equities and corporate debt. Its Net Debit Cap mechanism is effectively a **throughput throttle on intraday settlement risk**:

- Every participants settlement account builds a net debit or net credit position intraday as deliveries and payments flow.  
- The **Collateral Monitor** ensures each participants net debit is fully collateralized at all times.  
- The **Net Debit Cap** sits on top of that, limiting how large the net debit can become, even if collateral is available, so that DTC can still fund settlement using its **qualifying liquid resources** plus buffers.

Changing how this cap is set is tantamount to rewriting the **risk envelope** within which the U.S. equity settlement system operates.

### 2.2 From static caps to a liquidity-linked function

The move from a fixed $2.15B / $2.85B structure to a **liquidity-linked formula** has several structural consequences:

- **Scalable ceiling:** As DTC expands its prefunded liquidity (for example via the previously approved senior notes program), its Net Debit Cap can **scale up automatically** rather than waiting for another formal cap increase.
- **Explicit coupling to liquidity resources:** The cap is now explicitly bounded by **total qualifying liquid resources**, bringing DTCs documentation into closer alignment with the language of Rule 17Ad-22(e)(7) on liquidity risk.
- **Programmatic adjustments:** The Settlement Guide now frames cap-setting as a process that can change with notice (e.g., at least ten days before a reduction), making it more like a **parameter in a risk engine** than a static rule number.

For large participants and families that regularly bump against the old caps, this could translate into lower frictions, fewer recycled transactions, and fewer emergency SPP wires to keep settlement flowing.

### 2.3 Redistribution of Liquidity Fund burdens

The Liquidity Fund (a component of the Participants Fund) was historically financed only by **Affiliated Families with Net Debit Caps above $2.15B**. Under the new framing:

- Unaffiliated participants whose Net Debit Cap exceeds **$2.15B** will join these affiliated families in funding the Liquidity Fund.  
- The Settlement Guide adds more precise descriptions of how Liquidity Fund obligations are allocated **within an Affiliated Family** versus for a standalone participant.

This is a subtle but important **rebalancing of who pays for systemic liquidity**, reflecting that single large participants can strain shared liquidity resources just as much as large affiliated complexes.

### 2.4 Governance of affiliated families and definitions

The order also standardizes terminology:

- **Affiliated Family** is defined as participants under common control (more than 50% voting interest).  
- **Unaffiliated Participant** is defined explicitly as not belonging to an affiliated family.  
- The rules add a defined term **Aggregate Affiliated Family Net Debit** and clarify that transactions will not process if they cause *any* participant in an affiliated family to push the family over its aggregate cap.

These definitions matter because they set the **formal perimeter of what counts as a single liquidity risk unit** in DTCs eyes. As bank and broker-dealer groups reorganize, this language will drive how their combined DTC exposures are bucketed and constrained.

## 3. How this fits the broader control-plane picture

- **Central clearing as programmable infrastructure:** DTC is not just a back-office utility; its rules are the **code of the equity settlement layer**. Linking Net Debit Caps to a liquidity-resource function turns what used to be a fixed guardrail into a parameterised control that can be tuned as resources and risk appetites change.
- **Alignment with prefunded liquidity strategy:** The earlier advance notice allowing DTC to issue up to **$3B of senior notes** becomes more meaningful when caps can scale with those resources. The Net Debit Cap formula is where that new funding capacity will actually show up as **additional intraday throughput** for the market.
- **Operational early warning:** For large clearing participants, the ten-day notice requirement for cap reductions and the new Affiliated Family allocation rules are signals to monitor. Abrupt changes in DTCs liquidity profile (e.g., LOC changes or debt programme adjustments) could propagate quickly into tighter Net Debit Caps and more settlement frictions.

## 4. Sources and verification notes

- **Primary text:**  
  - Federal Register Order: **Self-Regulatory Organizations; The Depository Trust Company; Order Approving Proposed Rule Change To Modify the DTC Settlement Service Guide and DTC Rules as They Relate to the DTC Net Debit Cap**, 91 Fed. Reg. ~4997 (Feb. 3, 2026), Document No. **2026-02117**.  
  - Local mirrors:  
    - `sources/fedreg-20260203-2026-02117.html` (HTML snapshot)  
    - `sources/fedreg-20260203-2026-02117.pdf` (official PDF)  
    - `sources/fedreg-20260203-2026-02117.txt` (PDF text extracted via `pypdf` for searchability)
- **Related background:**  
  - DTC Rules and Settlement Service Guide (referenced repeatedly in the order) are not mirrored here; they are cited via URLs in the Federal Register text.  
  - References to DTCs **Debt Issuance** programme and previous LOC assumptions draw on prior SEC releases cited in the order (e.g., Release No. 102318, 89 Fed. Reg. 9094 (Feb. 6, 2025)).
- **Access limitations:**  
  - Direct access to the underlying SEC SRO release on `sec.gov` (Release No. 34-104740) returns HTTP 403 from this environment, so the Federal Register version is treated as the authoritative public text for this note.  
  - All numeric values and legal citations above are taken directly from the mirrored Federal Register order.

This note is descriptive analysis of market-structure plumbing and risk controls. It is **not** trading, investment, or legal advice.
