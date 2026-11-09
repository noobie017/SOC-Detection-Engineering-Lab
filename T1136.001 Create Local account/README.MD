# T1136.001 – Create Account: Local Account

MITRE ATT&CK ID:** T1136.001  
Tactic:** Persistence (TA0003)  
Platforms:** Windows, Linux, macOS  
Data Sources:** Windows Security Event Logs (Event ID 4720), Process Creation, Command Execution  



## 1. Technique Overview

Adversaries may create a local account on a compromised system to maintain persistent access. Local accounts are specific to a single host and do not require domain authentication.  

On Windows systems, this is commonly achieved using:
- `net user /add`
- PowerShell cmdlet `New-LocalUser`

These accounts can later be used for lateral movement, privilege escalation, or as a backup access method that does not rely on implanted remote access tools.

---
