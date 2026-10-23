# 9. VAPT Reporting, Checklist and References

## Report template

**Title:** Missing object-level authorization on `[method] [endpoint]`  
**Summary:** Principal, object class, action, and boundary crossed.  
**Preconditions:** Account, role, tenant, token, or workflow state.  
**Evidence:** Redacted baseline/comparison requests, status, relevant fields, timestamps, and approved test IDs.  
**Expected behavior:** Deny or conceal existence according to policy.  
**Actual behavior:** Returned or changed object and verified side effect.  
**Impact and severity:** CIA impact, scope, exploitability, and business consequences.  
**Remediation:** Server-side object/tenant authorization at every read and mutation; regression tests.  
**Retest:** Owner access succeeds; cross-user and cross-tenant reads, writes, deletes, downloads, exports, and alternate versions are denied; denied writes cause no state change.

## Checklist

- Scope, authorization, test accounts, and evidence rules confirmed.
- References mapped in paths, query/body fields, headers, files, GraphQL, jobs, and exports.
- Owner, peer, cross-tenant, and low-privilege cases tested.
- Read, update, delete, download, and bulk actions considered.
- Alternate routes and API versions compared.
- Responses, side effects, caching, and false positives validated.
- Reproduction minimized and sensitive data redacted.
- Root cause and remediation tied to the failing policy decision.

## Bibliography

- [OWASP API1:2023 - BOLA](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/)
- [OWASP WSTG - API BOLA](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/12-API_Testing/02-API_Broken_Object_Level_Authorization/)
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [MITRE CWE-639](https://cwe.mitre.org/data/definitions/639.html)
- [PortSwigger - IDOR](https://portswigger.net/web-security/access-control/idor)
- [CISA AA23-208A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-208a)
