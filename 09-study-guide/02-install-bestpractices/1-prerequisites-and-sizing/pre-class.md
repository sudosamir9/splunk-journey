---
type: pre-class
theme: 02-install-bestpractices
topic: prerequisites-and-sizing
covers: "Lectures 5–8"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/02-install-bestpractices]
---

# Pre-class — Deployment Prerequisites & Sizing

> Read before the lectures (covers lectures 5–8). ~4–5 min. The videos show the *download/account* mechanics; this primer gives you the *planning* frame the videos mostly skip, which is what actually matters in practice.

## Why this matters
Installing Splunk is easy; sizing it correctly for its workload is the real skill — and it's almost all decided *before* you install. Under-sized indexers and bad filesystem/port choices are expensive to fix later.

## The mental model (hold these)
1. **Splunk is infrastructure with an unusual resource profile.** Indexing is CPU + I/O heavy; searching is CPU + RAM heavy; both are sensitive to **storage IOPS** more than to raw capacity.
2. **Sizing flows from three dimensions:** **ingest volume** (GB/day) → number of indexers + storage; **search load/concurrency** → CPU/RAM and search heads; **retention** → storage capacity.
3. **Reference hardware is the yardstick.** The basic spec is **12 physical cores / 12 GB RAM**; indexers also need **high-IOPS (SSD-class) storage**.
4. **Storage ≈ daily_volume × retention_days × ~0.5 × replication_factor.** (The ~50% is the on-disk ratio from the fundamentals topic; RF multiplies it in a cluster.)
5. **Plan accounts, filesystem, ports, and time sync up front:** run as a non-root `splunk` user, install to `/opt/splunk` (`$SPLUNK_HOME`) and `chown` it, dedicate fast storage for indexes, and open the right ports.

## Key terms (quick definitions)
- **Enterprise Trial** — full features, **60 days, 500 MB/day**, then reverts to Free.
- **Splunk Free** — 500 MB/day, but **no auth, no clustering, no distributed search** (so not great for a distributed lab).
- **`$SPLUNK_HOME`** — the install root; `/opt/splunk` by convention.
- **Reference hardware** — Splunk's baseline capacity unit (basic = 12 cores / 12 GB).
- **IOPS** — disk operations/second; the real bottleneck for indexers.
- **Replication Factor (RF)** — copies of raw data in an indexer cluster; multiplies storage.
- **SVA (Splunk Validated Architecture)** — pre-vetted reference topologies you choose from.
- **Ports:** 8000 web · 8089 management · 9997 receiving · 8088 HEC · 8191 KV store.

## Watch for this in the video
- The version shown is **9.0.1 (2022)** and downloads a `.tgz`. The download UI changes over time; the *steps* (create account → get the `wget` command → unpack to `/opt` → `chown` → start) are what matter.
- Note the **non-root `splunk` user** creation and **`chown splunk:splunk /opt`** — that's a best practice, not a formality.
- When the health check later flags "physical memory below reference," that's the **12 GB reference hardware** baseline talking.
- Reference-hardware core counts in older material may look low — the current basic spec is **12 physical cores**.

## Questions to hold in mind while watching
1. What are the three things I'd need to know to size a real deployment, and what does each one drive?
2. Why is storage **IOPS** more important than storage **capacity** for an indexer?
3. Why a non-root user and `/opt/splunk` — what breaks if I ignore that?
4. Which ports must be open for forwarding and for distributed search/management?

## How this connects forward
- The **install + hardening** topic (next) turns these decisions into commands: install, THP, ulimit, boot-start, health check.
- **Indexes & buckets** revisits storage sizing and the hot/warm/cold tiers your filesystem plan anticipates.
- **Forwarders & distributed setup** is where the ports and time-sync planning pay off.

---

## Official references (for verification / deeper reading)

| Topic | Splunk Docs page |
|---|---|
| System requirements (supported OS) | https://docs.splunk.com/Documentation/Splunk/latest/Installation/SystemRequirements |
| Reference hardware | https://docs.splunk.com/Documentation/Splunk/latest/Capacity/Referencehardware |
| Capacity planning manual | https://docs.splunk.com/Documentation/Splunk/latest/Capacity/IntroductiontocapacityplanningforSplunkEnterprise |
| Splunk Validated Architectures | https://www.splunk.com/en_us/pdfs/tech-brief/splunk-validated-architectures.pdf |
| How Splunk licensing works | https://docs.splunk.com/Documentation/Splunk/latest/Admin/HowSplunklicensingworks |
| Ports / components and the network | https://docs.splunk.com/Documentation/Splunk/latest/InheritedDeployment/Ports |
| Change default values (ports) | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Changedefaultvalues |
