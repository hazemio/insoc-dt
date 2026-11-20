# Datasets

Public datasets used to train and evaluate the ML detection layer of INSOC-DT (Phase 5).

> **Do not commit dataset files to Git.** They are large. The `.gitignore` in this folder blocks everything except this README. Each team member downloads the data locally by following the steps below.

## 1. Datasets used

| Dataset | Used for | Official page | Citation key (`references.bib`) |
|---|---|---|---|
| CIC-IDS2017 | Main training and evaluation (port scan, brute force, DoS, etc.) | https://www.unb.ca/cic/datasets/ids-2017.html | `sharafaldin2018toward` |
| UNSW-NB15 | Second dataset to test generalization across datasets | https://research.unsw.edu.au/projects/unsw-nb15-dataset | `moustafa2015unsw` |

Always download from the official pages. Third-party mirrors (Kaggle, Hugging Face) are acceptable for quick experiments only, and the final report should cite the original source.

## 2. Download steps

1. Open the official page of the dataset.
2. Download the **CSV / flow-level files** first (smaller, enough for ML training). Download raw PCAPs only if needed, since they are very large.
3. Place the files using the layout below.
4. Fill in the **Download log** at the bottom of this file.

## 3. Local folder layout

```
datasets/
├── README.md              <- tracked in Git
├── .gitignore             <- tracked in Git
├── cicids2017/            <- local only (ignored)
│   ├── raw/               original files exactly as downloaded
│   └── processed/         cleaned data produced by our scripts
└── unsw-nb15/             <- local only (ignored)
    ├── raw/
    └── processed/
```

Never edit files in `raw/`. All cleaning happens in code (saved under `experiments/`) and writes to `processed/`.

## 4. Known issues (read before training)

- **CIC-IDS2017 has documented problems**: labeling errors and flow-construction issues in the original CSV files and in the CICFlowMeter tool that produced the features. See Engelen et al. (`engelen2021troubleshooting`).
- The data is **highly imbalanced** (benign traffic dominates most attack classes). Plan for this when choosing metrics (use Precision, Recall, F1 and the confusion matrix, not accuracy alone) and when splitting the data.
- Some columns contain `NaN` / `Infinity` values and duplicate rows that must be handled during cleaning.
- Features are flow-based. Our live pipeline (Suricata/Zeek) must produce **compatible features** or we must map between them. Document the mapping in `experiments/`.

## 5. Cleaning checklist

- [ ] Remove duplicate rows
- [ ] Handle `NaN` and `Infinity` values
- [ ] Strip whitespace from column names
- [ ] Fix or drop mislabeled flows (following Engelen et al.)
- [ ] Remove identifier columns that leak the answer (IP addresses, timestamps, flow IDs) unless justified
- [ ] Split train/test **before** any scaling or resampling, to avoid data leakage
- [ ] Record the final class distribution in the experiment notes

## 6. Our own lab data

Public datasets are for training and benchmarking. The final demo uses **traffic generated in our own lab** (isolated Kali attacker, Suricata and Zeek logs). Lab captures go in `experiments/` or a separate local folder, never in this one.

## 7. Download log

Fill in one row per download.

| Dataset | Files downloaded | Size | Date | Downloaded by | SHA-256 (optional) |
|---|---|---|---|---|---|
| CIC-IDS2017 | | | | | |
| UNSW-NB15 | | | | | |
