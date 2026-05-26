---
type: pre-class
theme: 01-fundamentals
topic: fundamentals-and-architecture
covers: "Lectures 1–4"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/01-fundamentals]
---

# Pre-class — Splunk Fundamentals & Architecture

> Read this **before** the lectures (covers lectures 1–4). ~4–5 minutes. Pairs with the audio overview. The goal is to walk in already holding the skeleton, so the videos just hang detail on a frame you already have.

## Why this matters
These first lectures are the skeleton for the *entire* discipline of Splunk administration. Everything later — installing, configuration files, indexes, forwarders, the deployment server, data onboarding — is just the detailed mechanics of two things introduced here: the **data pipeline** and the **components**. Get this solid and the advanced material gets much easier.

## The mental model (hold these six things)
1. **Splunk turns messy machine data into searchable events.** It ingests almost anything, indexes it, and lets you search, correlate, alert, and visualize across all of it in near real time. The loop is **data → insight → action**.
2. **Schema-on-read (late-binding schema).** Unlike a database, Splunk stores the *raw* event and applies structure (fields) **at search time** — flexible, reversible, and resistant to data loss. This is the defining idea of the platform.
3. **The data pipeline has four ordered segments: Input → Parsing → Indexing → Search.** Different work happens in each, and *different config files control each*. (Some explanations say "three stages" by merging parsing and indexing — use four.)
4. **Index-time vs. search-time.** A few things are decided *irreversibly* at index time (baked into the bucket); most field work is done cheaply and reversibly at search time. **Default to search time.**
5. **One package, many roles.** Every full component installs from the same Splunk Enterprise package; *configuration* decides whether it's an indexer, a search head, a heavy forwarder, etc. (The **Universal Forwarder** is the one separate, lightweight package.)
6. **Standalone vs. distributed.** One instance can do everything (great for labs/PoC); real deployments split the roles across dedicated machines so each can scale and stay available.

## Key terms (quick definitions)
- **Event** — one time-stamped record. **`_time`** = its timestamp; **`_raw`** = its original text.
- **host / source / sourcetype** — the three metadata fields. **Sourcetype** is the important one: it drives how data is parsed and how fields are extracted.
- **UF (Universal Forwarder)** — lightweight agent; **forwards only**, can't index or search, sends **unparsed ("uncooked")** data, free.
- **HF (Heavy Forwarder)** — full Splunk instance; **parses** data before forwarding (**"cooked"**), so the indexer skips parsing; licensed; can run add-ons a UF can't (DB Connect, HEC).
- **Indexer (search peer)** — parses, indexes, stores data in **buckets**, and searches its own data.
- **Search Head** — runs SPL, sends searches to indexers, merges the results.
- **Index → buckets** — an index is physically a set of bucket directories holding compressed **rawdata** + **tsidx** (the searchable keyword index). Buckets age **hot → warm → cold → frozen**.
- **Deployment Server vs. SHC Deployer** — DS manages **forwarders**; the Deployer pushes config to **search-head-cluster** members. Different components — don't mix them up.

## Watch for this in the video
- The lectures use some **older names**: "Cluster **Master**" is now the **Cluster Manager Node**, and "License **Master**" is now the **License Manager** (renamed in Splunk 9.0). Same roles — just mentally substitute the current term.
- The point that **"a heavy forwarder sends cooked data, so the indexer doesn't re-parse it"** is one people often get wrong — lock it in.
- Parsing and indexing may be presented as one "stage." Keep them **separate** in your head (different segments, different config files).
- The version shown is **9.0.1 (2022)**; current docs are 9.x/latest. The one behavior change that matters: a license violation **no longer blocks search** today (it used to).
- When components are toured, keep asking *"is this a processing component (touches data) or a management component (coordinates the others)?"*

## Questions to hold in mind while watching
1. For each pipeline segment, *which component performs it* and *which config file controls it*?
2. What exactly is the difference between a UF and an HF — and why does "cooked vs. uncooked" matter to the indexer?
3. Why would you ever process something at **index time** instead of **search time** — and why is search time the default?
4. What's the difference between the Deployment Server, the SHC Deployer, and the Cluster Manager Node?

## How this connects forward
- **Sourcetype** comes back as its own major topic in data flow — it's the key to clean onboarding.
- **Buckets, retention, and the fishbucket** get a full treatment in the indexes topic.
- **`props.conf` / `transforms.conf`** (the parsing controls named above) are the core of the data-onboarding topic.
- **Forwarders and the deployment server** each get hands-on labs later — this is where the components stop being diagrams and start being machines you configure.

---

## Official references (for verification / deeper reading)

| Topic                                           | Splunk Docs page                                                                                     |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| The data pipeline                               | https://docs.splunk.com/Documentation/Splunk/latest/Deploy/Datapipeline                              |
| Components of a deployment                      | https://docs.splunk.com/Documentation/Splunk/latest/Capacity/ComponentsofaSplunkEnterprisedeployment |
| Types of forwarders (UF vs HF, cooked/uncooked) | https://docs.splunk.com/Documentation/Splunk/latest/Forwarding/Typesofforwarders                     |
| How the indexer stores indexes (buckets)        | https://docs.splunk.com/Documentation/Splunk/latest/Indexer/HowSplunkstoresindexes                   |
| tsidx file / rawdata file                       | https://docs.splunk.com/Splexicon:Tsidxfile · https://docs.splunk.com/Splexicon:Rawdatafile          |
| Index time vs. search time                      | https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Indextimeversussearchtime                |
| How Splunk licensing works                      | https://docs.splunk.com/Documentation/Splunk/latest/Admin/HowSplunklicensingworks                    |
| Manager node (master→manager rename)            | https://docs.splunk.com/Splexicon:Managernode                                                        |
