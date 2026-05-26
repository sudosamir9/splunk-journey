# NBLM generation — Topic 09.2 · Data Inputs: Network, Scripted, and HTTP Event Collector

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Splunk network inputs, scripted inputs, and the HTTP Event Collector (HEC)`
- **KEY DISTINCTIONS:** `TCP/UDP network inputs ([udp://] / [tcp://]) and connection_host (ip/dns/none); queueSize vs persistentQueueSize; why direct syslog on an indexer is an anti-pattern (use HF/SC4S); scripted inputs ([script://]), interval (seconds or cron), bin/ directory requirement, stdout=events; modular inputs as the modern alternative; HEC port 8088, bearer token model, two endpoints (event vs raw), [http] global stanza vs [http://<name>] per-token stanza, allowedIndexes; indexer acknowledgement (ackEnabled, ackId polling); HEC vs UF decision; HEC in distributed deployments`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on three non-file Splunk input types: network inputs, scripted inputs,
and the HTTP Event Collector. For network inputs: cover the [udp://] and [tcp://] stanzas,
the critical connection_host attribute (ip/dns/none — and why ip is almost always right for
syslog), queueSize vs persistentQueueSize for flow control, and explain clearly why
receiving raw syslog directly on an indexer is an anti-pattern at scale — including the
preferred Heavy Forwarder / SC4S architecture in front. For scripted inputs: the
[script://] stanza, interval as seconds or cron, the bin/ directory requirement, that
stdout is indexed and stderr goes to splunkd.log, the OS user the script runs as and the
security implications, and when to reach for a modular input instead. For HEC: what it is
(token-authenticated HTTP/HTTPS endpoint on port 8088), the bearer token model
(Authorization: Splunk <token>), the two endpoints (/services/collector/event for JSON with
per-event metadata override vs /services/collector/raw for plain text), the [http] global
stanza vs [http://<name>] per-token stanza, allowedIndexes for routing control, how
indexer acknowledgement works (ackEnabled, the ackId two-phase flow), and the HEC vs UF
decision framework (HEC for agentless/cloud/app-level; UF for file-based OS logs). Close
with the recommended HEC distributed architecture (HF pool + LB). Call out the classic
mistakes: direct syslog on indexers, sharing a single token, using HEC without TLS,
assuming fire-and-forget HEC is reliable. Aim for a thorough episode of roughly 25–30
minutes — go deep enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of Splunk network,
scripted, and HEC inputs at an administrator level. Mix recall with scenario questions:
which connection_host value is appropriate when DNS is unreliable?; what happens to UDP
syslog events during a 30-second indexer outage?; a script writes its data to stderr —
where does it end up?; a developer shares one HEC token across 20 applications — what
problems does this create?; you need guaranteed delivery for compliance events over HEC —
which feature and what client-side workflow? Cover: connection_host values, queue/persistent
queue mechanics, scripted input location and execution user, modular vs scripted,
HEC token model and allowedIndexes, indexer acknowledgement flow, HEC vs UF tradeoffs.
Explain each answer.
```

## Flashcards
```
Make flashcards on Splunk network inputs, scripted inputs, and HEC. Front = term,
attribute, or scenario; back = a tight rule or definition. Include: connection_host values
(ip/dns/none) and when to use each; queueSize vs persistentQueueSize; why direct syslog
on an indexer is an anti-pattern; scripted input stanza format and bin/ requirement;
interval as seconds vs cron; modular input advantages; HEC port and auth header format;
/event vs /raw endpoint difference; [http] vs [http://<name>] stanza; allowedIndexes;
ackEnabled two-phase flow; HEC vs UF decision rule.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
