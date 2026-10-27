MITRE ATT&CK Technique: T1562.004 — Impair Defenses: Disable or Modify System Firewall 

Lab Component: Windows 10 Endpoint → Wazuh Manager (Ubuntu Server 24.04) Status: Attack executed · Telemetry confirmed ·  
No default alert triggered (detection gap identified) Last Updated: October 2026

Objective

Emulate an adversary disabling the Windows Firewall via netsh, validate that the Windows 10 endpoint's Sysmon telemetry reaches Wazuh, 
and determine whether the default Wazuh ruleset generates an alert for this behavior.

This executed the underlying command:

cmd
netsh advfirewall set allprofiles state off
