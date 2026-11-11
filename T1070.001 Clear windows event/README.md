T1070.001 Clear Windows Event Logs Detection with Wazuh

Overview
This repository / exercise documents a controlled adversary simulation using Atomic Red Team to execute MITRE ATT&CK technique T1070.001 (Indicator Removal: Clear Windows Event Logs) against a Windows host, followed by successful detection and alerting in Wazuh SIEM.

The goal of this exercise is to validate detection capabilities for defense evasion techniques that clear Windows Event Logs (via wevtutil, PowerShell Clear-EventLog, or similar). These actions generate Windows Security Event ID 1102 (The audit log was cleared) and related process creation events.
