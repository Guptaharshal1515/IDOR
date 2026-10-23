# 1. Introduction to IDOR

## Definition

Insecure Direct Object Reference is an access-control failure in which an application accepts a client-controlled reference-such as an invoice ID, filename, UUID, username, or nested resource key-and retrieves or changes the referenced object without verifying that the current principal is entitled to perform that action. The reference may be predictable, but predictability is not the vulnerability; the missing object-level authorization decision is.

Authentication answers “who is this?” Authorization answers “may this principal perform this action on this object?” An authenticated session therefore does not imply access to every object in the database.

```http
GET /api/invoices/1042 HTTP/1.1
Host: example.test
Cookie: session=alice-session

HTTP/1.1 200 OK
{"id":1042,"owner":"bob","total":8750}
```

If Alice can change `1042` to Bob’s invoice and receive it, the server authenticated Alice but failed to authorize the requested object. A secure response may be `403 Forbidden`, or `404 Not Found` where the API deliberately conceals resource existence.

## Classification

IDOR is commonly treated as Broken Access Control, OWASP Top 10 A01. In API work, the corresponding term is Broken Object Level Authorization (BOLA), API1:2023. CWE-639, Authorization Bypass Through User-Controlled Key, is a useful mapping when a user-controlled key selects another user’s record; CWE-863 and CWE-284 may also be relevant. IDOR is not authentication bypass, SQL injection, or merely “using an integer ID.” It is the unauthorized object action.

## Why it matters

The same defect can disclose personal data, alter orders, delete evidence, expose documents, or cross a tenant boundary. Risk must be based on the object, action, scope, and demonstrated consequence.

Sources: [OWASP API1:2023](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/), [MITRE CWE-639](https://cwe.mitre.org/data/definitions/639.html), [PortSwigger IDOR](https://portswigger.net/web-security/access-control/idor).
