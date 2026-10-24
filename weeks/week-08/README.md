# Week 8: Automated response

**Goal:** Blocking, isolation and rollback work safely and are verified.

**Main owner:** SEC (Security engineer)

## Tasks

- [ ] **SEC** IP blocking through firewall rules with expiry
- [ ] **SEC** Host isolation and move to Quarantine VLAN 50
- [ ] **SEC** Allowlist, thresholds, rollback and audit log
- [ ] **NET** Firewall API or CLI access for the response module
- [ ] **SEC** Verification step: confirm the attacker is really contained

## Deliverables

Upload these files to `weeks/week-08/deliverables/`:

- Response actions description
- Audit log sample
- Before/after screenshots

## Where the code goes

`src/insoc/response/`, `lab/configs/`

## Definition of done

A Critical incident blocks the attacker, a rollback restores access, all logged.

## Weekly notes (fill in on Friday)

- Done:
- Blockers:
- Next week:
