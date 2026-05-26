---
type: pre-class
theme: 08-deployment-server
topic: deployment-server-and-server-classes
covers: "Lectures 44–45"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/08-deployment-server]
---

# Pre-class — Deployment Server, Clients & Server Classes

> Read before the video (covers lectures 44–45). ~4–5 min. The lectures move fast through the config files and UI steps — walk in already holding the model so you can focus on the mechanics rather than building the mental picture from scratch.

## Why this matters
As soon as you have more than a handful of forwarders, touching `deploymentclient.conf` or `outputs.conf` on each one individually stops being viable. The Deployment Server (DS) is Splunk's answer: one instance that holds all your forwarder config bundles, with a declarative mapping that says "these clients get these apps." Understand this and you can manage thousands of forwarders centrally. Miss it and you're doing manual config surgery on every endpoint.

## The mental model (hold these)

1. **It is a pull model, not a push.** The DS never reaches out to clients. Each deployment client polls the DS on port 8089 at a configured interval (default 60 s), compares checksums, and downloads only what has changed. The DS is passive; the clients drive.

2. **Three moving parts — client config, app bundle, mapping.** A deployment client is any Splunk instance with `deploymentclient.conf` pointing at the DS. A deployment app is a config directory placed under `$SPLUNK_HOME/etc/deployment-apps/` on the DS. A server class is a named policy in `serverclass.conf` that binds a filter (which clients match) to a set of apps (what they receive).

3. **`deployment-apps/` (DS source) ≠ `apps/` (client destination).** Apps live in `deployment-apps/` only on the DS. When a client downloads an app, it lands in the client's `etc/apps/` — a normal app from that point forward, subject to the standard conf layering rules.

4. **`serverclass.conf` is the mapping layer.** At its simplest: `whitelist.0 = *` gives an app to every client. More specific patterns (`whitelist.0 = linux-*`, `blacklist.0 = linux-test-*`) give you surgical control. Three key per-app options: `stateOnClient` (enabled/disabled/noop), `restartSplunkd` (restart after deploy?), `restartIfNeeded` (restart only if required).

5. **`reload deploy-server` is the trigger.** Dropping an app into `deployment-apps/` or editing `serverclass.conf` on disk does nothing until you run `splunk reload deploy-server` (or the UI does it for you). No DS restart needed — it is a live reload.

6. **The DS is for forwarders and standalone instances — not cluster members.** Indexer cluster peers are managed by the cluster manager; SHC members are managed by the SHC deployer. Using the DS for clustered components creates conflicts.

## Key terms (quick definitions)

- **Deployment Server (DS)** — a Splunk instance that serves config bundles to deployment clients over port 8089. Must be dedicated if > 50 clients.
- **Deployment client** — any Splunk instance configured with `deploymentclient.conf` (stanza `[target-broker:deploymentServer]`, attribute `targetUri = <DS>:8089`) to poll the DS.
- **Deployment app** — a config bundle (app directory) in `$SPLUNK_HOME/etc/deployment-apps/` on the DS.
- **Server class** — a named mapping in `serverclass.conf` linking a set of clients (by filter) to a set of apps.
- **`phoneHomeIntervalInSecs`** — how often the client contacts the DS. Default: 60. Tune up for large deployments.
- **`stateOnClient`** — whether the DS-pushed app is `enabled`, `disabled`, or `noop` on the client.
- **`splunk reload deploy-server`** — tells the DS to re-read its config and rescan `deployment-apps/`; no restart.
- **Forwarder Management UI** — `Settings → Forwarder Management`; graphical front-end for server class management; writes `serverclass.conf`.

## Watch for this in the video

- The step of copying an app into `deployment-apps/` and then changing ownership (`chown -R splunk:splunk`) on Linux — both are required before the DS can serve the app.
- `deploymentclient.conf` being placed inside an app under `etc/apps/` on the UF — this is cleaner than editing `system/local/` directly, and it is the pattern the video uses.
- The Forwarder Management UI going from "no clients or apps" to showing connected UFs once the `deploymentclient.conf` is in place and the UF is restarted — that first phone-home is the activation event.
- Creating two server classes with different client filters: one using `*` (all clients) and one using a specific name prefix — notice how a single UF can match more than one server class and receive apps from each.
- `btool deploymentclient list --debug` on the UF to confirm the DS address took effect.

## Questions to hold in mind while watching

1. If a client already has the app and the checksum matches, what happens at phone-home? What if the checksum differs?
2. What is the difference between `deployment-apps/` on the DS and `apps/` on the client?
3. A client matches two server classes — how many apps can it receive, and what controls that?
4. After editing `serverclass.conf` directly on disk, what is the minimum action needed before clients get the change?

## How this connects forward

- **Indexer clustering (theme 09)** — the cluster manager's `master-apps/` follows a similar pattern (bundle directory + apply command) but is a push, not a pull. Understanding DS pull vs. CM push is a useful contrast.
- **SHC deployer (theme 10)** — another bundle-push mechanism, again with its own dedicated directory and apply command (`splunk apply shcluster-bundle`), and again distinct from the DS.
- **Data onboarding (theme 11)** — `inputs.conf` pushed via a DS deployment app is exactly how forwarder inputs are managed in practice. The conf layering model from theme 03 applies: the app-pushed `local/inputs.conf` sits in the client's `apps/<app>/local/` and follows normal precedence.
- **Forwarder architecture (theme 07)** — the `outputs.conf` base-app pattern connects directly: the DS is the mechanism that gets `outputs.conf` onto every UF without touching each one.

---

## Official references (for verification / deeper reading)

| Topic | Splunk Docs page |
|---|---|
| About deployment server and forwarder management | https://docs.splunk.com/Documentation/Splunk/latest/Updating/Aboutdeploymentserver |
| Deployment server architecture | https://docs.splunk.com/Documentation/Splunk/latest/Updating/Deploymentserverarchitecture |
| Configure deployment clients | https://docs.splunk.com/Documentation/Splunk/latest/Updating/Configuredeploymentclients |
| `deploymentclient.conf` reference | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Deploymentclientconf |
| Use `serverclass.conf` to define server classes | https://docs.splunk.com/Documentation/Splunk/latest/Updating/Useserverclass.conf |
| `serverclass.conf` reference | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Serverclassconf |
| Set up client filters | https://docs.splunk.com/Documentation/Splunk/latest/Updating/Filterclients |
| Deploy apps to clients (`reload deploy-server`) | https://docs.splunk.com/Documentation/Splunk/latest/Updating/Updateconfigurations |
| Use forwarder management to define server classes | https://docs.splunk.com/Documentation/Splunk/latest/Updating/Useforwardermanagement |
| Estimate deployment server performance (sizing) | https://docs.splunk.com/Documentation/Splunk/latest/Updating/Calculatedeploymentserverperformance |
| Implement a deployment server cluster (9.2+) | https://docs.splunk.com/Documentation/Splunk/latest/Updating/Implementascalabledeploymentserversolution |
