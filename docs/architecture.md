# Architecture

```text
Internet -> Firewall -> Networks -> Sensors (Suricata/Zeek)
-> Collector -> Detection (Rules + ML) -> Correlation
-> Risk Engine -> Incident/Response -> Firewall/Quarantine -> Dashboard

Parallel: Network Telemetry -> Digital Twin -> Simulation -> Impact Analysis -> Dashboard
```

| Component | Code | Responsibility |
|---|---|---|
| Sensors | `lab/sensors/` | Suricata signatures, Zeek logs |
| Collector | `src/insoc/collector/` | Ingest and normalize events |
| Detection | `src/insoc/detection/` | Signature and behavioral rules |
| ML | `src/insoc/ml/` | Second detection layer (Random Forest baseline) |
| Risk | `src/insoc/risk/` | Score 0-100 from severity, confidence, frequency, asset criticality |
| Response | `src/insoc/response/` | Block IPs, isolate hosts, quarantine, rollback |
| Incidents | `src/insoc/incidents/` | Lifecycle and records |
| Twin | `src/insoc/twin/` | Network model and what-if simulation |
| Dashboard | `src/insoc/dashboard/` | RBAC views: Admin, SOC Analyst, Network Engineer |

## ML models

Random Forest baseline, compared with Decision Tree, Logistic Regression and XGBoost.
Metrics: accuracy, precision, recall, F1, confusion matrix, false positive rate, inference time.
