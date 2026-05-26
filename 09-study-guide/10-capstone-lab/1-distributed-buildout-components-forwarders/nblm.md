# NBLM generation — Topic 10.1 · Distributed Splunk Deployment: Components, Topology, and Forwarders

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Distributed Splunk deployment — components, topology, and forwarder wiring`
- **KEY DISTINCTIONS:** `the seven component roles (indexer, search head, DS, LM, MC, HF, UF/IF) and what each does; the three-tier data path (endpoints → ingest tier → indexing tier); port requirements (8000/8089/9997/22/syslog) and why private vs public IPs matter; outputs.conf autoLB to multiple targets; inputs.conf splunktcp receiving; deploymentclient.conf phone-home; deployment-apps/ vs apps/ on the DS; server classes mapping apps to clients; the IF as relay vs HF for parsing; forwarding internal logs to make platform health searchable`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on building a distributed Splunk environment from scratch: the component
roles (indexer, search head, deployment server, license manager, monitoring console, heavy
forwarder, universal forwarder, intermediate forwarder), the three-tier data path from
endpoints through an ingest tier to indexers to the search head, and how you wire it all
together with the four key config files (outputs.conf, inputs.conf for splunktcp receiving,
deploymentclient.conf, and server classes on the deployment server).

Go deep on: why intermediate forwarders exist (geography, bandwidth, fault isolation, data
masking) and why they are UFs not HFs; the autoLB mechanism in outputs.conf and what
autoLBFrequency actually means operationally; the phone-home model of the deployment server
(clients pull, DS pushes) and why deployment-apps/ is distinct from apps/; the reason all
non-indexer components should forward internal logs to the indexers and how to verify with
index=_internal; the private-IP-vs-public-IP rule for intra-cloud vs cross-environment
connections; and the port matrix (9997, 8089, 8000, 22) with direction and purpose.

Walk through a concrete topology: UFs load-balancing across two IFs, IFs forwarding to
Indexer 1, a Heavy Forwarder receiving syslog and forwarding to Indexer 2, the search head
distributed-searching both indexers, and the DS pushing configs to the whole fleet. Call out
the common failure modes: forgetting to enable splunktcp receiving on the indexer; using
private IPs for cross-environment connections; putting apps in the wrong directory on the DS.
Near the end, pose a few drill questions so the listener can self-check. Aim for a thorough
episode of roughly 25–30 minutes — go deep enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of building and
operating a distributed Splunk deployment at an administrator level. Mix recall with scenario
questions (a UF doesn't appear in index=_internal — what are three possible causes and how
do you diagnose each?; write the outputs.conf for a UF load-balancing across two IFs; which
IP goes in deploymentclient.conf if the DS is in the cloud and the UF is on a local machine?;
what's the difference between deployment-apps/ and apps/ on the DS?; when do you use a Heavy
Forwarder instead of an intermediate forwarder?). Target: component roles, port matrix,
outputs.conf autoLB, inputs.conf receiving, deploymentclient.conf, server classes,
internal-log forwarding, private vs public IPs. Explain each answer.
```

## Flashcards
```
Make flashcards on distributed Splunk deployment components and forwarder wiring. Front =
term/scenario/config snippet; back = definition, purpose, or the correct answer. Include:
component roles and their ports, outputs.conf autoLB pattern, inputs.conf splunktcp receiving
stanza, deploymentclient.conf key attributes, deployment-apps/ vs apps/, server class purpose,
why IFs exist, HF vs UF distinction, private vs public IP rule, index=_internal verification.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
