 # Atomic Red Team – T1110 Brute Force Detection with Wazuh

## Overview

This repository / exercise documents a controlled adversary simulation using **Atomic Red Team** to execute MITRE ATT&CK technique **T1110.001 (Brute Force: Password Guessing)** against a Windows 10 host, 
followed by successful detection and alerting in **Wazuh SIEM**.

The goal of this exercise is to validate detection capabilities for credential access attacks that generate high-frequency Windows Security Event ID 4625 (failed logon attempts).

---

## Environment

| Component              | Details                                      |
|------------------------|----------------------------------------------|
| Target Host            | Windows 10 (`windows10`)                     |
| IP Address             | 192.168.175.131                              |
| Atomic Red Team Path   | `C:\AtomicRedTeam`                           |
| SIEM                   | Wazuh                                        |
| Detection Index        | `wazuh-alerts*` / `wazuh-archives*`          |
| Technique              | T1110 / T1110.001 – Password Guessing        |
| Tactic                 | Credential Access (TA0006)                   |

---

## Prerequisites

- Atomic Red Team installed on the target Windows host
- PowerShell running as **Administrator**
- Wazuh agent installed and reporting to the Wazuh manager
- Windows Security auditing enabled for logon events

---

## Execution Steps

### 1. Load Atomic Red Team Module

powershell
cd C:\AtomicRedTeam
Import-Module .\invoke-atomicredteam\Invoke-AtomicRedTeam.psd1 -Force
2. Execute the Test
powershell    
Invoke-AtomicTest T1110.001 -TestNumbers 1
