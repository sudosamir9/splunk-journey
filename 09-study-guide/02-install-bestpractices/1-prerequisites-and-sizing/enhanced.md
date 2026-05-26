---
type: enhanced
theme: 02-install-bestpractices
topic: prerequisites-and-sizing
covers: "Lectures 5–8"
tags: [study-guide/enhanced, theme/02-install-bestpractices]
sources: docs.splunk.com (Splunk 9.x / latest, 2026)
---

# Splunk Deployment Prerequisites & Sizing

> Deep reference on what to decide and verify *before* installing Splunk: platforms and packages, getting-started licensing, capacity planning, reference hardware, validated architectures, accounts and filesystem, and network/ports. Companion `pre-class.md` holds the short primer and official-doc links.

---

## 0. Orientation

Installing Splunk is easy. Installing it *correctly for the workload it will carry* is the real skill, and almost all of that work happens before you run a single command. This topic covers the planning decisions an administrator makes up front:

- **Where** will it run (OS, package, single instance vs. distributed)?
- **How big** does it need to be (ingest volume, search load, retention → CPU, RAM, storage, IOPS, number of nodes)?
- **What** must the OS and network provide (accounts, filesystem, ports, time sync)?

Getting these wrong is expensive to fix later: under-sized indexers cause search timeouts and ingestion lag, the wrong filesystem layout makes retention changes painful, and missed ports break forwarding silently. Plan first.

---

## 1. Why planning matters

Splunk is infrastructure, not an app you install and forget. Its resource profile is unusual: indexing is **CPU- and I/O-intensive**, searching is **CPU- and RAM-intensive**, and both are sensitive to **storage latency (IOPS)** far more than to raw capacity. A server that looks adequate by CPU/RAM can still perform terribly if its disks can't deliver the I/O Splunk needs. So sizing is about matching three workload dimensions — **ingest volume, search concurrency, and retention** — to the right hardware and node count.

---

## 2. Supported platforms & packages

Splunk Enterprise (the full product) runs on:

- **Linux** — the dominant production platform. Distributed as a **`.tgz` tarball** (portable, unpacks anywhere) and as native packages: **`.rpm`** (Red Hat/CentOS/Rocky/Alma/SUSE) and **`.deb`** (Debian/Ubuntu).
- **Windows** — distributed as an **`.msi`** installer.
- **macOS** — supported chiefly for evaluation/development, not production.

Always run a **64-bit x86 (or supported ARM) architecture**. The package you choose affects how it installs (the tarball drops a self-contained tree you own; rpm/deb integrate with the package manager), but the resulting Splunk is the same.

> **Full Splunk vs. Universal Forwarder packages:** the UF is a *separate, smaller download* — don't install full Splunk Enterprise on endpoints where you only need to collect data. (Forwarders are covered in their own topic.)

---

## 3. Licensing to get started

You need a license tier before you ingest data:

| Tier | What it gives you | Limits |
|---|---|---|
| **Enterprise Trial** | Full Enterprise features for evaluation | **60 days**, **500 MB/day** ingest, then converts to Free (or you apply a purchased license) |
| **Splunk Free** | Indefinite, single-user | **500 MB/day**; **no authentication, no clustering, no alerting/scheduling, no distributed search** |
| **Dev/Test license** | Full features for non-production | Obtained via Splunk; for lab/dev use |
| **Splunk Cloud Trial** | Hosted Splunk Cloud | ~14 days |
| **Purchased Enterprise** | Production use | Volume/ingest- or workload-based entitlement (see the fundamentals/licensing material) |

For a lab, the **Enterprise Trial** is the right choice — full features (auth, distributed search, clustering) for 60 days, after which you re-apply a dev/trial license or rebuild. The Free license is too restrictive for a distributed lab because it disables authentication and distributed search.

---

## 4. Capacity planning — the three dimensions

Sizing flows from three independent questions. Answer each, then translate to hardware and node count.

1. **Daily ingest volume (GB/day).** How much *raw* data per day? This is the primary driver of how many **indexers** you need and how much **storage** you'll consume.
2. **Search workload (concurrency & type).** How many concurrent searches, and how heavy? Scheduled correlation searches (e.g., Enterprise Security) are far heavier than occasional ad-hoc lookups. Search load drives **CPU/RAM** on both search heads and indexers, and lowers the per-indexer ingest a node can sustain.
3. **Retention (days/months).** How long must data stay searchable (and then archived)? Retention multiplied by daily volume drives **storage capacity**.

**Translating to node count and storage:**

- **Indexers** ≈ `daily_ingest ÷ per-indexer sustainable volume`. The sustainable per-indexer volume depends heavily on search load: a rough planning guide is **~100 GB/day/indexer under heavy search (e.g., ES)**, more (toward ~200–300 GB/day) under light search. Always confirm against current validated architectures.
- **Storage** ≈ `daily_ingest × retention_days × ~0.5 (the on-disk ratio) × replication_factor`. Recall the ~50% rule (≈15% compressed rawdata + ≈35% tsidx/metadata). In a clustered environment multiply by the **Replication Factor** because you keep multiple copies.
- **Search heads** scale with **search concurrency**; concurrency is a function of CPU cores. Add search heads (or a search head cluster) when scheduled + ad-hoc concurrency exceeds what one can serve.

---

## 5. Reference hardware

Splunk publishes **reference hardware** specs as the baseline unit of capacity. Memorize the basic spec — it's the yardstick everything else is measured against.

| Spec | CPU | RAM | Typical use |
|---|---|---|---|
| **Basic** (reference unit) | **12 physical cores** (or 24 vCPU) @ ≥2 GHz | **12 GB** | A single indexer or a small standalone instance |
| **Mid-range** | **24 physical cores** (48 vCPU) | more RAM | Distributed nodes needing extra search concurrency |
| **High-performance** | **48 physical cores** (96 vCPU) | more RAM + faster storage | High indexing throughput + sustained search |

**Storage / IOPS is the part people under-spec.** Indexers need **high-IOPS, low-latency storage** (SSD/NVMe class). The indexing tier is I/O-bound; a reference indexer targets on the order of **~800–1,200 IOPS minimum**, and high-performance designs assume considerably more (shared arrays serving many indexers must provide thousands of concurrent IOPS in aggregate). Capacity (TB) matters for retention; **IOPS matters for performance** — don't confuse the two.

**Role-specific emphasis:**
- **Indexing tier** → fast storage (IOPS) above all, plus cores for parsing.
- **Search tier** → CPU cores and RAM for query concurrency.

Splunk's **Monitoring Console health check** compares the live instance against these reference specs and flags shortfalls (e.g., "physical memory below the 12 GB reference") — exactly the kind of warning you'll see and must act on.

---

## 6. Splunk Validated Architectures (SVA)

**SVAs** are Splunk's catalog of pre-vetted reference topologies — proven combinations of indexers, search heads, clustering, and management components for given scale and availability needs. Use them so you don't design a distributed deployment from scratch.

SVA design considers pillars such as **availability, performance, scalability, security, and manageability**, and presents topology "tiers" (single-server → distributed non-clustered → clustered → multi-site) you select from based on your volume, HA/DR requirements, and search load. When you plan a real deployment, you pick the SVA tier that matches your requirements and then size each component using reference hardware.

---

## 7. Pre-install accounts & filesystem decisions

Two decisions you make before the first `splunk start`:

- **Run as a dedicated non-root user.** Splunk strongly recommends **not** running as `root`. Create a service account (commonly `splunk`) and run Splunk as that user. This limits blast radius, follows least privilege, and is required for clean systemd management.
- **Install location = `$SPLUNK_HOME`.** The convention is **`/opt/splunk`** for full Splunk Enterprise (and `/opt/splunkforwarder` for the UF). After unpacking, **change ownership** of the tree to the service account (`chown -R splunk:splunk /opt/splunk`) so Splunk can write its data and logs.
- **Dedicate a filesystem for indexed data** where possible. Index data (`$SPLUNK_HOME/var/lib/splunk`) grows large and is I/O-hot; putting it on its own fast volume isolates it and makes capacity/retention management cleaner. Plan hot/warm on fast storage and cold on cheaper storage.

`$SPLUNK_HOME` orientation (you'll live here): `bin/` (the `splunk` CLI and binaries), `etc/` (all configuration — system, apps, users), `var/lib/splunk/` (the indexes), `var/log/splunk/` (Splunk's own logs, e.g., `splunkd.log`).

---

## 8. Network & ports

Plan firewall rules and time/name resolution before deploying, especially for a distributed build.

**Default / conventional ports to know:**

| Port | Purpose | Notes |
|---|---|---|
| **8000** | Splunk Web (HTTP/HTTPS) | the browser UI |
| **8089** | **splunkd management** | REST API, CLI, distributed comms, deployment server/clients, license manager |
| **9997** | Receiving (forwarder → indexer) | *convention* — you enable a receiver on this port; not on by default |
| **8088** | HTTP Event Collector (HEC) | when HEC is enabled |
| **8191** | KV Store | app/state storage (MongoDB-based) |
| **8065** | App server | Splunk Web's internal app/python server |
| **8080 / 9887** | Indexer cluster replication / data | configurable; used in clustered indexers |
| **514** | syslog | only if you receive syslog directly (often via an intermediate forwarder/HF) |

Notes that matter in practice:
- During install, **if a default port is already in use, Splunk prompts for an alternative** — so don't assume the defaults are always what's running; verify.
- **Forwarding** needs the indexer's receiving port (commonly 9997) open from forwarders.
- **Distributed search / management** needs 8089 reachable between search heads, indexers, and management nodes.
- **Time sync (NTP/chrony)** across all nodes is essential — Splunk is time-series; clock skew corrupts event timing and license metering (metered on the license manager's clock). Ensure consistent **DNS/hostname** resolution too.

---

## 9. Worked sizing example

Suppose: **300 GB/day** ingest, **90-day** searchable retention, moderate scheduled-search load, single-site HA via an indexer cluster with **Replication Factor 2**.

- **Indexers:** at ~100–150 GB/day/indexer under moderate search, 300 GB/day → **≈3 indexers** (round up for headroom and HA).
- **Storage:** `300 GB × 90 days × 0.5 × 2 (RF)` ≈ **27 TB** of indexed storage across the cluster, before headroom — split across hot/warm (fast) and cold (cheaper) tiers per your retention policy.
- **Search heads:** start with one (or a 3-member search head cluster if HA/concurrency demand it).
- **Management:** cluster manager, license manager, deployment server, monitoring console (co-located where resources allow in smaller builds).

This is the reasoning to internalize: dimensions → reference units → node count and storage.

---

## 10. Terminology & version notes

- Splunk's **Enterprise Trial** has long been **60 days / 500 MB per day**; the Free tier is **500 MB/day** with auth/clustering/distributed-search disabled. Exact entitlements for *purchased* licenses now span volume/ingest and workload-based models — confirm against current licensing docs.
- Reference-hardware **core counts increased** over older guidance (the modern "basic" spec is **12 physical cores**; mid/high specs scale to 24/48). Tutorials citing 4-core indexers are outdated.
- Supported OS versions move forward each release — always check the current **System Requirements** page for your target Splunk version rather than trusting an old list.

---

## 11. Common misconceptions

- **"More disk capacity fixes slow indexers."** No — indexers are usually **IOPS**-bound, not capacity-bound. Add fast storage/indexers, not just terabytes.
- **"Sizing is just about ingest volume."** Search load is co-equal: heavy scheduled search (ES) can halve per-indexer ingest capacity.
- **"The Free license is fine for a distributed lab."** It disables authentication and distributed search — use the Enterprise Trial.
- **"Install as root, it's simpler."** Splunk recommends a dedicated non-root account; root causes permission and security problems and complicates systemd.
- **"Default ports are guaranteed."** Install detects in-use ports and may assign alternatives; always verify what's actually listening.
- **"Capacity = retention only."** Don't forget the Replication Factor multiplier in a cluster, and the ~50% on-disk ratio.

---

## 12. Mastery checklist — what you should be able to explain

- Supported platforms and package types (`.tgz`, `.rpm`, `.deb`, `.msi`).
- Enterprise Trial limits (**60 days / 500 MB/day**) and what Splunk Free disables.
- **Reference hardware** baseline (12 physical cores / 12 GB) and that indexers need high IOPS.
- The capacity dimensions (ingest, search, retention) and the storage ~50% rule.
- Recommended **non-root** install and **`/opt/splunk`** as `$SPLUNK_HOME`, with ownership changed to the service account.
- Key **ports**: 8000 (web), 8089 (management), 9997 (receiving), 8088 (HEC), 8191 (KV store).
- The role of **Splunk Validated Architectures** and the **Monitoring Console health check** for verifying readiness.

---

## 13. Key terms (flashcard seeds)

- **Enterprise Trial** — full features, 60 days, 500 MB/day, then reverts to Free.
- **Splunk Free** — 500 MB/day, no auth/clustering/distributed search/alerting.
- **`$SPLUNK_HOME`** — the install root; `/opt/splunk` by convention.
- **Reference hardware** — Splunk's baseline capacity unit (basic = 12 cores / 12 GB).
- **IOPS** — storage I/O operations per second; the limiting factor for indexers.
- **Capacity dimensions** — ingest volume, search concurrency, retention.
- **Replication Factor (RF)** — number of raw data copies in an indexer cluster (multiplies storage).
- **Splunk Validated Architecture (SVA)** — Splunk's pre-vetted reference topologies.
- **Management port (8089)** — splunkd REST/CLI/distributed communications.
- **Receiving port (9997)** — conventional forwarder-to-indexer port.
- **HEC port (8088)** — HTTP Event Collector.
- **KV Store port (8191)** — key-value store.
- **Service account** — dedicated non-root user (commonly `splunk`) Splunk runs as.

---

## 14. Questions to drill (quiz seeds)

1. Name the package types Splunk Enterprise ships in and the OS each targets.
2. What are the exact limits of the Enterprise Trial license, and what does it become when the trial ends?
3. Which capabilities does the Splunk Free license disable, and why does that make it unsuitable for a distributed lab?
4. List the three capacity-planning dimensions and what each one drives (nodes vs. storage vs. CPU/RAM).
5. Estimate indexed storage for 200 GB/day, 60-day retention, RF 3. Show the formula.
6. What is the basic reference-hardware spec, and why is IOPS more important than raw capacity for an indexer?
7. Why does Splunk recommend a non-root service account, and what's the conventional `$SPLUNK_HOME`?
8. Map these ports to their purpose: 8000, 8089, 9997, 8088, 8191.
9. What does the Monitoring Console health check compare your instance against, and name two things it flags?
10. Why is NTP/time sync across all nodes critical in a Splunk deployment?
