---
type: enhanced
theme: 09-data-inputs
topic: 2-network-scripted-hec-inputs
covers: "Lectures 51–53"
tags: [study-guide/enhanced, theme/09-data-inputs]
sources: docs.splunk.com (Splunk 9.x / latest, 2026)
---

# Data Inputs: Network, Scripted, and HTTP Event Collector

> Deep reference on three non-file input types: network inputs (TCP and UDP port listeners), scripted inputs (scheduled script execution), and the HTTP Event Collector (HEC). Covers real `inputs.conf` stanzas, the architectural trade-offs for each, security considerations, and the complete HEC token model including indexer acknowledgement and distributed deployment. Companion `pre-class.md` holds the short primer and official-doc links.

---

## 0. Orientation

When data cannot be read from a local file — because the source is a network device, a third-party API, or an application that cannot run a forwarder — Splunk provides input types that receive data from the outside rather than pulling it from disk. The three types covered here each solve a different problem:

- **Network (TCP/UDP)** — receive raw streams or datagrams on a port; the classic syslog collection model.
- **Scripted** — run a program on a schedule and index its standard output; the general-purpose "I can write a script" model.
- **HEC** — expose an HTTP/HTTPS endpoint that any HTTP-capable client can POST events to; the agentless, cloud-friendly, token-authenticated model.

Understanding when to use each, and how to configure each correctly, is central to designing a real Splunk data pipeline.

---

## 1. Network inputs

### 1.1 TCP and UDP stanzas

```ini
[tcp://<port>]
[udp://<port>]
```

Both accept connection-based (TCP) or datagram-based (UDP) data on the specified port. The most common use case is **syslog**:

- Syslog over **UDP 514** — the traditional, near-universal network device log format
- Syslog over **TCP** — used when reliability matters (firewalls, proxies configured for TCP syslog)
- Custom port — any port you choose; the network device just needs to match

```ini
# UDP syslog listener for firewall logs
[udp://514]
index           = network
sourcetype      = syslog
connection_host = ip
disabled        = false

# TCP syslog on a non-standard port with buffer
[tcp://6514]
index           = network
sourcetype      = syslog
connection_host = dns
queueSize       = 10MB
disabled        = false
```

### 1.2 Key attributes for network inputs

| Attribute | Values | Meaning |
|---|---|---|
| `index` | index name | Destination index |
| `sourcetype` | string | Sourcetype for events |
| `source` | string | Overrides the `source` field (default: port-based) |
| `host` | string | Static host override |
| `connection_host` | `ip` / `dns` / `none` | How to derive the `host` field from the incoming connection |
| `disabled` | true/false | Enable or disable the input |
| `queueSize` | e.g., `500KB`, `10MB` | In-memory buffer size for the port; default `500KB` |
| `persistentQueueSize` | e.g., `100MB` | Disk-based overflow queue; prevents event loss when memory queue is full |

### 1.3 `connection_host` — how the host field is set

The `connection_host` attribute controls how Splunk derives the `host` metadata field for events arriving on a network port:

- **`ip`** — uses the **IP address** of the sending host. Reliable; works when no DNS is available. Default for most deployments.
- **`dns`** — performs a **reverse DNS lookup** on the sender's IP. Useful when you want FQDNs in your data, but adds latency and depends on DNS reliability. If the lookup fails, Splunk falls back to the IP.
- **`none`** — the `host` is set to whatever value is in the `host` attribute in the stanza (a static string). If no `host` attribute is set, it falls back to the receiving machine's hostname — which is almost never what you want for network data.

In most syslog collection scenarios, `connection_host = ip` is the correct choice. The IP can always be enriched later with a lookup table; a missing or wrong hostname is much harder to recover.

### 1.4 Queue sizing and flow control

UDP is connectionless and fire-and-forget. When a Splunk listener receives UDP traffic faster than it can process it (or when the indexer is temporarily unreachable), packets are dropped — **UDP has no retransmission**. TCP has retransmission at the protocol level, but the Splunk TCP input's in-memory queue can still overflow.

`queueSize` sets the **in-memory** input buffer. When it fills, new incoming data is dropped (for UDP) or causes backpressure (for TCP).

`persistentQueueSize` configures a **disk-based overflow queue** at `$SPLUNK_HOME/var/run/splunk/`. When the in-memory queue is full, events spill to disk. When the condition clears (indexer becomes reachable, processing catches up), the persistent queue drains. This is the mechanism that bridges temporary unavailability of the indexer without losing in-transit data.

```ini
[udp://514]
index                = syslog
sourcetype           = syslog
connection_host      = ip
queueSize            = 10MB
persistentQueueSize  = 500MB
```

### 1.5 Why direct UDP/TCP syslog on a Splunk indexer is discouraged

Receiving raw syslog directly on an indexer is tempting but creates problems at scale:

1. **No load balancing** — a single port on a single indexer is a bottleneck; there is no automatic distribution across indexer peers.
2. **UDP packet loss** — high-volume UDP syslog bursts to a busy indexer drop events with no retransmission.
3. **Resource contention** — the indexer should index, not also handle raw socket I/O and parsing at high rates.
4. **No intermediate buffering** — a Heavy Forwarder or syslog server acting as an intermediary can absorb bursts, buffer to disk, and forward reliably.

The recommended architecture is:

```
Network device → [UDP 514] → Heavy Forwarder / syslog server (SC4S) → Indexers
```

A **Heavy Forwarder** (HF) running on a dedicated host, or an open-source syslog server like SC4S (Splunk Connect for Syslog), receives raw syslog, handles the UDP socket buffering, applies parsing and sourcetype detection, and forwards structured events to the indexing tier over the reliable TCP 9997 channel. This isolates the indexers from raw socket overhead and provides proper flow control.

```
mermaid
flowchart LR
    FW[Firewall<br>UDP 514] --> HF[Heavy Forwarder<br>UDP 514 listener<br>inputs.conf]
    SWITCH[Switch<br>UDP 514] --> HF
    PROXY[Proxy<br>TCP 6514] --> HF
    HF --> IDX1[Indexer 1<br>TCP 9997]
    HF --> IDX2[Indexer 2<br>TCP 9997]
```

---

## 2. Scripted inputs

### 2.1 What scripted inputs do

A scripted input runs an **executable script or program** on a scheduled interval and indexes its **standard output** (stdout) as events. The script runs on the host where Splunk is installed; its stdout stream is treated exactly like file-based input data.

Use cases:
- Collect OS-level metrics not available via file (`ps`, `netstat`, `top`, `df`)
- Poll a REST API or CLI tool on a schedule
- Generate synthetic events for testing
- Any data source where you can write a script to produce line-delimited output

### 2.2 `inputs.conf` scripted input stanza

```ini
[script://$SPLUNK_HOME/etc/apps/my_app/bin/ps_script.sh]
index    = os
sourcetype = ps
source   = ps
interval = 30
disabled = false
```

Or using the `$SPLUNK_HOME` placeholder:

```ini
[script://$SPLUNK_HOME/etc/apps/unix_inputs/bin/interfaces.sh]
index    = os
sourcetype = interfaces
interval = 60
```

The stanza header path must be the **full path to the executable**. The `$SPLUNK_HOME` variable is expanded by Splunk.

### 2.3 Script location requirements

Scripts must reside in one of these approved directories:

1. `$SPLUNK_HOME/etc/system/bin/` — system-level scripts
2. `$SPLUNK_HOME/etc/apps/<app>/bin/` — app-scoped scripts (preferred)
3. `$SPLUNK_HOME/bin/scripts/` — legacy location; still supported

Best practice: place scripts in the `bin/` directory of the same app whose `inputs.conf` references them. This keeps configuration and code together and enables clean Deployment Server distribution.

**Scripts must be executable** on the filesystem (`chmod +x script.sh` on Linux/macOS). Splunk will not run non-executable files.

```
$SPLUNK_HOME/etc/apps/unix_inputs/
├── bin/
│   ├── common.sh      # shared library / environment setup
│   ├── ps.sh          # process list script
│   ├── netstat.sh     # network connections
│   └── interfaces.sh  # network interface stats
└── local/
    └── inputs.conf    # references scripts in ../bin/
```

### 2.4 Key attributes

| Attribute | Type | Meaning |
|---|---|---|
| `interval` | integer (seconds) or cron expression | How often to run the script |
| `index` | string | Destination index |
| `sourcetype` | string | Sourcetype for the output |
| `source` | string | Source field value (defaults to script path) |
| `disabled` | bool | Enable/disable |
| `passAuth` | username | Passes a Splunk auth token to the script (for scripts that call Splunk APIs) |

The `interval` can be:
- An integer: seconds between executions (`30` = every 30 seconds)
- A cron expression: `*/5 * * * *` = every 5 minutes; `0 * * * *` = top of each hour

### 2.5 Supported script types

Splunk can execute any binary or script that the OS can run:
- **Shell scripts** (`.sh`) — most common on Linux
- **Python scripts** — Splunk ships a Python runtime; use `$SPLUNK_HOME/bin/python3` as the interpreter
- **PowerShell / batch** — on Windows, `.ps1` and `.bat` scripts
- **Any executable** — compiled binaries, interpreted scripts

The script must write its output to **stdout**. Anything written to **stderr** goes to Splunk's internal logs (`splunkd.log`), not to the event index.

### 2.6 Security considerations

Scripted inputs run with the **same OS user as the Splunk process** (typically `splunk`). This has two implications:

1. The `splunk` user must have read access to any files, commands, or APIs the script touches.
2. Scripts running as `splunk` should not require root — if they do, either delegate specific permissions via `sudo` rules or use a modular input with a separate execution context.

On production systems, audit what scripted inputs are running and what they do. A poorly written script that blocks indefinitely, consumes excessive CPU, or has output formatting bugs will affect event indexing.

### 2.7 Scripted inputs vs. modular inputs

Modular inputs are the **modern, packaged successor** to scripted inputs:

| Aspect | Scripted input | Modular input |
|---|---|---|
| Configuration in Splunk Web | Not natively | Full GUI, validated parameters |
| Per-instance execution | Single instance | One process per stanza |
| Self-describing | No | Declares its own parameter schema |
| Error handling | Manual, via stderr | Structured introspection protocol |
| Distribution | Via app | Via app (same, but more structured) |
| Use case | Quick/custom one-off | Technology add-ons for distribution |

For building new integrations intended for distribution on Splunk Base or across a large fleet, modular inputs are the correct framework. For quick operational scripts or ad hoc collection, scripted inputs are simpler and sufficient.

---

## 3. HTTP Event Collector (HEC)

### 3.1 What HEC is

The HTTP Event Collector is an **HTTP/HTTPS endpoint built into Splunk** that accepts event data via POST requests authenticated with a **bearer token**. No forwarder agent is required on the sending client — any system that can make an HTTP request can send data to Splunk.

HEC listens on **port 8088** by default (configurable). It accepts two endpoint patterns:

| Endpoint | Use case | Format |
|---|---|---|
| `/services/collector/event` | Structured JSON events | JSON with `event`, `time`, `host`, `source`, `sourcetype`, `index` fields |
| `/services/collector/raw` | Raw text data | Unstructured strings; Splunk applies auto-detection or token defaults |

### 3.2 The token model

HEC uses **bearer token authentication**. Each token is:
- Created in Splunk Web (Settings → Data Inputs → HTTP Event Collector) or via REST/CLI
- Assigned a default `index`, `sourcetype`, and optionally an `allowedIndexes` list
- Included in every HTTP request in the `Authorization` header

```
Authorization: Splunk <token_value>
```

If the token is missing, wrong, or revoked, HEC returns `HTTP 403` and drops the event. This is the primary access control mechanism for HEC — each application or team gets its own token, and that token constrains which index data can land in.

### 3.3 Enabling HEC

HEC is **disabled by default**. Enabling requires two steps:

**Step 1 — Enable the global HEC setting:**

Via Splunk Web: Settings → Data Inputs → HTTP Event Collector → Global Settings → Enable

This writes to `inputs.conf`:

```ini
[http]
disabled        = 0
port            = 8088
enableSSL       = 1
dedicatedIoThreads = 2
```

**Step 2 — Create a token:**

Via Splunk Web: Settings → Data Inputs → HTTP Event Collector → New Token

This creates a stanza in `inputs.conf`:

```ini
[http://my_application_token]
disabled        = 0
index           = main
sourcetype      = _json
allowedIndexes  = main,security,app_logs
token           = <auto-generated-UUID>
```

The `[http]` stanza controls global HEC behavior. The `[http://<token_name>]` stanzas control per-token settings that override the global defaults.

### 3.4 HEC configuration via files

In a production environment, HEC is typically configured through files rather than the GUI. The HEC configuration lives in the `splunk_httpinput` app:

```
$SPLUNK_HOME/etc/apps/splunk_httpinput/local/inputs.conf
```

A complete file-based HEC configuration:

```ini
# Global HEC settings
[http]
disabled           = 0
port               = 8088
enableSSL          = 1
dedicatedIoThreads = 2
maxSockets         = 0
maxThreads         = 0

# Token for the web application team
[http://webapp_prod]
disabled       = 0
token          = a1b2c3d4-e5f6-7890-abcd-ef1234567890
index          = web_app
sourcetype     = json_no_timestamp
allowedIndexes = web_app,web_app_debug
description    = Production web app event stream

# Token for the security team's SOAR platform
[http://soar_events]
disabled       = 0
token          = 00112233-4455-6677-8899-aabbccddeeff
index          = security
sourcetype     = soar_event
allowedIndexes = security
```

### 3.5 Sending data to HEC — curl examples

**Structured JSON event (event endpoint):**

```bash
curl -k https://splunk.example.com:8088/services/collector/event \
  -H "Authorization: Splunk a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
  -H "Content-Type: application/json" \
  -d '{"event": {"field1": "value1", "action": "login", "user": "alice"}, "sourcetype": "auth_event", "index": "security"}'
```

**Raw text event (raw endpoint):**

```bash
curl -k https://splunk.example.com:8088/services/collector/raw \
  -H "Authorization: Splunk a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
  -d 'Jan 25 14:22:33 webhost01 sshd[1234]: Accepted publickey for alice from 10.20.1.5'
```

**Multiple events in a single request (batch):**

```bash
curl -k https://splunk.example.com:8088/services/collector/event \
  -H "Authorization: Splunk a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
  -H "Content-Type: application/json" \
  -d '{"event": {"msg": "event1"}}{"event": {"msg": "event2"}}{"event": {"msg": "event3"}}'
```

Multiple JSON objects can be concatenated (not in an array) in a single request body — HEC parses them as separate events.

### 3.6 Token fields and metadata override

When using the `/services/collector/event` endpoint, the JSON payload can include metadata fields that **override the token's defaults**:

```json
{
  "time":       1700000000.000,
  "host":       "app-server-07",
  "source":     "myapp:auth",
  "sourcetype": "auth_event",
  "index":      "security",
  "event":      { "user": "bob", "action": "logout" }
}
```

- `time` — Unix epoch timestamp (seconds, with optional decimal for milliseconds). If omitted, Splunk uses the arrival time.
- `host`, `source`, `sourcetype` — override token defaults at the per-event level.
- `index` — must be in the token's `allowedIndexes` list; if absent from the payload, the token's `index` default is used.

This per-event metadata override is powerful: a single token can route events to different indexes or assign different sourcetypes based on what the sending application injects into each event.

### 3.7 Indexer acknowledgement

By default, HEC returns `HTTP 200` when it has **received** the event — not when the event has been **written to an index**. For applications where event loss is unacceptable (payment processing, compliance logging), this is insufficient.

**Indexer acknowledgement** (`ackEnabled`) adds a two-phase commit:

1. HEC accepts the event and returns an **ackID** in the response.
2. The client polls `/services/collector/ack` with the ackID.
3. When the event has been written to index, HEC responds with `{"acks": {"<ackID>": true}}`.

```ini
[http://critical_events]
ackEnabled = true
token      = ...
```

The client workflow:
```bash
# Step 1: send event, capture ackID from response
RESPONSE=$(curl -sk -H "Authorization: Splunk <token>" \
  -d '{"event": "critical record"}' \
  https://splunk:8088/services/collector/event)
ACK_ID=$(echo $RESPONSE | python3 -c "import sys,json; print(json.load(sys.stdin)['ackId'])")

# Step 2: poll for acknowledgement
curl -sk -H "Authorization: Splunk <token>" \
  -d "{\"acks\": [${ACK_ID}]}" \
  https://splunk:8088/services/collector/ack
```

Acknowledgement increases latency and requires client-side state. Use it only for high-consequence data streams, not for bulk telemetry.

### 3.8 HEC in a distributed environment

In a distributed Splunk deployment (multiple indexers), HEC must be configured to use an appropriate load-balancing strategy. There are two approaches:

**Option A — HEC on Heavy Forwarders (recommended):**
Enable HEC on a pool of Heavy Forwarders fronted by a load balancer. The HF receives events via HEC, applies any necessary transforms, and forwards to indexers via the standard TCP 9997 channel with automatic load balancing.

```
Sending clients → LB (port 8088) → HF pool (HEC enabled) → Indexers (port 9997)
```

**Option B — HEC directly on indexers:**
Enable HEC on each indexer peer. Clients or a load balancer distributes POST requests across indexers. This works but means the indexers handle both HTTP ingestion and indexing, which competes for resources. Use a dedicated HEC endpoint (HF) where possible.

For the Deployment Server to distribute HEC configuration across indexers or forwarders, set `useDeploymentServer = 1` in the `[http]` stanza.

### 3.9 HEC vs. Universal Forwarder — when to use each

| Dimension | Universal Forwarder (UF) | HTTP Event Collector (HEC) |
|---|---|---|
| Agent required | Yes — UF installed on source | No — any HTTP client |
| Source control | File tailing, Windows events, scripted | Any HTTP-capable application or service |
| Reliability | High — persistent queuing, acks built-in | Variable — depends on client retry logic |
| Throughput | High — optimized binary protocol | High — HTTP/1.1 or HTTP/2 |
| Cloud / serverless | Difficult — no persistent host | Ideal — Lambda, Cloud Functions, containers |
| Overhead on source | Low (UF is lightweight) | Zero install overhead |
| Best for | OS logs, application file logs, Windows | App events, cloud-native, IoT, APIs |

The UF remains the right choice wherever you can install it and have file-based logs to collect. HEC is the right choice for cloud-native environments, serverless functions, application developers who want a simple POST endpoint, and anywhere running a forwarder is impractical.

---

## 4. Input architecture decision tree

```
Is data in a file on the local filesystem?
  Yes → [monitor://] stanza
    Is it a one-time archive? → batch:// or oneshot (CLI)
    Is it live/growing? → monitor://

Is data arriving as a network stream (syslog)?
  Yes → [udp://] or [tcp://] stanza
    → Prefer HF/SC4S in front of indexer for production

Is data available only via script / API / CLI?
  Yes → [script://] stanza (or modular input for packaged distribution)

Is the source an HTTP-capable application with no agent?
  Yes → HTTP Event Collector (HEC)
    → Structured JSON → /services/collector/event
    → Raw text → /services/collector/raw
```

---

## 5. Terminology & version notes

- **HEC port 8088** — default since introduction; configurable in the `[http]` stanza `port` attribute.
- **`allowedIndexes`** — constrains which indexes a token can write to; events specifying an index not in this list are rejected. Introduced to prevent token misuse from landing data in wrong indexes.
- **`enableSSL`** — default `1` (enabled) in Splunk 9.x HEC configurations. Production deployments should always use HTTPS (port 8088 with TLS). Self-signed cert → use `-k` in curl for testing only.
- **Scripted inputs** — pre-date modular inputs; still fully supported in 9.x. For new development, modular inputs are preferred.
- **SC4S** — Splunk Connect for Syslog; an open-source, containerized syslog server (based on `syslog-ng`) that receives raw syslog, normalizes it, and forwards to Splunk via HEC. The current recommended architecture for high-volume syslog collection.
- **`connection_host`** — available for both TCP and UDP network inputs; the `dns` value performs live reverse DNS at event receipt time and is not cached per session.
- **`queueSize` / `persistentQueueSize`** — both apply at the **input** stage. The analogous `maxQueueSize` in `outputs.conf` applies at the **output** stage. They are not the same attribute.
- **Whitelist/blacklist in network inputs** — `allowlist`/`denylist` apply to monitor file inputs (§1.5 of the monitor topic). Network inputs do not have a path-based filter; filtering network data happens at the parsing stage via `props.conf`/`transforms.conf`.

---

## 6. Common misconceptions

- **"HEC is less reliable than a UF because it's HTTP."** Reliability depends on the client's retry logic, not the protocol. HEC with indexer acknowledgement and client-side retries can match UF reliability. Vanilla fire-and-forget HEC without retry is less reliable than a UF.
- **"I can receive syslog on the indexer over UDP 514 with no issues."** Not at scale. UDP bursts drop events silently; the indexer's I/O resources are better spent indexing. Use an HF or SC4S in front.
- **"Scripted inputs can run as root to access protected files."** The script runs as the Splunk process user. Granting the Splunk user root access (or running Splunk as root) is a security anti-pattern. Use targeted `sudo` rules for specific commands if needed.
- **"A single HEC token should be shared across all applications."** No — use one token per application or team. Tokens control index routing and access; shared tokens lose the ability to control or revoke per-application.
- **"HEC with `enableSSL = 0` is fine for internal networks."** Tokens in HTTP headers are plaintext. Even internal traffic should use TLS. The `-k` flag in curl (skip cert check) is a testing convenience, not a production configuration.
- **"Scripted inputs work the same on Windows and Linux."** The script type and paths differ; shell scripts run on Linux; PowerShell or batch on Windows. Cross-platform apps using scripted inputs must bundle both versions.
- **"HEC `ackEnabled` prevents all event loss."** It prevents loss between the HEC endpoint and the index. It does not protect against network loss before the event reaches HEC, or against client crashes before polling the ack. True end-to-end delivery guarantees require additional client-side retry logic.

---

## 7. Mastery checklist — what you should be able to explain

- The TCP and UDP `inputs.conf` stanzas, their common attributes, and what `connection_host` controls.
- Why direct UDP syslog on an indexer is problematic at scale and what the preferred architecture looks like.
- How `queueSize` and `persistentQueueSize` provide flow control for network inputs.
- The scripted input stanza format, the required script location (`bin/` directory), the `interval` attribute (seconds or cron), and what Splunk indexes from script execution.
- Security implications of scripted inputs: what user they run as, and why running as root is an anti-pattern.
- When to use a modular input instead of a scripted input.
- What HEC is, what port it uses, how it authenticates (bearer token in Authorization header).
- The two HEC endpoints (`/services/collector/event` vs `/services/collector/raw`) and what each accepts.
- The `[http]` global stanza vs `[http://<token_name>]` per-token stanza structure.
- How to enable HEC via files (the `splunk_httpinput` app).
- What `allowedIndexes` does and why it matters for token security.
- How indexer acknowledgement works (ackID flow), when to use it, and its trade-offs.
- The HEC vs UF decision: when each is the right tool.
- The recommended HEC architecture for distributed deployments (HF pool + LB in front).

---

## 8. Key terms (flashcard seeds)

- **`[udp://<port>]` / `[tcp://<port>]`** — `inputs.conf` stanzas for network port listeners.
- **`connection_host`** — `ip` (use sender IP), `dns` (reverse DNS lookup), `none` (static from stanza).
- **`queueSize`** — in-memory input buffer (default 500 KB); drop or backpressure on overflow.
- **`persistentQueueSize`** — disk-based overflow buffer at `$SPLUNK_HOME/var/run/splunk/`; drains when conditions clear.
- **UDP vs TCP syslog** — UDP is connectionless, drops on overflow, no retransmission; TCP is stream-based with retransmission.
- **SC4S** — Splunk Connect for Syslog; containerized syslog-ng that normalizes and forwards to HEC.
- **`[script://<path>]`** — scripted input stanza; runs executable, indexes stdout.
- **`interval`** — integer seconds or cron expression controlling script run frequency.
- **Script `bin/` directory** — scripts must live in `$SPLUNK_HOME/etc/apps/<app>/bin/` (or system/bin); must be executable.
- **Modular input** — packaged, structured modern alternative to scripted inputs; supports GUI config, per-stanza execution.
- **HTTP Event Collector (HEC)** — token-authenticated HTTP/HTTPS endpoint on port 8088 for agentless event ingestion.
- **HEC bearer token** — `Authorization: Splunk <token>` header; required on every request; controls index routing.
- **`/services/collector/event`** — JSON-structured HEC endpoint; supports per-event metadata override.
- **`/services/collector/raw`** — raw text HEC endpoint; uses token defaults for metadata.
- **`[http]` stanza** — global HEC settings (port, SSL, thread count).
- **`[http://<name>]` stanza** — per-token HEC settings (index, sourcetype, allowedIndexes).
- **`allowedIndexes`** — list of indexes the token may write to; events requesting other indexes are rejected.
- **Indexer acknowledgement (`ackEnabled`)** — two-phase commit; returns ackID; client polls `/services/collector/ack` for confirmed indexing.
- **HEC vs UF** — HEC for agentless/cloud/app-level events; UF for file-based OS/application logs where agent install is feasible.

---

## 9. Questions to drill (quiz seeds)

1. Write a complete `inputs.conf` stanza that listens for syslog on UDP 514, routes to the `network` index with sourcetype `syslog`, sets the host from the sender's IP address, and configures a 10 MB in-memory queue.
2. A network device sends UDP syslog at 50,000 events per second in bursts. Your Universal Forwarder processes at 30,000/sec. Which `inputs.conf` attributes help protect against event loss, and what are their limitations?
3. Explain why receiving raw syslog directly on an indexer at high volume is an anti-pattern. What architecture would you recommend instead?
4. Write the `inputs.conf` stanza for a scripted input that runs `/apps/unix_inputs/bin/ps.sh` every 30 seconds, indexing output to `os_metrics` with sourcetype `ps_output`.
5. What is the mandatory filesystem requirement for a script referenced by a scripted input? What user does the script run as?
6. You have a Lambda function that generates security events. It cannot run a forwarder. What Splunk input type is appropriate and why? What does the HTTP request look like, including the required header?
7. Describe the structure of the `[http]` and `[http://<token>]` stanzas. Which attributes can be overridden per-token?
8. A developer's application sends HEC events without specifying `index` in the JSON payload. The token has `index = main` and `allowedIndexes = main,security`. Where do the events land?
9. You need to guarantee that a compliance-critical event stream is confirmed as indexed before your application marks a transaction complete. Which HEC feature enables this? Describe the two-step flow.
10. Compare a scripted input with a modular input across three dimensions. When would you choose one over the other?
