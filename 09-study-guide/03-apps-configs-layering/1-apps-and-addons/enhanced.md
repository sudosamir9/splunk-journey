---
type: enhanced
theme: 03-apps-configs-layering
topic: apps-and-addons
covers: "Lectures 17–18"
tags: [study-guide/enhanced, theme/03-apps-configs-layering]
sources: docs.splunk.com (Splunk 9.x / latest, 2026)
---

# Splunk Apps & Add-ons

> Deep reference on what Splunk apps and add-ons are, how they differ, where they live on disk, and how to install and manage them via the web and the CLI. Companion `pre-class.md` is the short primer and holds the official-doc links.

---

## 0. Orientation

Almost everything you add to Splunk — vendor integrations, parsing rules, dashboards, the Search app itself, Enterprise Security — arrives packaged as an **app** or an **add-on**. Understanding what they are, the difference between them, and how they sit on disk is the bridge between "I installed Splunk" and "I onboarded a data source." It also sets up the next topic (configuration files and layering), because an app is, under the hood, just a directory of `.conf` files and assets.

---

## 1. What apps and add-ons are

Both are **packages that extend Splunk's functionality** — think of them as plugins. The classic use case: a vendor's logs (Cisco, Palo Alto, Fortinet, etc.) arrive in a format Splunk doesn't understand out of the box. Rather than every customer writing parsing rules from scratch, someone packages the knowledge — how to break the events, extract fields, assign sourcetypes — into a reusable bundle. That bundle is an add-on (and often a companion app for visualization).

A package can contain: configuration files (`props.conf`, `transforms.conf`, `inputs.conf`, …), sourcetype definitions, field extractions, lookups, macros, saved searches, dashboards, custom search commands, scripts, and a navigation UI — in any combination.

---

## 2. App vs. add-on — the distinction

This is the key conceptual split:

| | **App** | **Add-on (TA)** |
|---|---|---|
| Purpose | A complete solution for a data source/use case, with a **user interface** | A **reusable component** that gets data in or enriches it |
| UI / navigation | Yes — dashboards, views, often a setup screen | **No navigable UI**; it works behind the scenes |
| Typical contents | Dashboards, saved searches, knowledge objects, *plus* the underlying inputs/parsing | Inputs, `props`/`transforms`, sourcetype definitions, field extractions, macros, custom REST endpoints |
| Used how | Run/viewed directly by users | Not run standalone — supports apps and the platform across many use cases |
| Example | "Cisco Networks" app (dashboards over Cisco data) | "Splunk Add-on for Cisco" (parses Cisco logs into fields/sourcetypes) |

**Mental model:** an **add-on gets the data in and makes it clean**; an **app makes the clean data useful** (visualizes/analyzes it). A single solution often ships as *both* — the add-on does the parsing on indexers/forwarders, the app provides the dashboards on the search head.

---

## 3. Technology Add-ons (TA) and the CIM

Add-ons whose names start with **`TA-`** (or "Splunk Add-on for …") are **technology add-ons** — technology-specific packages that provide the field extractions and **CIM-compliant** knowledge needed to normalize a data source. CIM (Common Information Model) is the shared schema that lets data from many vendors be searched with common field names (e.g., `src_ip`, `user`, `action`). TAs are what make a source usable in **Enterprise Security**, which depends on CIM normalization. (Where each TA's pieces get installed — forwarder vs. indexer vs. search head — matters in a distributed deployment; that's a distributed-onboarding concern.)

---

## 4. Splunkbase

**Splunkbase** (splunkbase.splunk.com) is Splunk's catalog/directory of apps and add-ons. Two trust tiers:

- **Splunk-supported** — built and maintained by Splunk, vetted ("Splunk Supported" tag). Prefer these.
- **Community-supported** — built by third parties/community; useful but **not** vetted by Splunk ("not supported by Splunk or the developer" notices). Review before deploying.

You (or anyone) can also package and upload your own apps. A Splunk.com account is required to download.

> **Security note (public-repo / production mindset):** treat a community add-on like any third-party code — it can contain scripts that run on your Splunk hosts. Review it, check the publisher and version, and stage it before deploying widely.

---

## 5. Where apps live, and app directory anatomy

Every installed app/add-on is a directory under **`$SPLUNK_HOME/etc/apps/<app_name>/`**. The standard subdirectories:

| Subdir | Contents |
|---|---|
| `default/` | The app's shipped configuration. **Never edit** — upgrades overwrite it. |
| `local/` | Your customizations/overrides. `local` beats `default`. |
| `metadata/` | `default.meta` / `local.meta` — object ownership, **permissions/sharing**, export settings. |
| `bin/` | Executable scripts, custom commands, scripted/modular inputs. |
| `static/` | Icons, screenshots, static assets. |
| `lookups/` | Lookup files (CSV, etc.). |
| `appserver/` | Web UI assets. |

So "an app" is literally a folder of `.conf` files plus assets — which is exactly why the configuration-layering topic matters: app `default`/`local` directories are layers in the precedence scheme.

---

## 6. Installing an app/add-on — via the web

1. Download the package (a `.tgz`/`.spl` file) from Splunkbase (log in first).
2. In Splunk Web: **Apps → Manage Apps → Install app from file**, then upload (drag-and-drop) the package.
3. Splunk unpacks it into `etc/apps/` and (usually) prompts to restart if required.

You can also install directly **from Splunkbase within Splunk Web** ("Browse more apps") if the instance has internet access and you provide Splunk credentials.

After install you can see the app under **Apps** (if it has a UI) and manage its **visibility**, **sharing/permissions**, and **enabled/disabled** state.

---

## 7. Installing an app/add-on — via the CLI

The manual, repeatable path (and the only path on headless/forwarder hosts):

1. Copy the package to the host and **unpack it into `etc/apps`**:
   ```
   sudo tar -xzvf splunk-add-on-for-cisco.tgz -C /opt/splunk/etc/apps
   ```
2. **Change ownership** to the Splunk service account so Splunk can read/write it:
   ```
   sudo chown -R splunk:splunk /opt/splunk/etc/apps/<app_dir>
   ```
3. **Make Splunk pick it up** (see §8) — restart or reload.

There's also a dedicated CLI command: `splunk install app <package.tgz>` (and `splunk remove app <name>`), which unpacks and registers the app for you. To **delete** an app manually, remove its directory (`rm -rf etc/apps/<app>`) and reload.

> **The chown step is mandatory** — same lesson as the install topic. If the app directory is owned by root, Splunk can't read its config properly.

---

## 8. Making changes take effect: restart vs. reload

A subtle but important point: when you add/remove an app on disk, the change **isn't live until Splunk reloads its configuration**. The running `splunkd` holds config in memory. Two ways to apply:

- **Restart Splunk** (`splunk restart`) — always works, but interrupts service.
- **Reload without full restart** — the "debug/refresh" endpoint reloads many configurations in place (`splunk _internal call /services/admin/conf-times/_reload`, or via the URL `/debug/refresh`). The course calls this "debug refresh." Not everything can be reloaded — some changes (e.g., certain `server.conf`/index changes) still require a restart.

If you delete an app's files but still see it in the UI, that's because the old config is still in memory — reload/restart to clear it.

---

## 9. Visibility, sharing/permissions, and state

- **Enabled/disabled** — an app can be present but disabled.
- **Visible/invisible** — add-ons are typically **invisible** (no nav menu entry) because they have no UI; apps are visible.
- **Sharing scope (permissions)** — objects and apps are shared at one of three levels, stored in the `metadata/*.meta` files:
  - **Private** — only the owning user.
  - **App** — everyone using that app.
  - **Global** — all apps/users on the instance.
  Role-based **read/write** permissions control who can view vs. edit. (When the course installs the Cisco add-on and notes "it's shared globally," that's this setting.)

These sharing scopes connect directly to the next topic: an object's sharing/export determines whether it participates in another app's configuration context.

---

## 10. Best practices

- **Never edit `default/`** — put changes in `local/`. Upgrades overwrite `default/`.
- **Prefer Splunk-supported** Splunkbase content; review community add-ons.
- **At scale, don't hand-install on every host** — push apps to forwarders via the **Deployment Server** and to search-head-cluster members via the **Deployer** (their own topics). Manual install is for single hosts and learning.
- **Mind where each part of a TA goes** in a distributed deployment (parsing pieces on indexers/heavy forwarders, inputs on forwarders, UI on search heads).

---

## 11. Terminology & version notes

- Package files use the **`.spl`** or **`.tgz`** extension (both are gzipped tarballs).
- The "debug/refresh" reload mechanism still exists, but the supported way to reload is via the REST endpoint / `splunk _internal call`; behavior of what can reload vs. needs a restart varies by config type.
- "Technology Add-on (TA)" naming is conventional; the CIM is delivered by the **Splunk Common Information Model add-on**.

---

## 12. Common misconceptions

- **"Apps and add-ons are the same thing."** No — an app has a UI and is a solution; an add-on is a UI-less reusable component (often the parsing/inputs half).
- **"I edited the file in `default/` and it worked."** It works until the next upgrade wipes it. Always use `local/`.
- **"I deleted the app folder but it's still there."** The running config is in memory — reload/restart.
- **"Everything on Splunkbase is vetted by Splunk."** Only Splunk-supported entries are; community ones aren't.
- **"An add-on's dashboards aren't showing."** Add-ons usually have no UI by design — that's expected.

---

## 13. Mastery checklist — what you should be able to explain

- The difference between an app and an add-on, with an example of each.
- What a TA is and why it matters for CIM/Enterprise Security.
- Splunkbase, and the difference between Splunk-supported and community content.
- Where apps live (`etc/apps/<app>`) and the role of `default/`, `local/`, `metadata/`, `bin/`.
- How to install an app via the web and via the CLI (untar to `etc/apps`, `chown`, reload/restart).
- Why a newly installed/removed app needs a reload or restart to take effect.
- The three sharing scopes (private/app/global) and where they're stored.

---

## 14. Key terms (flashcard seeds)

- **App** — a Splunk package with a UI/solution for a data source or use case.
- **Add-on** — a UI-less, reusable package that gets data in / enriches it.
- **Technology Add-on (TA)** — technology-specific add-on providing CIM-compliant field knowledge.
- **CIM** — Common Information Model; shared field schema for normalization.
- **Splunkbase** — Splunk's app/add-on catalog (supported vs. community).
- **`$SPLUNK_HOME/etc/apps/`** — where installed apps live.
- **`default/` vs `local/`** — shipped config (never edit) vs. your overrides (local wins).
- **`metadata/` (`*.meta`)** — ownership, permissions, sharing/export.
- **`bin/`** — scripts/custom commands within an app.
- **Sharing scope** — private / app / global.
- **`splunk install app` / `splunk remove app`** — CLI install/remove.
- **debug/refresh (reload)** — apply config changes without a full restart (where supported).
- **`.spl` / `.tgz`** — app package file formats.

---

## 15. Questions to drill (quiz seeds)

1. Define an app and an add-on and give a concrete example of each for the same data source.
2. Why does an add-on usually have no navigation UI, and what does it typically contain?
3. What is a TA, and why is it essential for Enterprise Security?
4. On Splunkbase, what's the difference between "Splunk supported" and community content, and why does it matter?
5. List the standard subdirectories of an app and what each holds.
6. Give the CLI steps to install an add-on by hand. Why is the `chown` step required?
7. You removed an app's directory but still see it in the UI — what's going on and how do you fix it?
8. Name the three sharing scopes and where that setting is stored.
9. Why should you never edit files in an app's `default/` directory?
10. At scale, how should apps be deployed to forwarders rather than installing by hand?
