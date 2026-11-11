T1053.005 Scheduled Task Detection with Wazuh

Overview
This repository / exercise documents a controlled adversary simulation using Atomic Red Team to execute MITRE ATT&CK technique T1053.005 (Scheduled Task/Job: Scheduled Task) against a Windows host,
followed by successful detection and alerting in Wazuh SIEM.

The goal of this exercise is to validate detection capabilities for persistence and execution techniques that abuse the Windows Task Scheduler (commonly via schtasks.exe). These actions typically generate Windows Security Event ID 4698 (A scheduled task was created) along with related process creation events.
