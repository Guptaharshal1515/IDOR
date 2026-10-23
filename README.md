# IDOR — In-Depth Vulnerability Research

An internship-oriented research repository on Insecure Direct Object Reference (IDOR): how object-level authorization fails, how VAPT professionals validate the failure safely, how impact is assessed, and how developers prevent recurrence.
![[![IDOR vuln.png](https://github.com/Guptaharshal1515/IDOR/blob/main/assets/images/IDOR%20vuln.png)]]
## Scope and objectives

This repository covers web applications, APIs, file workflows, GraphQL, mobile backends, and multi-tenant systems. It focuses on authorization decisions and evidence-driven assessment; it does not contain a standalone vulnerable application, lab, or proof-of-concept project.

## Contents

1. [Introduction to IDOR](01%20-%20Introduction%20to%20IDOR/01-introduction.md)
2. [Technical foundations and root causes](02%20-%20Technical%20Foundation%20%26%20Root%20Causes/02-technical-foundations.md)
3. [Types and attack surfaces](03%20-%20Types%20and%20Attack%20Surfaces/03-types-and-attack-surfaces.md)
4. [Identifiers and security mechanisms](04%20-%20Identifiers%20and%20Security%20Mechanisms/04-identifiers-and-security.md)
5. [Discovery and testing methodology](05%20-%20IDOR%20Discovery%20and%20Testing%20Methodology/05-testing-methodology.md)
6. [Impact assessment and severity](06%20-%20Impact%20Assessment%20and%20Severity/06-impact-and-severity.md)
7. [Remediation and secure coding](07%20-%20Remediation%20and%20Secure%20Coding/07-remediation.md)
8. [Real-world case studies](08%20-%20Real-World%20Case%20Studies/08-real-world-case-studies.md)
9. [Reporting, checklist, and references](09%20-%20VAPT%20Reporting%2C%20Checklist%20and%20References/09-reporting-checklist-references.md)

## Repository map

Each numbered folder corresponds to one article section. `code-examples/` contains small illustrative Flask examples and regression tests. No example represents a verified finding in a live system.

The repository also includes three explanatory infographics in `assets/images/`. They are educational visuals, not screenshots from a real assessment.

## Responsible use

Test only systems for which you have explicit authorization and a defined scope. Use test accounts and non-sensitive records, minimize requests, preserve evidence safely, and report through the agreed disclosure channel. The examples and HTTP messages are illustrative unless explicitly labeled otherwise.

## References

The bibliography prioritizes OWASP, MITRE CWE, PortSwigger Web Security Academy, CISA guidance, and official standards. Claims about incidents are separated from technical analysis and linked to public sources.
"# IDOR" 
