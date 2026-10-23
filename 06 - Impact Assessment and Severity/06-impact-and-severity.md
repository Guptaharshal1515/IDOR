# 6. Impact Assessment and Severity

Assess confidentiality, integrity, and availability separately. A read-only profile may expose personal data; an update may alter payment details; deletion may create recovery costs. Cross-tenant access generally increases scope because one customer can reach another customer’s data.

Severity should be evidence-led. Consider authentication and privileges required, discoverability of the reference, repeatability, object sensitivity, action, number of tenants or records reachable, and whether the defect enables account takeover, financial fraud, safety impact, or durable deletion. CVSS can structure technical exploitability and impact, but business risk should also capture regulatory, contractual, operational, and reputational consequences.

An illustrative low-impact case might expose a non-sensitive display preference between users. An illustrative high-impact case might allow an authenticated tenant member to download another tenant’s identity documents or change payout details. These are examples, not ratings for a real system.

A defensible report explains the chain: “Account B, using a valid session, changed object reference X; the server returned or changed object A; the object contained Y; no state outside the approved test account was touched.” Do not claim full database exposure when testing established only one object class.
