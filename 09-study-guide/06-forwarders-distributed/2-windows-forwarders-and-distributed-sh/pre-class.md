---
type: pre-class
theme: 06-forwarders-distributed
topic: 2-windows-forwarders-and-distributed-sh
covers: "Lectures 34–36"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/06-forwarders-distributed]
---

# Pre-class — Windows Forwarders, Technology Add-ons, and Distributed Search

> Read before the videos (covers lectures 34–36). ~4–5 min. Two significant concepts land here: the TA split-tier deployment pattern (non-obvious until someone explains it clearly) and the distributed search architecture (the model everything else in Splunk scaling builds on).

## Why this matters
Windows Event Logs are the primary data source in most enterprise security environments — they feed SIEM, detection, and compliance workflows. Getting them into Splunk correctly requires understanding how the Splunk Add-on for Windows works and why it must be installed in multiple places. Distributed search is the foundation of every scaled Splunk deployment. Understanding these two patterns at the two-machine level now makes the clustered, multi-site version obvious later.

## The mental model (hold these)

1. **The Windows UF installs via MSI; the directory structure is identical to Linux.** Same `etc\apps\`, `etc\system\`, `bin\` layout under `C:\Program Files\SplunkUniversalForwarder\`. Same conf layering rules. The UF runs as a Windows service (`SplunkForwarder`), not a background daemon.
2. **Windows Event Logs are not files — they are API-accessed channels.** The `[WinEventLog://<channel>]` input stanza tells the UF to read a named channel (Security, System, Application) via the Windows Event Log API. You cannot monitor these as files with `[monitor://...]`.
3. **Technology add-ons (TAs) must be split across tiers — this is the critical pattern.** A TA contains two distinct things: `inputs.conf` (what to collect) and `props.conf`/`transforms.conf` (how to parse). The UF needs `inputs.conf`. The indexer needs `props.conf`/`transforms.conf`. The search head needs the search-time knowledge. Deploy all three, each with the right parts active.
4. **A dedicated search head holds no data.** It is a pure dispatch/merge node. When a user searches, the search head fans the query to all configured indexer search peers, each peer searches its own buckets, and the search head merges the results.
5. **Search peers are added on the search head side via port 8089 (management), not port 9997 (data).** The distinction matters: 9997 is for forwarder → indexer data flow; 8089 is for search head ↔ indexer management/search coordination.
6. **The knowledge bundle is what makes distributed search work correctly.** The search head replicates its knowledge objects (props, transforms, lookups) to every peer so field extractions defined in apps on the search head are available when the peer executes its sub-search.

## Key terms (quick definitions)

- **Windows UF MSI** — `.msi` installer; wizard screens for receiving indexer + deployment server; installs as `SplunkForwarder` service.
- **`[WinEventLog://<channel>]`** — `inputs.conf` stanza for Windows event log channels (Security, System, Application).
- **`renderXml = true`** — collect events in XML format; richer structured fields; preferred since TA v6.0.
- **Technology add-on (TA)** — packaged app: `inputs.conf` + `props.conf` + `transforms.conf` + knowledge objects for a specific source type.
- **Split-tier TA deployment** — `inputs.conf` on UF; `props.conf`/`transforms.conf` on indexer; all three plus search-time knowledge on search head.
- **Dedicated search head** — Splunk instance with no local data; dispatches searches to indexer peers.
- **Search peers** — indexers registered on the search head that execute sub-searches on their local data.
- **Knowledge bundle** — compressed archive of knowledge objects (props, lookups, eventtypes) replicated from search head to peers.
- **`distsearch.conf`** — search head config file; `[distributedSearch] servers = https://<indexer>:8089`.
- **Port 8089** — Splunk management port; used for distributed search, CLI, REST API, Deployment Server.
- **Quarantine mode** — excludes a slow indexer peer from searches without deleting its data.

## Watch for this in the video

- During Windows UF install, the wizard asks for a Receiving Indexer — this pre-populates `outputs.conf`. Pay attention to what it configures vs what you still need to do manually.
- When the Splunk Add-on for Windows is deployed and `inputs.conf` stanzas are enabled (`disabled = 0`), note that the index must be explicitly set — the add-on's defaults do not automatically send to a specific index.
- When the search head is configured, the peer is added via `Settings → Distributed search → Search peers` — note that the port used is 8089, not 9997.
- After the search peer is added, watch how the same data that was indexed by the indexer is now searchable from the search head — the search head itself contributed zero events.

## Questions to hold in mind while watching

1. If the TA is only on the UF, data reaches the indexer but what specifically is broken at the indexer and search head?
2. What happens to search performance when a peer is slow — and how does quarantine solve it without losing data?
3. After adding a search peer via Splunk Web, what file on the search head changes, and where is it?
4. Why does the knowledge bundle need to travel from the search head to the indexer peers, and what would break if it didn't?

## How this connects forward

- **Deployment Server (DS):** The manual TA deployment you see here (copy to `etc/apps/`) is exactly what the DS automates. The DS pushes server classes containing TAs to groups of UFs, saving you from touching each machine.
- **Indexer clustering:** In a cluster of three indexers, the search head has all three as search peers. Each peer has a copy of some buckets and the search head merges results from all three. The `distsearch.conf` pattern you see here scales directly.
- **Search Head Clustering (SHC):** Multiple search heads behind a load balancer, with a Deployer managing knowledge object distribution. Builds directly on the single-SH distributed search model.
- **Data onboarding / props+transforms:** The TA you deploy here is the embodiment of the props/transforms topic — the TA is exactly a packaged `props.conf`/`transforms.conf` for a specific source type.

---

## Official references

| Topic | Splunk Docs page |
|---|---|
| Install a Windows universal forwarder | https://docs.splunk.com/Documentation/Forwarder/latest/Forwarder/InstallaWindowsuniversalforwarderfromaninstaller |
| Monitor Windows event log data | https://docs.splunk.com/Documentation/Splunk/latest/Data/MonitorWindowseventlogdata |
| Splunk Add-on for Microsoft Windows | https://docs.splunk.com/Documentation/AddOns/released/Windows/Configuration |
| About distributed search | https://docs.splunk.com/Documentation/Splunk/latest/DistSearch/Whatisdistributedsearch |
| Add search peers to the search head | https://docs.splunk.com/Documentation/Splunk/latest/DistSearch/Configuredistributedsearch |
| Knowledge bundle replication overview | https://docs.splunk.com/Documentation/Splunk/latest/DistSearch/Knowledgebundlereplication |
| distsearch.conf spec | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Distsearchconf |
