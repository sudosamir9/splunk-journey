# NBLM generation — Topic 08.1 · Deployment Server, Clients & Server Classes

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Splunk Deployment Server, deployment clients, and server classes`
- **KEY DISTINCTIONS:** `the pull model (client phones home to DS on port 8089; DS never initiates); deployment-apps/ on the DS vs. apps/ on the client; the three components — deployment client (deploymentclient.conf, targetUri, phoneHomeIntervalInSecs), deployment app (config bundle in deployment-apps/), server class (serverclass.conf — whitelist/allowlist + blacklist/denylist filters, stateOnClient, restartSplunkd); the reload deploy-server trigger; DS vs. cluster manager vs. SHC deployer — what each manages and why they cannot substitute for each other; sizing (>50 clients = dedicated DS; single DS up to ~10K; DS cluster 9.2+ up to 75K)`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on the Splunk Deployment Server, deployment clients, and server classes.
Go deep on the pull model: why the client initiates every contact (never the DS), what
happens on each phone-home cycle (checksum comparison, selective download, optional restart),
and what the firewall implication is. Explain the three moving parts — deployment client
(deploymentclient.conf, the target-broker:deploymentServer stanza, targetUri, phoneHomeIntervalInSecs),
deployment app (a config bundle in $SPLUNK_HOME/etc/deployment-apps/ on the DS), and server
class (serverclass.conf — whitelist/allowlist and blacklist/denylist filters, stateOnClient,
restartSplunkd). Walk through the directory model: deployment-apps/ on the DS is the source;
apps/ on the client is the destination — they are not the same path. Explain the reload
deploy-server trigger and why an app drop into deployment-apps/ does nothing until that
command runs.

Contrast the DS sharply with the cluster manager (manages indexer peers via master-apps/
and a push) and the SHC deployer (manages SHC members via a push) — explain why you must
never use the DS for clustered components. Cover the base-outputs pattern as the canonical
first use case. Address sizing: when a DS must be dedicated, the rough single-DS ceiling,
and the DS cluster option in 9.2+.

Keep it concrete — walk a full phone-home cycle from the moment the UF wakes up to the
moment an app lands in its etc/apps/. Pose a few drill questions near the end so the
listener can self-check. Energetic and conversational, but dense and precise — this is
learning, not entertainment. Aim for a thorough episode of roughly 25–30 minutes — go
deep enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of the Splunk
Deployment Server and server classes at an administrator level. Mix recall with scenario
questions: given a serverclass.conf snippet with whitelist/blacklist patterns, which
clients match?; a client is not appearing in Forwarder Management — what are the
diagnostic steps?; you update a deployment app and nothing happens — what must occur?;
why can't you use the DS for indexer cluster peers? Target: the pull model mechanics,
deploymentclient.conf stanzas and attributes, the deployment-apps/ vs. apps/ distinction,
serverclass.conf structure and filter matching, stateOnClient values, reload deploy-server,
and DS vs. cluster manager vs. deployer. Explain each answer.
```

## Flashcards
```
Make flashcards on the Splunk Deployment Server, deployment clients, and server classes.
Front = term/scenario; back = a tight definition, rule, or stanza. Include: the pull model
(who initiates, what port, what is exchanged); deploymentclient.conf key stanzas and
attributes (target-broker:deploymentServer, targetUri, phoneHomeIntervalInSecs); the
deployment-apps/ vs. apps/ directory distinction; serverclass.conf filter attributes
(whitelist/allowlist, blacklist/denylist, stateOnClient values, restartSplunkd); reload
deploy-server purpose; DS vs. cluster manager vs. SHC deployer; the base-outputs pattern;
sizing thresholds (50-client dedicated rule, single-DS ceiling, DS cluster).
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
