# Atomic Red Team Detection Lab

## Overview

This repository documents a lightweight adversary simulation and detection validation lab built around **Atomic Red Team (ART)**.

The environment is designed for testing MITRE ATT&CK techniques on a resource-constrained Windows 10 endpoint while collecting high-fidelity telemetry through **Sysmon (Olaf Hartong configuration)** 
and forwarding it to a central **Wazuh** server for detection engineering and rule validation.

---

## Lab Architecture

| Component              | Details                                      |
|------------------------|----------------------------------------------|
| Endpoint               | Windows 10 (resource-constrained / low RAM) |
| Adversary Simulation   | Atomic Red Team + Invoke-AtomicRedTeam      |
| Endpoint Telemetry     | Sysmon (Olaf Hartong configuration)         |
| SIEM / Detection       | Wazuh Server                                |
| Purpose                | Technique execution → Detection validation  |


## Prerequisites

- Windows 10 machine with Atomic Red Team installed
- Sysmon deployed using **Olaf Hartong’s** configuration
- Wazuh agent installed and connected to the Wazuh manager
- PowerShell 5.1+ (Administrator privileges recommended)
- Antivirus exclusion for `C:\AtomicRedTeam` (strongly recommended)
