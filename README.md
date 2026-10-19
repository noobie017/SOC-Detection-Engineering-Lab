# Windows 10 Endpoint – Atomic Red Team Detection Lab

**Lab Component:** Windows 10 Virtual Machine (Endpoint)  
**Purpose:** Adversary emulation using Atomic Red Team + detection validation with Wazuh  
**Last Updated:** October 2026

---

## Overview

This README documents the **Windows 10 VM** used as the attack surface in a home detection engineering lab.

The lab consists of:

| Component              | Role                                      | Type          |
|------------------------|-------------------------------------------|---------------|
| **Windows 10 VM**      | Endpoint under test (this document)       | Virtual Machine |
| **Ubuntu Server 24.04**| Wazuh Manager + Indexer + Dashboard       | Virtual Machine |
| **Host Laptop**        | Hypervisor + access to Wazuh Dashboard    | Physical Host |

**Goal:** Execute Atomic Red Team techniques mapped to the MITRE ATT&CK framework on the Windows 10 endpoint and observe the resulting alerts in the Wazuh dashboard.

---

## Lab Architecture

+-------------------------------------------------------------------+
|                         HOST LAPTOP                               |
|                    (Physical Hypervisor)                          |
|                                                                   |
|   +-----------------------+           +-----------------------+   |
|   |    Windows 10 VM      |           | Ubuntu Server 24.04   |   |
|   |  (Endpoint Under Test)|           |  - Wazuh Manager      |   |
|   |                       |           |  - Wazuh Indexer      |   |
|   | [Wazuh Agent Installed] --------> |  - Wazuh Dashboard    |   |
|   +-----------------------+   Logs    +-----------------------+   |
|               ^                                   ^               |
|               |                                   |               |
+---------------|-----------------------------------|---------------+
                |                                   |
                +-----------------------------------+
                     Accessed via Web Browser

Note on Architecture & Resource Constraints:
This lab environment is purposely consolidated onto a single physical host due to limited RAM capacity on the laptop. Running the all-in-one Ubuntu server (Wazuh Manager, Indexer, and Dashboard) alongside a Windows 10 endpoint VM maximizes resource efficiency for testing and evaluation without requiring dedicated physical hardware.
