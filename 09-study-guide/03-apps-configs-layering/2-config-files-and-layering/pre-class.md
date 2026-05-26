---
type: pre-class
theme: 03-apps-configs-layering
topic: config-files-and-layering
covers: "Lectures 19–21"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/03-apps-configs-layering]
---

# Pre-class — Configuration Files & Layering / Precedence

> Read before the lectures (covers lectures 19–21). ~4–5 min. This is one of the most important topics in Splunk administration — the lectures move fast through precedence, so walk in already holding the model.

## Why this matters
Splunk's behavior is controlled by `.conf` files, and the *same* file can exist in many places with conflicting settings. Splunk merges them by **precedence**. Almost every "why is Splunk doing that / why didn't my change take effect?" traces back to this. Master it and configuration stops being mysterious.

## The mental model (hold these)
1. **`.conf` files = `[stanza]` + `attribute = value`, case-sensitive.** Each file governs one area (`inputs`, `props`, `transforms`, `outputs`, `indexes`, `server`…).
2. **Config lives in three places under `etc/`:** `system/`, `apps/<app>/`, `users/<user>/`. Each app and system has **`default/`** (shipped — never edit) and **`local/`** (your overrides — local wins).
3. **The same file can exist in many layers; Splunk merges them at runtime by precedence.** Per attribute: on a conflict the **highest-precedence copy wins**; non-conflicting attributes are **unioned** in.
4. **Two contexts, two different precedence orders:**
   - **Global (index-time:** inputs/parsing/indexing/forwarding**):** `system/local` **#1** > app `local` > app `default` > `system/default`.
   - **App/user (search-time):** **user #1** > current-app `local` > current-app `default` > `system/local` > `system/default`.
   - **The contrast is the whole point:** global → system/local on top; app/user → user/app on top and system near the bottom.
5. **App ties break by lexicographic ASCII order:** numbers > UPPERCASE > lowercase (so `Cisco` beats `firewall`; a leading number beats letters). Admins exploit this to force an app to win.
6. **`btool` shows the effective merged config** and (with `--debug`) which file each setting came from — your go-to for "why is this value what it is?"

## Key terms (quick definitions)
- **Stanza / attribute** — `[section]` and `key = value` (case-sensitive).
- **default vs local** — shipped (never edit, overwritten on upgrade) vs your override (wins).
- **Global context** — index-time; `system/local` is highest.
- **App/user context** — search-time; user → current app highest, system near bottom.
- **Lexicographic order** — ASCII tie-break among apps: numbers > uppercase > lowercase.
- **Merge** — conflict → highest precedence wins; no conflict → union.
- **`btool`** — `splunk btool <conf> list --debug` shows merged config + source file.

## Watch for this in the video
- The course walks an `inputs.conf` merge across `system/local`, app `local`/`default`, and `system/default` — follow *why each attribute's winner is chosen* (conflict → highest; else union).
- It explains **"Cisco beats firewall"** by ASCII (uppercase `C` before lowercase `f`) — that's the lexicographic rule.
- For **search-time** (a user in the Cisco app), notice the order flips to **user → app → system** — different from index-time.
- "default should never be changed; customize under local" is stated explicitly — internalize it.

## Questions to hold in mind while watching
1. For a given setting, which copy wins — and does the answer change between index-time and search-time?
2. When two apps both define the setting, how does Splunk break the tie?
3. What's the difference between a *conflict* (highest wins) and a *union* (added in) during merge?
4. How would I prove which file a running setting actually came from?

## How this connects forward
- **Data onboarding** (`props.conf`/`transforms.conf`) is precedence in action — and adds *within-file* stanza specificity.
- **Deployment Server / Deployer / indexer clustering** all push config as apps, which slot into this precedence scheme (peer-apps on clustered indexers).
- Every later "edit a conf file" lab assumes you know `default` vs `local` and how to verify with `btool`.

---

## Official references (for verification / deeper reading)

| Topic | Splunk Docs page |
|---|---|
| Configuration file precedence | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Wheretofindtheconfigurationfiles |
| Configuration file directories | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Configurationfiledirectories |
| Configuration file structure | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Howtoeditaconfigurationfile |
| Attribute precedence within a single file | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Attributeprecedencewithinafile |
| Use btool to troubleshoot configurations | https://docs.splunk.com/Documentation/Splunk/latest/Troubleshooting/Usebtooltotroubleshootconfigurations |
