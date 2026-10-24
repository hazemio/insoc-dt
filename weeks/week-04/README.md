# Week 4: Collector and signature detection

**Goal:** Events are parsed, normalized and signature rules fire reliably.

**Main owner:** SEC (Security engineer)

## Tasks

- [ ] **SEC** Write the collector: read `eve.json` and `conn.log`, output one event format
- [ ] **SEC** Signature rules: port scan, brute force, suspicious payload
- [ ] **SEC** Unit tests with sample events
- [ ] **DASH** Define the shared event and alert JSON schema
- [ ] **LEAD** Review the schema with every owner

## Deliverables

Upload these files to `weeks/week-04/deliverables/`:

- Event schema document
- Rule list with test evidence

## Where the code goes

`src/insoc/collector/`, `src/insoc/detection/`, `tests/`

## Definition of done

Generated attacks are detected and the tests pass in CI.

## Weekly notes (fill in on Friday)

- Done:
- Blockers:
- Next week:
