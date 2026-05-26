---
type: pre-class
theme: 10-capstone-lab
topic: 1-distributed-buildout-components-forwarders
covers: "Lectures 54–58"
read_time: "~5 min"
tags: [study-guide/pre-class, theme/10-capstone-lab]
---

# Pre-class — Distributed Splunk Deployment: Components, Topology, and Forwarders

> Read before the material (covers lectures 54–58). ~5 min. The sessions walk a multi-instance build end to end at high speed — come in already holding the topology and the key config files so you can follow the decisions rather than just the clicks.

## Why this matters
A single Splunk instance is a toy. Real environments distribute work across specialized roles: indexers store data, search heads query it, forwarders ship it, and management components run the fleet. Understanding which role listens on which port, which config file wires them together, and how configuration gets pushed to hundreds of forwarders without SSH-ing into each one — that is what separates someone who can use Splunk from someone who can operate it. This section builds the complete picture from bare compute to verified data flow.

## The mental model (hold these)

1. **Every role is the same package, different config** (except UFs which use a lighter package). An indexer, search head, deployment server, and heavy forwarder all start from the same Splunk Enterprise `.tgz`. What you configure afterward determines the role.

2. **Three-tier data path: endpoints → ingest tier → indexing tier.** UFs on endpoints ship data to Intermediate Forwarders (relay UFs); IFs aggregate and forward to indexers. The HF sits on the ingest tier too, receiving network/syslog data that devices can't install agents on. Search heads query indexers; they don't touch the data path.

3. **Four config files wire the whole thing:**
   - `outputs.conf` — where does this node send data? (forwarders and any Splunk instance forwarding internal logs)
   - `inputs.conf` `[splunktcp://9997]` — is this indexer listening for incoming forwarded data?
   - `deploymentclient.conf` — which DS does this forwarder phone home to, and how often?
   - `serverclass.conf` (on the DS, managed via Forwarder Management UI) — which apps go to which clients?

4. **Automatic load balancing (`autoLB`) is built in.** List multiple targets in `outputs.conf`; Splunk rotates between them every 30 seconds by default. This is how UFs distribute data across two IFs and how IFs distribute across indexers — no external load balancer needed.

5. **Deployment Server = push, not pull.** Clients phone home (pull) to the DS on port 8089 at a configured interval. The DS then pushes any changed apps. You never push; clients initiate. Once a UF has its `deploymentclient.conf`, you manage it entirely from the DS — no more SSH per-host.

6. **Internal logs should go to the indexers.** Every Splunk component generates `_internal` logs. Forwarding these from the SH, DS, MC, and HF to the indexers lets you query platform health from the search head with `index=_internal | stats count by host`. If a component's host doesn't appear, forwarding is broken.

7. **Private IPs inside the cloud; public IPs across environments.** All intra-cloud communication (IF→indexer, DS→phone-home) uses private IPs — stable, no egress cost. A UF on a machine outside the cloud must use the public IP of the DS/IF, and the cloud security group/NSG must allow port 8089 (or 9997) from that external IP.

## Key terms (quick definitions)
- **Indexer** — receives forwarded data (port 9997) and serves search queries (port 8089).
- **Search Head** — user-facing queries; fans out searches to all indexers; Splunk Web on 8000.
- **Deployment Server** — centralized config-push; `deployment-apps/` on disk; Forwarder Management on 8000.
- **Universal Forwarder (UF)** — lightweight agent; monitors files/WinEventLog/scripts; no parsing.
- **Intermediate Forwarder (IF)** — UF acting as relay; aggregates from other UFs, sends to indexers.
- **Heavy Forwarder (HF)** — full Splunk Enterprise; can parse, mask, and route events; accepts network/syslog input.
- **`outputs.conf`** — defines forwarding target(s) and autoLB behavior.
- **`inputs.conf` `[splunktcp://9997]`** — enables receiving on indexer or IF.
- **`deploymentclient.conf`** — `targetUri = <DS_IP>:8089`; `phoneHomeIntervalInSecs`.
- **Server class** — DS construct mapping apps to a filtered set of clients.
- **`deployment-apps/`** — staging area on the DS; distinct from `etc/apps/`.

## Watch for this in the video
- The source environment uses AWS EC2 instances and Security Groups. The Splunk concepts are identical in any cloud or on-prem environment — only the IaaS console differs. A Security Group inbound rule is the same concept as an Azure NSG rule or an on-prem firewall ACL.
- Pay attention to which IP is used in each config file — the internal (private) IP appears in `outputs.conf` for intra-cloud forwarding, but the public IP is used when the Windows local-machine UF connects to the cloud DS. This is a practical decision, not a Splunk one.
- When `index=_internal | stats count by host` doesn't show a new host, the next debugging step is always: did you enable port 9997 on the indexer? The demo walks through this exact sequence.
- The `deployment-apps/` path on the DS is easy to miss. Apps you want deployed to clients go there, not in `etc/apps/`. Watch for the `scp`/copy step into that path.
- On Windows UF install, the wizard asks for the DS address — this writes `deploymentclient.conf` automatically. On Linux, you create that app manually.

## Questions to hold in mind while watching
1. What's the difference between a universal forwarder, an intermediate forwarder, and a heavy forwarder — and when does each get deployed?
2. How does a newly deployed UF "know" where the DS is, and how does the DS know the UF exists?
3. What is the minimum you need to configure on an indexer before a forwarder can successfully deliver data to it?
4. If I have 100 UFs and I need to change the destination indexer IP, how do I do it without touching each UF?
5. What would `index=_internal | stats count by host` tell me about a component that I suspect is not forwarding correctly?

## How this connects forward
- **Base apps pattern (Topic 10.2):** the deployment-server → server-class → app mechanism introduced here becomes the foundation for pushing standardized output, input, and TA configs to the entire fleet at scale.
- **Indexer clustering:** clustered indexers use a cluster manager (not the DS) for config distribution; the DS is not involved. Understanding the non-clustered DS pattern makes the clustered contrast sharp.
- **Data onboarding (`props.conf`/`transforms.conf`):** once data flows into an index, the next challenge is parsing it correctly. The HF introduced here is where parsing-at-the-edge happens for firewall logs.

---

## Official references

| Topic | Splunk Docs page |
|---|---|
| Distributed deployment overview | https://docs.splunk.com/Documentation/Splunk/9.4.0/Deploy/Searchheadwithindexers |
| Forwarder deployment topologies | https://docs.splunk.com/Documentation/Splunk/latest/Forwarding/Forwarderdeploymenttopologies |
| Types of forwarders | https://docs.splunk.com/Documentation/Splunk/9.3.1/Forwarding/Typesofforwarders |
| Configure the universal forwarder | https://docs.splunk.com/Documentation/Forwarder/9.4.0/Forwarder/Configuretheuniversalforwarder |
| Configure forwarding with outputs.conf | https://docs.splunk.com/Documentation/Forwarder/9.0.4/Forwarder/Configureforwardingwithoutputs.conf |
| Set up load balancing (autoLB) | https://docs.splunk.com/Documentation/Splunk/9.0.4/Forwarding/Setuploadbalancingd |
| About the deployment server | https://docs.splunk.com/Documentation/Splunk/9.4.0/Updating/Aboutdeploymentserver |
| Configure deployment clients | https://docs.splunk.com/Documentation/Splunk/9.4.1/Updating/Configuredeploymentclients |
| deploymentclient.conf reference | https://docs.splunk.com/Documentation/Splunk/9.4.2/Admin/Deploymentclientconf |
| Best practice: forward search head data to indexer layer | https://docs.splunk.com/Documentation/Splunk/9.2.5/DistSearch/Forwardsearchheaddata |
