# 8. Real-World Case Studies

Public material often omits implementation details. The examples below are labeled carefully so illustrative guidance is not presented as a breach report.

## CISA joint guidance

The CISA-led advisory [AA23-208A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-208a) describes IDOR as a recurring web and mobile API weakness: an identifier is used to access an object without checking whether the requester is authorized. It highlights disclosure, modification, deletion, and higher-privilege access as possible consequences. Lesson: every identifier-bearing function is an authorization point.

## OWASP API vehicle scenario

OWASP’s [API1:2023 guidance](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/) describes a vehicle API that accepts a VIN but fails to verify that it belongs to the authenticated driver. The scenario demonstrates why a high-entropy identifier is still unsafe without ownership validation. It is an OWASP scenario, not a confirmed production incident.

## OWASP API GraphQL deletion scenario

The same guidance describes a document-storage GraphQL mutation that deletes a document using a client-supplied ID without an object-level permission check. Lesson: GraphQL variables and mutations require the same per-object authorization as REST endpoints. This is also an illustrative OWASP scenario, not a CVE claim.

For a submission requiring a named breach, add only a separately verified disclosure after checking its original advisory, affected version, impact, and remediation.
