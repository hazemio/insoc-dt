# Project charter

## Objectives

- Network monitoring and intrusion detection
- ML-based threat classification
- Risk scoring and incident management
- Automated IP blocking and host isolation
- Digital twin for simulation and what-if analysis
- SOC dashboard with role-based access

## Milestones

| # | Milestone | Deliverable |
|---|---|---|
| 1 | Lab network | Topology, VLANs, firewall, endpoints, Kali attacker |
| 2 | Sensors and collector | Suricata/Zeek logs flowing to the collector |
| 3 | Detection | Signature and behavioral rules |
| 4 | ML | Trained and compared models with report |
| 5 | Risk and response | Scoring, blocking, quarantine, rollback |
| 6 | Digital twin | Model and what-if scenarios |
| 7 | Dashboard and incidents | RBAC UI, incident lifecycle |
| 8 | Evaluation and demo | Metrics report, rehearsal |

## Evaluation metrics

| Area | Metrics |
|---|---|
| IDS | Detection rate, FPR, precision, recall, F1 |
| ML | Accuracy, precision, recall, F1, confusion matrix, inference time |
| Response | Detection time, response time, containment and rollback success |
| Network | Latency, packet loss, throughput, CPU/memory |
| Digital twin | Model agreement, connectivity validation, prediction accuracy |
