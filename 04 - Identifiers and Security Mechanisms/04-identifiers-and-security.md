# 4. Identifiers and Security Mechanisms

Identifiers are references, not permissions. Sequential integers are easy to enumerate and may reveal record volume or creation order. UUIDs, GUIDs, slugs, usernames, email addresses, encoded integers, composite keys, and opaque tokens change discoverability but do not change the authorization requirement. Base64 is encoding, not encryption; obscuring an ID is not an ownership check.

Useful defense-in-depth choices include opaque non-sequential identifiers, tenant-scoped resource names, short-lived download capabilities, and server-generated references. An attacker may still obtain a UUID through a list endpoint, notification, log, referer, or another workflow.

Authorization models may combine ownership, RBAC, ABAC, organization membership, resource state, and delegation. Do not accept `user_id`, `tenant_id`, or `role` from the client as the source of truth. Derive the principal from the authenticated context and constrain the object query using server-side policy. If sharing is intended, model it as an explicit capability with scope, expiry, revocation, and auditability.
