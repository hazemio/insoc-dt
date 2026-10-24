# Week 3: Sensors and baseline traffic

**Goal:** Suricata and Zeek see the traffic and write JSON logs.

**Main owner:** SEC (Security engineer)

## Tasks

- [ ] **SEC** Install Suricata and Zeek on a sensor host in VLAN 40
- [ ] **NET** Configure port mirroring (SPAN) from the switches to the sensor
- [ ] **SEC** Enable `eve.json` output and Zeek JSON logs
- [ ] **SEC** Load `lab/sensors/suricata/local.rules` and test one alert
- [ ] **ALL** Record 30 minutes of normal traffic as the baseline

## Deliverables

Upload these files to `weeks/week-03/deliverables/`:

- Sensor configs
- Sample `eve.json` and `conn.log` (small, no real data)
- Screenshots

## Where the code goes

`lab/sensors/`

## Definition of done

A test scan from Kali produces a Suricata alert and Zeek conn records.

## Weekly notes (fill in on Friday)

- Done:
- Blockers:
- Next week:
