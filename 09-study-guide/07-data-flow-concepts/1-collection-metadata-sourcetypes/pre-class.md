---
type: pre-class
theme: 07-data-flow-concepts
topic: 1-collection-metadata-sourcetypes
covers: "Lectures 37–39"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/07-data-flow-concepts]
---

# Pre-class — Data Collection Methods, Metadata Fields & Sourcetypes

> Read before the videos (covers lectures 37–39). ~4–5 min. These three lectures move fast through a lot of mechanism — walk in already holding the model so you can focus on the *why* rather than scrambling to absorb the *what*.

## Why this matters
Data never arrives in Splunk pre-labelled and pre-structured. Every event has to be collected by some input mechanism, tagged with metadata that tells Splunk where it came from and what it is, and then parsed according to that metadata. If any of these steps are done wrong — wrong collection method, wrong metadata, especially wrong sourcetype — the damage cascades through every downstream pipeline stage. Searches return nothing. CIM mappings never fire. Timestamps are wrong. Understanding this chain is the foundation for every data onboarding task you will ever do.

## The mental model (hold these)
1. **The pipeline has four stages: Input → Parsing → Indexing → Search.** The forwarder handles Input; the indexer handles Parsing and Indexing; the search head handles Search. Each stage has specific jobs and knows nothing about the others' internal workings.
2. **Every event carries four primary metadata fields — `host`, `source`, `sourcetype`, `index` — assigned at the Input stage.** A fifth field, `_time`, is assigned later at the Parsing stage (because extracting a timestamp requires first having a discrete event, which requires sourcetype-based line breaking).
3. **Sourcetype is the lookup key for everything in `props.conf`.** Line breaking rules, timestamp extraction patterns, search-time field extractions, CIM field aliases — all are written as `[sourcetype_name]` stanzas in `props.conf`. Wrong sourcetype = wrong stanza fires = broken data.
4. **Six main collection methods:** monitor inputs (UF tailing files), TCP/UDP (syslog receivers), HEC (agent-free HTTP push), scripted inputs (polling scripts), modular inputs (packaged add-on collectors), Windows-specific inputs (Event Log, perfmon, AD, registry). Choose by infrastructure constraints, not preference.
5. **Explicit sourcetype assignment in `inputs.conf` is mandatory for production.** Splunk's automatic classifier works for common formats like syslog and access logs, but is unreliable for custom or vendor-specific data. The rule: always set `sourcetype =` in the stanza.
6. **Sourcetype naming convention matters for add-on CIM mappings.** Splunk add-ons ship `props.conf` keyed to specific sourcetype names (e.g., `pan:traffic`, `cisco:asa`). If your events carry a different sourcetype name, the add-on's field extractions and CIM mappings never fire.

## Key terms (quick definitions)
- **Input stage** — raw data acquisition + metadata assignment; runs on the forwarder.
- **Parsing stage** — event breaking + timestamp extraction; runs on the indexer.
- **`host`** — originating machine hostname; defaults to UF's own hostname; override for relay scenarios.
- **`source`** — originating file path or stream identifier; the "where from?" field.
- **`sourcetype`** — data classification; the "what kind?" field; lookup key for all `props.conf` rules.
- **`index`** — destination index; assigned at input; immutable after write.
- **`_time`** — event timestamp extracted at parse time from event text (not the forwarder's clock).
- **`[monitor://]`** — inputs.conf stanza for file/directory continuous tailing.
- **`[splunktcp://9997]`** — receiving stanza on indexer for Splunk-to-Splunk (S2S) forwarder traffic.
- **HEC** — HTTP Event Collector; agent-free JSON push on port 8088; needs a HF or full instance to host.
- **LINE_BREAKER / SHOULD_LINEMERGE** — `props.conf` settings that define event boundaries, keyed to sourcetype.

## Watch for this in the video
- The explanation of why `source` and `sourcetype` are different things — source is the file path (where from), sourcetype is the processing key (what kind). The distinction sounds obvious but is confused constantly in practice.
- When the pipeline assigns each default field — the videos step through this explicitly. Pay attention to the fact that `_time` is NOT assigned by the forwarder.
- The demo showing Splunk automatically recognising a sourcetype for a sample file upload — notice it works cleanly for access logs, but the point being made is that for real production data you never rely on this.
- How installing a Splunk add-on adds new sourcetype definitions — and the implication that your input stanzas must use those exact sourcetype names for the add-on to do anything useful.

## Questions to hold in mind while watching
1. A syslog relay is forwarding logs from 50 firewalls. What will `host` contain without any override, and why is that wrong? What attribute fixes it?
2. I set `sourcetype = wrong_type` on a monitor input. At what stage does parsing break, and what are the visible symptoms?
3. What is the difference between a scripted input and a modular input — and when would you choose one over the other?
4. HEC doesn't need a UF on the sender. So what does need to run HEC, and what does the sender need to do?

## How this connects forward
- **Data onboarding / `props.conf` + `transforms.conf`** — everything in those files is a `[sourcetype]` stanza; this topic is the prerequisite.
- **Routing and load balancing (next topic)** — the `_TCP_ROUTING` mechanism and index-routing transforms both operate on the metadata fields introduced here.
- **CIM and Technology Add-ons** — TAs ship sourcetype-keyed `props.conf`; if the sourcetype on your events doesn't match the TA's stanza name, you get nothing.
- **Index design** — `index =` in the input stanza is how events land in the right bucket for RBAC and retention; it cannot be corrected after the fact.

---

## Official references (for verification / deeper reading)

| Topic | Splunk Docs page |
|---|---|
| About default fields (host, source, sourcetype, index, _time) | https://docs.splunk.com/Documentation/Splunk/latest/Data/Aboutdefaultfields |
| How data moves through the pipeline | https://docs.splunk.com/Documentation/Splunk/latest/Deploy/Datapipeline |
| Monitor files and directories with inputs.conf | https://docs.splunk.com/Documentation/Splunk/latest/Data/Monitorfilesanddirectorieswithinputs.conf |
| Set up and use HTTP Event Collector | https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector |
| Configure event line breaking | https://docs.splunk.com/Documentation/Splunk/latest/Data/Configureeventlinebreaking |
| Create source types | https://docs.splunk.com/Documentation/Splunk/latest/Data/Createsourcetypes |
| Source types for add-ons (naming conventions) | https://docs.splunk.com/Documentation/AddOns/released/Overview/Sourcetypes |
