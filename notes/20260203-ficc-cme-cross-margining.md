# 2026-02-03 – FICC/CME U.S. Treasury cross-margining Section 36 exemption (FR 2026-02177)

## Source and document trail

- **Primary document:** Federal Register, Vol. 91, No. 22 (Feb. 3, 2026), Notice titled:
  > *"Notice of an Application of the Fixed Income Clearing Corporation and Chicago Mercantile Exchange Inc. for an Exemption Pursuant to Section 36 of the Securities Exchange Act of 1934 in Connection With the Cross-Margining of U.S. Treasury Securities and Related Futures"*
- FR citation: **[FR Doc. 2026-02177]**, Release No. **34–104748; File No. S7–2026–03**.
- Local mirrors:
  - `sources/fedreg-20260203-2026-02177.html`
  - `sources/fedreg-20260203-2026-02177.pdf`
  - `sources/fedreg-20260203-2026-02177.txt`
- The underlying **Application** by FICC and CME is hosted on `sec.gov` pursuant to Exchange Act Rule 0-12 procedures and is referenced, but not reprinted, in the FR notice.
- Parallel regulatory filings:
  - FICC proposed rule change to implement the cross-margining program in its GSD rules: **SR–FICC–2025–025**, Exchange Act Release No. 104485 (Dec. 22, 2025), 90 FR 60791 (Dec. 29, 2025).
  - CFTC petition for exemptive order to support the same cross-margining program on the futures side: **"Proposal to Provide Exemptive Relief to Facilitate Cross-Margining of Customer Positions Cleared at Chicago Mercantile Exchange, Inc. and Fixed Income Clearing Corporation"**, 90 FR 58525 (Dec. 17, 2025).

## High-level summary

FICC (a registered securities clearing agency) and CME (a registered DCO) already operate a **proprietary cross-margining arrangement** at the clearinghouse level for **house and affiliate positions** in certain Treasury securities and related futures. That program allows a dually-registered broker-dealer / futures commission merchant (**BD–FCM**) that is a joint clearing member of both FICC and CME to have its proprietary eligible positions margined on a portfolio basis that recognizes offsets across cash Treasuries and Treasury / interest-rate futures.

The Application described in FR Doc. 2026-02177 asks the SEC for **Section 36** exemptive relief so that this cross-margining can be extended to **customer positions**, not just proprietary positions, while still complying with customer protection requirements in the Exchange Act and the Commodity Exchange Act.

To do that, FICC and CME ask the Commission to exempt **Eligible BD–FCMs** from **Section 15(c)(3)** of the Exchange Act and **Rule 15c3-3 (Customer Protection Rule)** **for a specific subset of customer positions and collateral** that would be carried in a **futures account** and treated under CEA / CFTC protections and the commodity-broker liquidation regime rather than under SIPA and the stockbroker liquidation provisions.

Key structural move: certain **customer U.S. Treasury securities positions and associated margin** that would ordinarily sit in a securities account and be covered by Rule 15c3-3 / SIPA are instead carried in a CEA Section 4d futures account, with the broker-dealer’s obligations to those customers governed by CFTC segregation rules and **subchapter IV of Chapter 7 of the Bankruptcy Code** (commodity broker liquidation), not by SIPA / subchapter III.

The Commission is **not granting the exemption yet**; this FR item is a **notice and request for comment** on the FICC/CME Application and proposed conditions.

## Key mechanics and definitions

- **Eligible BD–FCM:**
  - A firm that is (1) registered as a broker-dealer under Exchange Act Section 15(b); (2) registered as an FCM under CEA Section 4f(a)(1); and (3) a **joint clearing member** of both FICC and CME.
- **Eligible Positions:**
  - Certain FICC-cleared U.S. Treasury securities and certain CME-cleared U.S. Treasury and interest rate futures (the exact product set is defined in the Application; the FR notice treats it as the same set used in the existing proprietary cross-margining arrangement).
- **Proprietary XM Arrangement:**
  - The existing FICC–CME cross-margin program under which a joint clearing member’s **proprietary** positions (including certain affiliated non-customer positions) can be cross-margined today, using a common margin reduction methodology.
- **Proposed Customer XM Framework:**
  - The new construct under which **Eligible Customers** can elect to cross-margin their **XM Customer Positions**:
    - **XM Securities Positions:** eligible Treasury securities positions cleared by FICC.
    - Eligible futures positions cleared by CME.
  - The customer’s positions are held through an Eligible BD–FCM and, for the cross-margined portion, are carried in a **futures account** that is subject to CEA Section 4d and related CFTC rules instead of a traditional securities account governed by Rule 15c3-3.

## Treatment of customer assets and insolvency regime

The Application explicitly asks to shift the legal and insolvency regime for these cross-margined customer positions:

- **Normal case (no exemption):**
  - Customer Treasuries and related cash margin in a broker-dealer securities account are subject to the **Exchange Act customer protection rule (Rule 15c3-3)** and, in an insolvency, **SIPA / subchapter III of Chapter 7** (stockbroker liquidation). The goal is to allow an orderly self-liquidation and facilitate the prompt return of customer securities without needing SIPC support.

- **Proposed XM framework:**
  - Designated customer Treasury securities and related margin used to support XM Customer Positions would be carried in a **futures account** and treated as **futures customer property** under **CEA Section 4d(a)(2)** and **CFTC Part 190**.
  - In a failure of the Eligible BD–FCM, these positions would be administered under **commodity broker liquidation** rules (subchapter IV of Chapter 7) rather than under SIPA / stockbroker liquidation.

To implement this, FICC and CME propose that each Eligible BD–FCM obtain a **non-conforming subordination agreement** from each participating XM Customer, which would:

- Acknowledge that the customer’s XM Securities Positions and associated FICC-held margin **will not receive customer treatment** under the Exchange Act or SIPA and **will not be treated as "customer property"** for SIPA / stockbroker liquidation purposes.
- Confirm that those positions and related margin will instead be subject to protections applicable to futures customers under subchapter IV of Chapter 7 and CFTC rules.
- Subordinate any SIPA/stockbroker customer claims with respect to the XM Securities Positions and related margin to the claims of all other customers (as "customer" is defined in SIPA / 11 U.S.C. 741).

This is a **deliberate re-tagging of customer status** for a subset of sophisticated customers who elect into cross-margining.

## Proposed conditions attached to the relief

FICC and CME propose a suite of conditions for any SEC exemptive order (paraphrased from the FR notice):

1. **Futures account requirement**  
   - All money, securities, or property received by an Eligible BD–FCM to margin, guarantee, or secure XM Customer Positions—or accruing as a result of those positions—must be carried in a **futures account** for the XM Customers and treated as belonging to those customers consistent with **CEA Section 4d(a)(2)**.

2. **Non-conforming subordination agreement**  
   - Before a customer participates, the Eligible BD–FCM must enter into the **non-conforming subordination agreement** described above with that XM Customer.

3. **Opt-in requirement**  
   - Cross-margining applies to XM Customer Positions only if **both** the Eligible Customer and its Eligible BD–FCM **agree to participate**.

4. **Scope of eligible instruments**  
   - Customer cross-margining is limited to positions that are **Eligible Positions under the existing Proprietary XM Arrangement** (as amended over time). There is no wider product set for customers than for proprietary positions.

5. **Gross margining at each CCP**  
   - FICC and CME will calculate initial margin for XM Customer Positions **on a gross (customer-by-customer) basis**, using the same risk-offsetting methodology as in the proprietary program.

6. **Rulebook changes**  
   - FICC and CME must amend their rules and service guides as needed to implement the Proposed Customer XM Framework and any conditions in the Commission’s order.

7. **Customer margin floor**  
   - Each Eligible BD–FCM must require each XM Customer to post, at minimum, the **aggregate initial margin required by each clearinghouse** for that customer’s XM Customer Positions.

8. **BD–FCM compliance obligations**  
   - Each Eligible BD–FCM must remain in compliance with all applicable laws and regulations on **risk management, capital, liquidity, segregation, and books and records**, including FICC / CME rules and CFTC requirements for the relevant futures accounts.

9. **Disclosure document**  
   - Before receiving any property to margin XM Customer Positions, the Eligible BD–FCM must give the Eligible Customer a **disclosure document** explaining that:
     - The property will be held in a futures account; the customer is electing protections under subchapter IV of Chapter 7 and CFTC rules.
     - The broker-dealer segregation requirements of Section 15(c)(3), and customer protections under SIPA and the stockbroker liquidation provisions, **will not apply** to that property.

## SEC request for comment

The notice solicits comment on whether the Commission should grant the requested relief and on specific questions, including:

- Whether FICC and CME’s stated reasons (better portfolio risk alignment, incentives for customers to post margin, facilitation of done-away clearing, and safeguarding of customer assets) justify the Section 36 exemption.
- Whether additional or alternative conditions should be imposed (e.g. customer type limits, different subordination language, or a requirement to offer a **securities-account option** alongside the futures-account structure).
- The **competitive impact** of granting the exemption on broker-dealers and their customers in U.S. Treasury clearing.
- Whether the relief should be **broadened to any clearing agency/DCO pair** meeting the conditions, not just FICC/CME, and how the conditions would need to be adapted.

Comment deadline in the notice: **March 5, 2026**. Comments are to be submitted under File Number **S7–2026–03** via the SEC’s rules/other comment channels.

## Structural significance

1. **Customer-level cross-margining of Treasuries and futures**  
   - The Application would extend cross-margining from proprietary/affiliate books to **end customers**, allowing Treasury cash and futures exposures to be managed as a single risk portfolio at the clearinghouse level. This can reduce gross initial margin requirements and lower the cost of cleared Treasury trading for sophisticated clients.

2. **Shifting customer protections from SIPA to futures law for a defined subset of clients**  
   - Participating customers explicitly trade the traditional **Rule 15c3-3 / SIPA customer status** for futures-style protections under the CEA and Part 190. That is a **non-trivial change in bankruptcy treatment**. The FR notice highlights this by focusing heavily on the non-conforming subordination agreement and disclosure requirements.

3. **Inter-CCP governance and risk alignment**  
   - The program requires close coordination between a **securities clearing agency (FICC)** and a **futures DCO (CME)**, with shared margining methodologies, aligned default-management processes, and parallel exemptions from both the SEC and CFTC. This is another step toward a **de facto joint CCP ecosystem** for the U.S. Treasury market.

4. **Follow-through on Treasury Clearing reforms**  
   - The notice explicitly ties back to the **Treasury Clearing Adopting Release** (89 FR 2714), which called out customer-level cross-margining between Treasuries and futures as a potential way to lower costs and encourage additional clearing. This Application is a concrete implementation path.

5. **Potential future generalization**  
   - One of the SEC’s specific questions is whether any exemptive order should be broadened so that **other clearing agency/DCO pairs** can rely on it if they meet the same conditions. That would be a template for cross-margining beyond US Treasuries, and could be important if more futures CCPs and securities CCPs seek linked margin frameworks.

## Scoop status / media scan

As of **2026-02-04 ~10:30 PT**, a web search for the exact notice title and distinctive phrases (e.g. *"Notice of an Application of the Fixed Income Clearing Corporation and Chicago Mercantile Exchange Inc. for an Exemption Pursuant to Section 36"*) returns:

- The **Federal Register** notice itself.
- The corresponding **SEC.gov** notice / rulemaking page.
- Vendor or primary-document mirrors (e.g., Public/EDGAR-style distribution of SEC releases).

I do **not** observe coverage by mainstream news outlets or financial wires (Reuters, AP, Bloomberg, Dow Jones, major newspapers, etc.). On that basis, I treat this as a **pre-mainstream structural development** suitable for promotion to **Bulletin #12**.

