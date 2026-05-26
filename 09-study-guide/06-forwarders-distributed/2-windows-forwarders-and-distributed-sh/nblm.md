# NBLM generation — Topic 06.2 · Windows Forwarders, Technology Add-ons, and Distributed Search

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Windows Universal Forwarder, technology add-on split-tier deployment, and distributed search architecture`
- **KEY DISTINCTIONS:** `Windows UF MSI install (wizard screens, service account, silent install properties); WinEventLog input stanza (channel names, disabled=0, renderXml=true, XmlWinEventLog sourcetype); technology add-on anatomy (inputs + props + transforms + knowledge); split-tier TA deployment (inputs.conf on UF, props/transforms on indexer, all+search-time knowledge on search head — and why each tier needs its part); dedicated search head model (no local data, dispatch to search peers); three ways to add search peers (Web, CLI, distsearch.conf); knowledge bundle replication (what it contains, why peers need it, where it lives); map-reduce search flow; distsearch.conf structure; quarantine mode; port 8089 vs 9997 distinction`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on two significant topics: first, the Windows Universal Forwarder and the
Splunk Add-on for Windows — then the distributed search architecture. Go deep on both.

For Windows forwarders and the TA: explain how the Windows UF is installed (MSI, service
account, wizard screens for receiving indexer and deployment server, silent install with
msiexec); why Windows Event Logs are different from Linux file logs and how the
[WinEventLog://<channel>] input stanza works; the main channels (Security, System,
Application); renderXml=true and why it matters; and then go deep on the split-tier TA
deployment pattern — what a technology add-on contains (inputs.conf for collection +
props.conf/transforms.conf for parsing + search-time knowledge), why it must be deployed
to the UF, indexer, AND search head simultaneously with different parts active on each,
and what breaks if you skip a tier.

For distributed search: explain what a dedicated search head is (no local data, pure
dispatch-and-merge node), how it connects to indexer search peers via the management port
(8089 not 9997), the three methods to add search peers (Web, CLI, distsearch.conf), what
distsearch.conf looks like, the knowledge bundle (what it contains, why it must be replicated
to peers, where it lives), the map-reduce search flow (peers search locally, SH merges
results), quarantine mode, and why you'd run multiple search heads.

Connect the two halves: the search head needs the TA deployed on it for search-time field
extractions to work; the indexer needs it for index-time parsing; the UF needs it for
collection. Show how the full three-tier architecture (UF → indexer → search head) fits
together.

Keep it concrete — walk through configuration examples, explain the port numbers (9997 vs
8089), and call out common confusions (search head has no data; TA must be on all tiers;
8089 not 9997 for peer registration). Near the end, pose a few of the drill questions so
the listener can self-check. Energetic and conversational, but dense and precise — this is
learning, not entertainment. Aim for a thorough episode of roughly 25–30 minutes — go deep
enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of Windows Universal
Forwarder deployment, the Splunk Add-on for Windows split-tier pattern, and distributed
search architecture. Mix recall with scenario questions (given an architecture diagram, which
tier needs which part of the TA; what breaks if you skip deploying the TA on the indexer;
where does data come from when a search head searches index=windows). Target: Windows UF
install (MSI, service account), WinEventLog input stanza, renderXml, split-tier TA pattern,
dedicated search head model, adding search peers (Web/CLI/distsearch.conf), knowledge bundle
contents and replication, map-reduce search flow, port 8089 vs 9997, quarantine mode. Explain
each answer.
```

## Flashcards
```
Make flashcards on Windows UF deployment, the Splunk Add-on for Windows split-tier pattern,
and distributed search architecture. Front = term/scenario; back = a tight definition or
correct configuration. Include: WinEventLog stanza format, renderXml=true effect, split-tier
TA pattern (what goes where), dedicated SH definition, knowledge bundle definition, distsearch.conf
structure, add-search-server CLI command, port 8089 vs 9997 distinction, quarantine mode
definition, splunk_server field purpose.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
