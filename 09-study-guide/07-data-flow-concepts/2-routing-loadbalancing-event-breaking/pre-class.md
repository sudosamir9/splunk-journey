---
type: pre-class
theme: 07-data-flow-concepts
topic: 2-routing-loadbalancing-event-breaking
covers: "Lectures 40–43"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/07-data-flow-concepts]
---

# Pre-class — Routing, Load Balancing & Event Breaking

> Read before the videos (covers lectures 40–43). ~4–5 min. These lectures cover a cluster of related mechanisms that are easy to confuse with each other. Walk in already knowing what problem each one solves and you can follow the config examples without getting lost.

## Why this matters
A production Splunk deployment has many forwarders feeding many indexers. Without load balancing, all data lands on one indexer and the others sit idle. Without event breaking, load balancing silently fails for large continuous files. Without routing, you cannot direct sensitive data to security-specific indexers. Without null-queue filtering, low-value events inflate your license for no analytical benefit. These are four distinct problems solved by four interlocking mechanisms — and the instinct to conflate them is one of the most common sources of misconfiguration.

## The mental model (hold these)
1. **Load balancing (`outputs.conf`) distributes data across indexers automatically.** `autoLBFrequency` (default: 30 seconds) and `autoLBVolume` (default: off) control when the forwarder switches to the next indexer in the list. Both conditions are evaluated together when `autoLBVolume` is non-zero — first threshold hit triggers the switch.
2. **Load balancing only switches at event boundaries or end-of-file.** For small, frequently-rotating files this is fine. For large, continuously growing files, the forwarder may never encounter a clean switch point — it "sticks" to one indexer regardless of the timer. This is the problem event breaking solves.
3. **`EVENT_BREAKER_ENABLE` / `EVENT_BREAKER` (UF-only `props.conf` settings) tell the UF where events end so it can switch cleanly.** These run on the UF before data is forwarded. They are NOT the same as `LINE_BREAKER` / `SHOULD_LINEMERGE`, which run on the indexer's parsing pipeline. Both can (and often should) coexist.
4. **Routing is two distinct things:**
   - **`_TCP_ROUTING`** (in `inputs.conf`) → points an input to a named output group in `outputs.conf` → controls which physical indexers receive the data.
   - **`_MetaData:Index`** (in `transforms.conf`) → dynamically re-assigns the destination index name on a per-event basis, regardless of which indexer it lands on.
5. **`nullQueue` drops events permanently.** `DEST_KEY = queue` / `FORMAT = nullQueue` in a `transforms.conf` stanza (referenced by `TRANSFORMS-<name>` in `props.conf`) discards matched events before indexing. Data dropped here is gone. It does not count against license.
6. **Default to UF for intermediate forwarding; only use HF when you specifically need parsing, masking, content-based routing, or HEC hosting at the intermediate tier.** UF = free, raw, low overhead. HF = license, cooked, heavier, but capable of transforms.

## Key terms (quick definitions)
- **`autoLBFrequency`** — seconds between indexer switches; default 30.
- **`autoLBVolume`** — bytes sent before switching; default 0 (off); triggers independently of frequency if set.
- **`EVENT_BREAKER_ENABLE`** — `props.conf` boolean, UF only; activates clean event-boundary switching.
- **`EVENT_BREAKER`** — `props.conf` regex, UF only; defines event boundary for LB switching (not parsing).
- **`LINE_BREAKER`** — `props.conf` regex on indexer; defines event boundaries for the parsing pipeline.
- **`SHOULD_LINEMERGE`** — set `false` when LINE_BREAKER defines boundaries; avoids slow line-merging.
- **`_TCP_ROUTING`** — `inputs.conf` attribute; routes an input to a named `[tcpout:<group>]` in outputs.conf.
- **`_MetaData:Index`** — transforms.conf DEST_KEY; re-assigns destination index dynamically per event.
- **`nullQueue`** — `FORMAT = nullQueue` in transforms.conf; permanently drops matched events.
- **Intermediate forwarder** — receives from UFs, forwards to indexers; reduces indexer-tier connection count.
- **`useACK`** — outputs.conf boolean; enables indexer acknowledgment for in-flight data protection.

## Watch for this in the video
- The diagram showing UFs load-balancing to multiple indexers — pay attention to the point where the instructor notes that load balancing breaks down for continuously growing files. That is the motivating problem for `EVENT_BREAKER`.
- The `autoLBFrequency` and `autoLBVolume` demonstration in `outputs.conf` — note that they are not mutually exclusive; both can be active simultaneously with first-wins behaviour.
- The `_TCP_ROUTING` example routing `/var/log/secure` to one indexer group and `/var/log/messages` to another — notice this is purely at the input stanza level, not based on event content.
- The `nullQueue` filtering example — note the `DEST_KEY = queue` / `FORMAT = nullQueue` pair and the fact that the regex in the transform stanza does the content matching, while the `props.conf` TRANSFORMS reference scopes it to a sourcetype or source.
- The UF vs HF comparison — the core argument is: UF is always preferred unless you need something only HF can provide (parsing, masking, HEC).

## Questions to hold in mind while watching
1. A high-volume syslog file is being monitored by a UF. `autoLBFrequency = 30` is set. After watching for 5 minutes you notice all events are landing on indexer 1. What is happening and what change do you make?
2. What is the difference between routing data to a specific indexer group (`_TCP_ROUTING`) and routing data to a specific index (`_MetaData:Index`)? Can you do both simultaneously?
3. If I want to drop all events from a noisy sourcetype before they are indexed, what two files do I edit and what is the exact key-value pair that drops the events?
4. An intermediate forwarder is a UF. A requirement comes in to mask credit card numbers before data hits the indexer. What do you need to change, and what is the cost?

## How this connects forward
- **`props.conf` + `transforms.conf` deep dive** — the routing and filtering mechanisms here (`_MetaData:Index`, `nullQueue`) are a preview of the full data onboarding pipeline.
- **Deployment Server** — in production, `outputs.conf` and `props.conf` changes on forwarders are pushed via Deployment Server app bundles; the config content is what this topic covers.
- **Indexer clustering** — in a clustered environment, the indexer groups in `outputs.conf` point to indexer peers; the load balancing model is the same.
- **Capacity planning** — the UF vs HF decision, the intermediate forwarder tier sizing, and the `maxQueueSize` buffer directly feed into hardware and network capacity decisions.

---

## Official references (for verification / deeper reading)

| Topic | Splunk Docs page |
|---|---|
| Set up load balancing | https://docs.splunk.com/Documentation/Splunk/latest/Forwarding/Setuploadbalancingd |
| outputs.conf reference | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Outputsconf |
| Route and filter data | https://docs.splunk.com/Documentation/Splunk/latest/Forwarding/Routeandfilterdatad |
| Configure event line breaking | https://docs.splunk.com/Documentation/Splunk/latest/Data/Configureeventlinebreaking |
| Configure an intermediate forwarder | https://docs.splunk.com/Documentation/Splunk/latest/Forwarding/Configureanintermediateforwarder |
| Types of forwarders | https://docs.splunk.com/Documentation/Splunk/latest/Forwarding/Typesofforwarders |
| Protect against loss of in-flight data (useACK) | https://docs.splunk.com/Documentation/Splunk/latest/Forwarding/Protectagainstlossofin-flightdata |
