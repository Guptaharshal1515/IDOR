# 5. IDOR Discovery and Testing Methodology

Testing must be authorized, scoped, and designed to minimize data access and side effects.

1. Confirm scope, test accounts, tenant boundaries, rate limits, sensitive actions, and evidence rules.
2. Map endpoints and workflows. Record references in paths, parameters, JSON, GraphQL variables, headers, filenames, download links, and job IDs.
3. Capture a baseline as Account A for an object A owns. Record status, response shape, and side effects.
4. Using Account B, request object A and, where approved, use a controlled second test object. Compare status, body, and state. Test reads and writes separately.
5. Check alternate representations: mobile/API versions, bulk operations, nested routes, exports, downloads, GraphQL aliases, and caches.
6. Validate with the smallest safe proof. Do not enumerate production records or alter data unnecessarily. Restore approved test changes.
7. Document preconditions, redacted requests, expected versus actual behavior, affected object class, scope, and remediation evidence.

Burp Suite Proxy helps map and retain requests; Repeater supports careful comparisons. Automated scanners can find parameters but generally cannot infer ownership, tenant policy, or business impact. A `200` is not the only signal: secure APIs may use `404` to conceal existence, while response differences can arise from caching or validation.

| Test | Expected secure result |
|---|---|
| A reads A’s object | Allowed |
| A reads B’s object | Denied or existence-concealing response |
| A updates B’s object | Denied; no state change |
| A deletes B’s object | Denied; object remains |
| Low-privilege user invokes admin operation | Denied by function policy |
