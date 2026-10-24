# Research

| Folder | Content |
|---|---|
| `papers/` | One summary per paper: `YYYY-author-topic.md` |
| `datasets/` | Dataset notes only (source, license, features). Never commit raw data |
| `experiments/` | One file per experiment: hypothesis, setup, results, conclusion |
| `references/` | Bibliography (`references.bib`) |

## Starter reading

Digital twin and security:

- Digital Twins for security, survey: https://arxiv.org/pdf/2505.17310
- Intrusion detection of a LAN using a digital twin (Snort 3): https://ir.unilag.edu.ng/handle/123456789/13371
- Digital twin based IDS for industrial control systems: https://arxiv.org/abs/2207.09999v1
- Aether, network validation with agentic AI and digital twin: https://arxiv.org/pdf/2604.18233

What-if network analysis:

- Batfish (open source): https://github.com/batfish/batfish
- A General Approach to Network Configuration Analysis (NSDI 2015): https://ratul.org/papers/nsdi2015-batfish.pdf

Open source SOC examples:

- SOC Automation Lab (Wazuh, Shuffle, TheHive): https://github.com/guideops/SOC-Automation-Lab
- Open source SOC with Suricata and Zeek: https://solomonneas.dev/projects/designing-and-building-an-open-source-soc

## Datasets for the ML part

- NetFlow datasets (UNSW-NB15, CSE-CIC-IDS2018, UQ-NIDS): https://staff.itee.uq.edu.au/marius/NIDS_datasets/
- Dataset page: https://www.cyber.uq.edu.au/node/824
- Standard feature set paper: https://arxiv.org/pdf/2101.11315
- Critique of synthetic NIDS datasets: https://arxiv.org/pdf/2104.09029

Plan: train on a public dataset, then also test on traffic recorded in our own lab.
