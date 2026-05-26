---
type: pre-class
theme: 03-apps-configs-layering
topic: apps-and-addons
covers: "Lectures 17–18"
read_time: "~3–4 min"
tags: [study-guide/pre-class, theme/03-apps-configs-layering]
---

# Pre-class — Apps & Add-ons

> Read before the lectures (covers lectures 17–18). ~3–4 min. The videos install a Cisco app and add-on via the web and the CLI; this primer gives you the concepts so the clicks make sense.

## Why this matters
Almost everything you add to Splunk — vendor integrations, parsing, dashboards, even the Search app and Enterprise Security — ships as an **app** or an **add-on**. And under the hood an app is just a folder of `.conf` files, which is the bridge to the next topic (configuration layering).

## The mental model (hold these)
1. **Both extend Splunk** (plugins). The split: an **app** is a complete solution *with a UI* (dashboards, views); an **add-on** is a *UI-less, reusable component* that gets data in and cleans it (inputs, `props`/`transforms`, sourcetypes, field extractions).
2. **Add-on gets data in and normalizes it; app makes it useful.** A vendor solution often ships as both — the add-on parses on indexers/forwarders, the app visualizes on the search head.
3. **TA = Technology Add-on** — provides **CIM-compliant** field knowledge; this is what makes a source usable in Enterprise Security.
4. **Apps live in `$SPLUNK_HOME/etc/apps/<app>/`** with `default/` (shipped — never edit), `local/` (your overrides — wins), `metadata/`, `bin/`, `static/`.
5. **Install = drop files in `etc/apps`** (web upload, or CLI untar + `chown`), then **reload/restart** so the running Splunk picks it up.

## Key terms (quick definitions)
- **App** — package with a UI / solution for a data source.
- **Add-on** — UI-less reusable package that ingests/enriches data.
- **TA (Technology Add-on)** — tech-specific add-on with CIM field knowledge.
- **Splunkbase** — Splunk's app catalog; **Splunk-supported** (vetted) vs **community** (not vetted).
- **`default/` vs `local/`** — shipped config (don't touch) vs your overrides (local wins).
- **`metadata/*.meta`** — ownership + permissions + sharing (private/app/global).
- **debug/refresh (reload)** — apply config changes without a full restart.

## Watch for this in the video
- The course installs **both** a Cisco *add-on* (no UI — won't appear in the Apps menu) and a Cisco *app* (has dashboards). Notice the add-on "disappears" — that's expected, it has no UI.
- CLI install = `tar -xzvf … -C etc/apps` then **`chown splunk:splunk`** — the same ownership lesson as the install topic.
- After CLI changes, the course runs **"debug refresh"** — because the deleted/added app isn't live until Splunk reloads its in-memory config.
- Note the **"shared globally"** label — that's the sharing scope (private/app/global) from the `metadata` files, which connects to the layering topic next.

## Questions to hold in mind while watching
1. For this Cisco solution, which part is the add-on doing and which part is the app doing?
2. Why does the add-on not show up in the Apps menu?
3. After dropping files into `etc/apps`, why isn't the app live until I reload/restart?
4. What's the difference between Splunk-supported and community content, and would I trust a community add-on in production?

## How this connects forward
- **Config files & layering** (next) explains why apps have `default/` and `local/` — they're layers in the precedence scheme.
- **Deployment Server** and the **SHC Deployer** are how apps get pushed to many hosts instead of installed by hand.
- **Data onboarding** is mostly about the `props`/`transforms` an add-on contains.

---

## Official references (for verification / deeper reading)

| Topic | Splunk Docs page |
|---|---|
| What's an app / apps and add-ons | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Whatsanapp |
| About Splunk add-ons | https://docs.splunk.com/Documentation/AddOns/released/Overview/AboutSplunkAdd-ons |
| Splexicon: add-on | https://docs.splunk.com/Splexicon:Addon |
| Where apps are installed / config file directories | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Configurationfiledirectories |
| Manage app/object permissions | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Appconf |
| Splunkbase | https://splunkbase.splunk.com |
