# Fortinet FortiCloud SSO authentication bypass (CVE-2026-24858 / FG-IR-26-060)

- **Internal slug:** `20260203-fortinet-forticloud-sso`
- **Draft start (UTC):** 2026-02-03T18:15Z
- **Target publish window (UTC):** 2026-02-03T18:45Z

## 1. Summary (26 sentences)

Fortinet has disclosed a critical authentication bypass in its FortiCloud single sign-on (SSO) integration that affects multiple on-premises products, including FortiOS, FortiManager, FortiAnalyzer, FortiProxy, and FortiWeb. Tracked as CVE-2026-24858 (FG-IR-26-060) and rated CVSS 3.1 base score 9.4 (CRITICAL), the bug allows an attacker with a FortiCloud account and at least one registered device to log into other customers' devices if those devices have FortiCloud SSO enabled. Fortinet reports that two malicious FortiCloud accounts abused this flaw in the wild, and in response the company temporarily disabled FortiCloud SSO service-wide on January 26, 2026 before re-enabling it only for non-vulnerable firmware versions.

## 2. Evidence & primary sources

- [x] CISA Known Exploited Vulnerabilities (KEV) entry &mdash; CVE-2026-24858, Fortinet Multiple Products Authentication Bypass Using an Alternate Path or Channel Vulnerability &mdash; https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- [x] Fortinet PSIRT advisory FG-IR-26-060 (overview) &mdash; Fortinet Multiple Products FortiCloud SSO Authentication Bypass &mdash; https://www.fortiguard.com/psirt/FG-IR-26-060
- [x] Fortinet CSAF JSON for FG-IR-26-060 (per-product CVSS, affected/fixed versions) &mdash; https://filestore.fortinet.com/fortiguard/psirt/csaf_administrative-forticloud-sso-authentication-bypass_fg-ir-26-060.json
- [x] Fortinet PSIRT blog with exploitation and mitigation timeline &mdash; "Analysis of SSO abuse on FortiOS" &mdash; https://www.fortinet.com/blog/psirt-blogs/analysis-of-sso-abuse-on-fortios
- [x] NVD entry for CVE-2026-24858 (metadata cross-check) &mdash; https://nvd.nist.gov/vuln/detail/CVE-2026-24858

## 3. Pre-mainstream check

- [x] CISA KEV lists CVE-2026-24858 as added 2026-01-27 with required action due by 2026-01-30 and references Fortinet's PSIRT advisory, PSIRT blog, and NVD as primary sources.
- [x] Directly consulted Fortinet's PSIRT advisory, CSAF JSON, and PSIRT blog, which provide technical and timeline details, but are vendor-hosted primary documents rather than independent coverage.
- [x] Environment limitations: My browser access to broad search results (for example, Google web/News queries like "Administrative FortiCloud SSO authentication bypass" or "Fortinet disabled FortiCloud SSO on January 26") is gated behind a JavaScript/consent interstitial that I cannot reliably bypass. I therefore cannot definitively state that no wire-service or major-outlet coverage exists.
- [x] Within those constraints, I have not yet seen this treated as a standalone, cross-tenant SSO failure story by major general-news wires (Reuters, AP, Bloomberg, etc.) or large security trade press; most surfaced material is vendor output or database entries.

## 4. Verification checklist

- [x] CVE and identifiers: CVE-2026-24858, FG-IR-26-060, CWE-288 all match across CISA KEV, Fortinet CSAF, and NVD.
- [x] Severity: CSAF lists CVSS v3.1 baseScore 9.4, baseSeverity CRITICAL, vector `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:H/RL:O/RC:C` for affected products (e.g., FortiOS, FortiManager, FortiAnalyzer).
- [x] Affected products and ranges: CSAF marks FortiOS, FortiManager, FortiAnalyzer (and other products such as FortiProxy/FortiWeb) with vulnerable 7.x ranges and non-affected versions including all 6.4 releases and specific 7.x fixed builds (for example, FortiOS 7.6.6, 7.4.11, upcoming 7.2.13, upcoming 7.0.19).
- [x] Exploitation and timeline: Fortinet's blog states that two malicious FortiCloud accounts abused the flaw, that those accounts were locked on 2026-01-22, that Fortinet disabled FortiCloud SSO on the service side on 2026-01-26, and that SSO was re-enabled on 2026-01-27 only for devices running non-vulnerable versions.
- [x] Scope of impact: CISA KEV and the Fortinet blog both frame this as an authentication bypass using an alternate path/channel (CWE-288) that can let an attacker with a FortiCloud account and a registered device log into other Fortinet devices registered to different accounts when FortiCloud SSO is enabled.
- [x] Non-impacted services: Fortinet's blog clarifies that FortiManager Cloud, FortiAnalyzer Cloud, and FortiGate Cloud were not impacted, and that deployments using a custom identity provider (including FortiAuthenticator) are not affected.

## 5. Risk & harm analysis (brief)

- [x] This bulletin focuses on widely disclosed technical and operational details from CISA and Fortinet, without adding exploit code, network indicators, or customer-identifying data.
- [x] The vulnerability is already listed in CISA KEV with a remediation deadline and vendor guidance, and Fortinet has already taken emergency actions (global SSO disablement and version-gated re-enablement) to constrain further abuse.
- [x] The main incremental value is explaining the cross-tenant nature of the failure, the unusual decision to shut down FortiCloud SSO globally, and the operational implications for organizations that rely on Fortinet appliances for perimeter/security functions.

Short notes:

> Given that this is an already-exploited vulnerability in network and security infrastructure products with a CISA KEV mandate, explaining the issue using only vendor and government documentation is low-risk and may help defenders understand why FortiCloud SSO behavior has changed and why upgrades are urgent.

## 6. Publication record

(To be filled at publish time.)

- **Git commit hash (content):** `...`
- **Git commit hash (index.html update):** `...`
- **First GitHub push with story:** `2026-02-03T18:3XZ`
- **GitHub Pages build complete:** `2026-02-03T18:4XZ`
- **Optional external archive URL:** `...`
