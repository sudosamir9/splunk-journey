---
type: pre-class
theme: 10-capstone-lab
topic: 2-base-apps-usecases-hf-firewall
covers: "Lectures 59–61"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/10-capstone-lab]
---

# Pre-class — Base Apps, Forwarder Use Cases, Heavy Forwarder, and Firewall Log Ingestion

> Read before the material (covers lectures 59–61). ~4–5 min. These sessions move through several distinct concepts quickly — base apps, use-case TAs, the HF, and syslog ingestion. Walk in with the mental model so you're following the decisions, not just watching clicks.

## Why this matters
Having a fleet of UFs registered to a DS is the plumbing. The content — which apps and configurations you push, to which hosts, with what inputs — is where the operational value lives. This section covers the full cycle: designing a base-app structure, activating real data collection use cases on Linux and Windows UFs, and solving the specific problem of getting data from a device that can never run an agent (a firewall). If you understand these patterns you can onboard almost any data source in a distributed environment.

## The mental model (hold these)

1. **The base-apps pattern is just naming discipline.** Three categories of apps cover almost everything: an outputs base app (where does this host send data?), an inputs/receive base app (is this host listening for incoming data?), and use-case/TA apps (what data does this host collect and where does it go?). One server class per host class, named descriptively. This scales to hundreds of hosts.

2. **TAs ship disabled — you activate them.** A TA's `default/inputs.conf` has nearly every stanza set to `disabled = true`. You copy the stanzas you want into `local/inputs.conf`, set `disabled = false`, add `index = <your_index>`, and leave `default/` untouched. The DS then pushes the modified TA. The `local/` directory pattern applies here just like everywhere else in Splunk.

3. **`sourcetype` is not just a label — it's the parsing key.** Whatever `sourcetype` you set in `inputs.conf` is what `props.conf` uses to look up timestamp extraction, line merging, and field extraction rules. Set it wrong and the TA's rules never fire. For vendor TAs, the expected sourcetype is documented in the TA's README.

4. **Indexes must exist before data arrives.** Create custom indexes (`windows`, `linux`, `fortinet`, etc.) on the receiving indexer before deploying the UF input apps. Events targeting a non-existent index fall back to `main` or are dropped. Creating the index first avoids this.

5. **The Heavy Forwarder is the gateway for devices that cannot install agents.** Firewalls, routers, switches — these send syslog (UDP/TCP port 514 or custom). The HF receives it via a `[udp://...]` or `[tcp://...]` stanza in `inputs.conf`. From there it processes the data through the vendor TA and forwards it to the indexer. Deployed and managed through the DS like any other forwarder — but it runs full Splunk Enterprise, not the UF package.

6. **The TA has three homes: HF (parsing), indexer (index-time fields), search head (search-time KOs).** For CIM-based searches (especially ES) to work, the TA's `eventtypes.conf` and `tags.conf` must be visible on the search head. Deploying the TA only to the HF gets you raw parsed events, not CIM-normalized searches. Install the TA on the SH (and optionally the indexer for index-time routing/masking) to complete the picture.

## Key terms (quick definitions)
- **Base app** — a DS-pushed app providing standardized minimal config to a class of forwarders.
- **Server class** — DS mapping of apps to a client filter (hostname wildcard); the deployment unit.
- **TA (Technology Add-on)** — app from Splunkbase; provides `props.conf`, `transforms.conf`, `eventtypes`, `tags` for a specific data source.
- **`disabled = false` / `disabled = 0`** — activates an `inputs.conf` stanza; TAs ship with most stanzas disabled.
- **`index = <name>`** — destination index for events; must exist on the indexer.
- **`allowlist` / `denylist`** — filter which files in a monitored directory are collected (9.x names; replaced `whitelist`/`blacklist`).
- **Heavy Forwarder** — full Splunk Enterprise in forwarding mode; needed for network input, index-time parsing, routing, masking.
- **`[udp://5555]`** — HF network input for syslog; `connection_host=ip` sets host to sender's IP.
- **CIM** — Common Information Model; normalizes field names across vendors (`srcip` → `src_ip`); powers ES correlation.
- **`splunk reload deploy-server`** — reloads DS server classes without restart; triggers re-deployment to clients.

## Watch for this in the video
- The source environment is AWS-based. The Splunk configuration concepts (apps, server classes, `inputs.conf`, `outputs.conf`, `deploymentclient.conf`) are cloud-independent. Only the IaaS console steps differ.
- When the TA's `default/inputs.conf` is copied to `local/` and edited — this is the `default`-vs-`local` rule in action inside a deployment app. The pattern is the same whether you're in `etc/apps/` on a live instance or staging an app in `deployment-apps/` on the DS.
- Pay attention to the sequence: create the index on the indexer first, then deploy the TA with `index=<name>`. Reversing this order causes data to land in the wrong index.
- For the FortiGate flow: there are three distinct "where does the TA go" steps — on the HF (parsing at the edge), the indexer is receiving the already-parsed data, and the SH needs the TA's knowledge objects for CIM searches. The sessions may not make all three explicit.
- The custom port for syslog (5555 vs standard 514) is a practical choice to avoid conflicts with OS-level syslog daemons. Both work identically in Splunk's `inputs.conf`.

## Questions to hold in mind while watching
1. When the Linux TA stanzas are copied from `default/` to `local/`, why is that necessary — what would break if you edited `default/` instead?
2. What is the minimum `inputs.conf` change needed to activate a TA monitoring stanza correctly (beyond just setting `disabled = false`)?
3. What makes a Heavy Forwarder necessary for the FortiGate use case, and why can't a UF do the same job?
4. After deploying three apps to the HF via the DS, how do you verify they actually landed on the HF?
5. What would you see in `index=fortinet` immediately after the HF is configured and the firewall starts sending? What would be wrong if you see raw, unparsed events?

## How this connects forward
- **Data onboarding (`props.conf` / `transforms.conf`):** the TA does this work for you when a vendor TA exists. When there is no TA, you write `props.conf` and `transforms.conf` manually — the mechanics are identical; you're just doing what the TA author did.
- **Splunk Enterprise Security:** CIM normalization introduced here is the prerequisite for ES. Every correlation search joins data via CIM-normalized fields. Getting a TA correctly deployed — on HF, indexer, and SH — is an ES admin prerequisite, not just a nice-to-have.
- **Indexer clustering:** in a clustered environment, TA updates to indexers go through the cluster manager's bundle, not the DS. Understanding the non-clustered pattern first makes the distinction clear.

---

## Official references

| Topic | Splunk Docs page |
|---|---|
| About the deployment server | https://docs.splunk.com/Documentation/Splunk/9.4.0/Updating/Aboutdeploymentserver |
| Forwarder management overview | https://docs.splunk.com/Documentation/Splunk/9.4.0/Updating/Forwardermanagementoverview |
| Use serverclass.conf to define server classes | https://docs.splunk.com/Documentation/Splunk/9.4.1/Updating/Useserverclass.conf |
| serverclass.conf reference | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Serverclassconf |
| Monitor files and directories with inputs.conf | https://docs.splunk.com/Documentation/Splunk/9.2.1/Data/Monitorfilesanddirectorieswithinputs.conf |
| Include or exclude specific incoming data (allowlist/denylist) | https://docs.splunk.com/Documentation/Splunk/9.4.0/Data/Whitelistorblacklistspecificincomingdata |
| Get data from TCP and UDP ports (syslog) | https://docs.splunk.com/Documentation/Splunk/latest/Data/Monitornetworkports |
| Types of forwarders (HF vs UF) | https://docs.splunk.com/Documentation/Splunk/9.3.1/Forwarding/Typesofforwarders |
| Route and filter data (HF routing) | https://docs.splunk.com/Documentation/Splunk/9.2.0/Forwarding/Routeandfilterdatad |
| CIM overview | https://docs.splunk.com/Documentation/CIM/6.1.0/User/Overview |
| inputs.conf reference | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Inputsconf |
