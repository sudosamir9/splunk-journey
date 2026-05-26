# NBLM generation — Topic 10.2 · Base Apps, Forwarder Use Cases, Heavy Forwarder, and Firewall Log Ingestion

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Splunk base-apps pattern, forwarder use cases, Heavy Forwarder deployment, and firewall syslog ingestion`
- **KEY DISTINCTIONS:** `the base-apps pattern (outputs base, inputs/receive base, TA/use-case app) and server class naming; activating TA stanzas by copying default/ to local/ and setting disabled=false + index=; allowlist/denylist in inputs.conf (9.x names, denylist wins, replaces whitelist/blacklist); when to use a Heavy Forwarder vs Universal Forwarder (network input, parsing, routing, masking, agentless devices); deploying 3 apps to the HF via DS (outputs, inputs/network, TA); udp://port network input stanza with connection_host=ip; sourcetype as the props.conf lookup key; CIM normalization (srcip→src_ip) and its role in ES correlation; the TA's three deployment locations (HF for parsing, indexer for index-time fields, SH for search-time KOs)`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on three interconnected topics: (1) the base-apps pattern for managing
forwarder configuration at scale through the deployment server — what a base app is, the
three categories (outputs, inputs/receive, TA/use-case), server class naming conventions,
and the end-to-end workflow for deploying a TA with a modified local/inputs.conf; (2) real
forwarder use cases — activating Linux file monitoring, Windows WinEventLog collection, and
scripted inputs by copying default/ to local/ and setting disabled=false with the correct
index= and sourcetype=, including the allowlist/denylist filtering mechanism; (3) the Heavy
Forwarder — why it's needed for devices that can't install agents, the three apps you push
to it via the DS (outputs, network input, vendor TA), the complete UDP syslog input stanza
for receiving FortiGate logs, and the end-to-end path from firewall CLI config to indexed
CIM-normalized events on the search head.

Go deep on: why sourcetype is not just a label but the key that triggers props.conf parsing
rules; why the TA must be on the HF AND the search head for CIM-based searches to work;
what CIM normalization means in practice (srcip→src_ip) and why it matters for ES; why you
never edit default/ even in a deployment-apps/ staged TA; the allowlist/denylist precedence
and the 9.x rename from whitelist/blacklist; and how splunk reload deploy-server avoids a
full restart when adding apps. Walk through a complete scenario: FortiGate to HF to Indexer 2
to search head, calling out each configuration file and where it lives. Near the end, pose
a few drill questions. Aim for a thorough episode of roughly 25–30 minutes — go deep enough
to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of the base-apps
deployment pattern, forwarder use cases, Heavy Forwarder configuration, and firewall syslog
ingestion at a Splunk administrator level. Mix recall with scenario questions (a Linux TA is
deployed but index=linux returns nothing — list three possible causes; write the inputs.conf
stanza for UDP syslog on port 5555; which three locations need the TA for CIM searches to
work?; why can't a UF receive FortiGate syslog?; what does connection_host=ip do?; what
breaks if sourcetype is wrong?). Target: base-app naming, default-vs-local in TAs, inputs.conf
stanza attributes, allowlist/denylist, HF vs UF choice, network input config, CIM normalization,
TA deployment locations. Explain each answer.
```

## Flashcards
```
Make flashcards on the Splunk base-apps pattern, forwarder use cases, Heavy Forwarder, and
firewall log ingestion. Front = term/scenario/config snippet; back = precise answer or rule.
Include: base app categories, server class naming, default-vs-local in TAs, inputs.conf
monitor stanza key attributes (disabled, index, sourcetype, allowlist, denylist), WinEventLog
stanza format, scripted input interval, HF vs UF decision criteria, [udp://port] stanza
attributes, connection_host values, TA deployment locations (HF/indexer/SH), CIM field mapping
examples, splunk reload deploy-server command.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
