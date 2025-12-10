# 📘 Network Security — Weekly Code Summaries

## 🔹 Week 2 — Cryptography Fundamentals  
This week focused on asymmetric cryptography using RSA. I implemented scripts to generate RSA key pairs, encrypt data using the public key, and decrypt using the private key. These exercises demonstrated core concepts of confidentiality, key management, and the mathematical foundation behind secure communication.

## 🔹 Week 3 — Password Security, Hashing & Two-Factor Authentication  
This week introduced secure password handling using hashing, salting, and peppering through bcrypt. I evaluated password entropy, compared salted vs unsalted hashing outcomes, and built a full TOTP-based two-factor authentication system using `pyotp`. This demonstrated why multi layered authentication is essential for modern network security.

## 🔹 Week 4 — File Integrity & Malware Behaviour Simulation  
This week explored integrity monitoring and basic malware behavior. I built a file integrity baseline generator, implemented change detection via hashing, and identified, modified or deleted files. Additional scripts were used to simulate malware concepts such as worms, signature based scanning, and network monitoring. This shows how security tools detect unauthorized changes and suspicious behavior.

## 🔹 Week 5 — Web Vulnerability Scanning (Wapiti)  
This week, I performed automated vulnerability scanning using Wapiti, generated HTML reports, and analysed detected issues such as CSP misconfigurations and injection risks. This introduced the workflow of web security testing, report interpretation, and how scanners categorize vulnerabilities into attacks, anomalies, and additional findings.

## 🔹 Week 6 — Static Malware Analysis  
Week 6 focused on static malware analysis techniques. I created scripts to compute file hashes such as MD5/SHA1/SHA256, I then extract readable strings, inspected PE imports, and detected indicators of compromise such as URLs and IPs. Then I wrote and evaluated a simple YARA rule. The tasks demonstrated how analysts examine suspicious executables without executing them.

## 🔹 Week 7 — Nmap & Network Reconnaissance Automation  
This week covered automated network reconnaissance. Python wrappers were used for Nmap to scan hosts, list ports, and extract IP information. Combining this with WHOIS lookups to gather ownership and network metadata. This reflected real world workflows used by penetration testers and defenders.

## 🔹 Week 9 — LLM Security & Adversarial Testing  
Week 9 explored security risks in large language models. Using a local Ollama model, testing prompt injection, data poisoning, model inversion, and model extraction attacks. Then documenting how the model responded, whether it resisted manipulation, and what information it showed. This week highlighted the emerging cybersecurity challenges introduced by generative AI systems.

