# Roadmap — Splunk Architect Journey

Phase- and chapter-based plan. **No calendar.** Variable rhythm means deliverables over deadlines. Each phase ends with a clear artifact, not a date.

I'm in Phase 0 right now. The whole repo gets built across Phase 0 → Phase 3, with stretch goals beyond.

---

## Phase 0 — Setup (current)

**Goal:** Toolchain works, repo is bootstrapped, first commit pushed to public GitHub.

**Done when:**
- [ ] WSL2, Claude Code, VS Code, Obsidian, Notion, Azure CLI, GitHub CLI all installed and verified
- [ ] Repo bootstrapped at `/mnt/c/Users/<me>/Documents/splunk-journey/`
- [ ] All bootstrap files in place; folder structure created by Claude Code
- [ ] Udemy transcripts dropped into `02-course-saif/transcripts/<theme>/`
- [ ] First commit pushed to public GitHub
- [ ] First lab journal entry written: `05-labs/journal/YYYY-MM-DD-setup-complete.md`
- [ ] `handoff.md` populated and reflects readiness for Phase 1

**Deliverable:** A clean, navigable repo with everything in place. Anyone (including future-me) can land in it and know what's going on within 5 minutes.

---

## Phase 1 — Foundations

**Scope:** Saif themes 1-3 — fundamentals, install, apps/configs/layering.

**Course coverage:** Lectures 1-21.

**Chapters:**

### Chapter 1.1 — Mental model of Splunk
- Watch lectures 1-4
- Write `03-topics/splunk-mental-model.md`: what Splunk fundamentally does, the data pipeline, the components and their roles
- Tie it to the architecture diagram in `01-architecture/`

### Chapter 1.2 — Linux install + best practices
- Watch lectures 5-16
- **Lab work:** install Splunk on a single Linux VM in Azure (smallest cheap SKU). Disable THP, set ulimits, configure boot start.
- Write `05-labs/runbooks/splunk-linux-install.md` — your own version of best practices.
- Lab journal entry documenting what broke, what surprised you.

### Chapter 1.3 — Apps and conf layering
- Watch lectures 17-21
- **The most important infra concept:** conf file precedence and layering. This is where infrastructure gets weird.
- Write `03-topics/conf-file-layering.md` — the synthesis. Include a worked example showing exactly which file wins in a contrived case.
- Make a `04-concepts/btool.md` atom — `btool` is your friend, it shows effective config.

### Chapter 1.4 — Bundle for NBLM
- Bundle `01-foundations` for NotebookLM. Source: theme transcripts + your notes + the two synthesis notes + your runbook.
- Generate all four NBLM outputs.
- Listen to the podcast, take the quiz, review the mind map.
- Update synthesis notes with anything NBLM exposed.

**Phase 1 done when:**
- [ ] All 21 lectures watched, notes in `02-course-saif/notes/`
- [ ] Single-node Splunk running in Azure
- [ ] Two synthesis notes done: `splunk-mental-model.md`, `conf-file-layering.md`
- [ ] One runbook: `splunk-linux-install.md`
- [ ] At least one `04-concepts/` atom (`btool.md`)
- [ ] NBLM bundle `01-foundations` created and outputs generated
- [ ] At least 3 lab journal entries

---

## Phase 2 — Storage and forwarding

**Scope:** Saif themes 4-8 — indexes/buckets, users/LDAP, forwarders, distributed setup, data flow concepts, Deployment Server.

**Course coverage:** Lectures 22-45.

**Chapters:**

### Chapter 2.1 — Indexes, buckets, retention, fishbucket
- Watch lectures 22-28
- **Lab:** create indexes via CLI + web. Walk through bucket lifecycle. Test retention by aggressively shortening it.
- Write `03-topics/indexes-and-buckets.md`. Include a diagram of the bucket states.
- `04-concepts/` atoms: `bucket-states.md`, `fishbucket.md`, `frozen-thawed.md`.

### Chapter 2.2 — Users, roles, LDAP/AD
- Watch lectures 29-30
- **Lab:** integrate Splunk with the lab AD DC. Create custom roles. Test capability inheritance.
- Write `05-labs/runbooks/splunk-ldap-integration.md`.

### Chapter 2.3 — Forwarders
- Watch lectures 31-36
- **Lab:** deploy UFs on the lab Windows endpoint and Linux endpoint. Get logs flowing to a single indexer.
- Write `03-topics/forwarder-topology.md` — UF vs HF vs IF, when to use each. Tie to your architecture diagram.

### Chapter 2.4 — Data flow concepts
- Watch lectures 37-43
- **Critical lecture:** 40 (event breaking + load balancing). Pay close attention; this is exam-heavy.
- Write `03-topics/parsing-pipeline.md` — the journey from raw event → indexed event. Include the parsing/indexing/search phases.

### Chapter 2.5 — Deployment Server
- Watch lectures 44-45
- **Lab:** deploy the DS in your Mgmt subnet. Add UFs as deployment clients. Push an app via server class.
- Write `05-labs/runbooks/deployment-server-setup.md`.

### Chapter 2.6 — Bundle for NBLM
- Two bundles: `02-storage` (indexes, buckets, retention) and `02-forwarding` (forwarders, DS, data flow). Don't combine — too much for one notebook.
- Generate all four outputs per bundle.

**Phase 2 done when:**
- [ ] All 24 lectures watched
- [ ] Lab has: 1 indexer receiving from 2 UFs (Win + Linux), LDAP integrated, DS pushing apps
- [ ] Four synthesis notes done
- [ ] Two runbooks done
- [ ] Two NBLM bundles complete
- [ ] At least 5 more lab journal entries

---

## Phase 3 — Data ingestion mastery

**Scope:** Saif themes 9-11 — data inputs deep dive, capstone, data onboarding.

**Course coverage:** Lectures 46-68.

**Chapters:**

### Chapter 3.1 — Data inputs
- Watch lectures 46-53
- **Lab:** configure monitoring inputs with wildcards, host_regex, whitelist. Set up a network input. Wire HEC. Run a scripted input.
- Write `03-topics/data-inputs-catalogue.md` — every input type with when-to-use and config minimal example.

### Chapter 3.2 — Capstone (adapted for Azure)
- Watch lectures 54-61 (Saif's AWS capstone). Translate to Azure as you go.
- **Lab:** this is the big one. Build the full diagram (well, a simplified version — clustering comes in Phase 4):
  - 1 IDX (clustering deferred to Phase 4)
  - 1 SH (SHC deferred to Phase 4)
  - 1 HF
  - 1 DS, 1 LM (collocated)
  - UFs on Win + Linux + AD DC
  - pfSense → HF → IDX (for syslog)
- Document every `az` CLI command in `05-labs/azure-setup/azure-cli-commands.md`.
- Write `05-labs/runbooks/distributed-deployment.md`.

### Chapter 3.3 — Data onboarding
- Watch lectures 62-68
- **The other most important infra concept:** props/transforms and the parsing pipeline. Where SPL-level skills become infrastructure-level skills.
- **Lab:** onboard pfSense logs through the HF — get sourcetype right, event breaking right, field extractions in props.conf. Use SEDCMD to mask sensitive fields.
- Write `03-topics/props-transforms.md` — the synthesis. Include the parsing pipeline phases and which conf goes where.
- Write `05-labs/runbooks/data-onboarding-fortigate-or-pfsense.md`.

### Chapter 3.4 — Course retrospective
- Mark `02-course-saif/course-index.md` complete.
- Write `03-topics/saif-course-retrospective.md` — what the course did well, what it skipped, what I disagree with.

### Chapter 3.5 — Bundle for NBLM
- Three bundles: `03-data-inputs`, `03-distributed-lab`, `03-data-onboarding`.
- Big NBLM session. This is also when I'd consider doing a *meta-bundle* covering everything for exam prep.

**Phase 3 done when:**
- [ ] All 68 Saif lectures watched, all checkboxes ticked
- [ ] Lab has full distributed Splunk running (pre-clustering version)
- [ ] pfSense logs are flowing end-to-end with proper sourcetype and field extractions
- [ ] Three synthesis notes done
- [ ] Three runbooks done
- [ ] Three NBLM bundles complete
- [ ] Saif course retrospective written
- [ ] Power User practice exam attempted at least once (light prep — most content is daily work)
- [ ] Admin practice exam attempted at least once (cold — measure baseline)

---

## Phase 4 — Beyond Saif: Clustering and HA

**Scope:** Indexer clustering + Search Head Clustering + Monitoring Console. **This is what Saif's course skipped.**

**Source material:** Splunk docs (the "Distributed Deployment Manual" is essential), Splunk's free EDU courses if accessible, supplementary YouTube/blogs.

**Chapters:**

### Chapter 4.1 — Indexer clustering
- Read Splunk docs cover-to-cover on indexer clustering.
- **Lab:** scale lab to 3 indexers. Stand up CM in Mgmt subnet. Configure RF=2, SF=2 (lab-sized). Test peer failure: shut down an IDX, watch fixup tasks.
- Write `06-supplementary/indexer-clustering.md` — full synthesis. Multi-site is out of scope unless I get curious.
- Runbook: `05-labs/runbooks/indexer-cluster-setup.md`.

### Chapter 4.2 — Search Head Clustering
- Read SHC docs.
- **Lab:** scale lab to 3 SH. Stand up SHC Deployer in Mgmt subnet. Form the cluster. Test captain election.
- Write `06-supplementary/search-head-clustering.md`.
- Runbook: `05-labs/runbooks/shc-setup.md`.

### Chapter 4.3 — Monitoring Console
- Stand up MC in Mgmt subnet. Configure it for distributed monitoring of the whole lab.
- Write `06-supplementary/monitoring-console.md`.

### Chapter 4.4 — Bundle for NBLM
- One bundle: `04-clustering-and-ha`. All three topics fit in one notebook.

### Chapter 4.5 — Take SPLK-1003 Admin exam
- Drill weak areas using NBLM quizzes from all bundles.
- Schedule the exam when practice exam scores stabilize at 80%+.
- Update `handoff.md` with exam result.

**Phase 4 done when:**
- [ ] Lab has 3-IDX cluster + 3-SHC + MC running
- [ ] Three supplementary topic notes done
- [ ] Three runbooks done
- [ ] One NBLM bundle complete
- [ ] **SPLK-1003 Admin certification passed**

---

## Phase 5 — Enterprise Security admin

**Scope:** Install ES on the SHC, onboard data through CIM, build/tune correlation searches (from the infra side this time), manage threat intel.

**Source material:** Splunk's ES admin docs + the SPLK-3001 exam blueprint.

**Chapters:**

### Chapter 5.1 — Install ES
- Install ES on the SHC.
- Configure data models for CIM compliance.

### Chapter 5.2 — Threat intel and correlation
- Configure threat intel framework.
- Tune the OOTB correlation searches.
- This phase plays to my existing strengths — go fast where I already know the material, slow down where infrastructure surfaces (data model acceleration, threat intel framework configs).

### Chapter 5.3 — UBA integration (stretch)
- If budget allows. UBA is heavy.

### Chapter 5.4 — Take SPLK-3001 ES Admin exam

**Phase 5 done when:**
- [ ] ES running on SHC, fed by CIM-compliant data
- [ ] Correlation searches tuned and producing notable events
- [ ] **SPLK-3001 ES Admin certification passed**

---

## Phase 6 — Architect mindset (stretch / open-ended)

**No clear end state.** This is the long tail: capacity planning, multi-site, ITSI, SOAR, edge processors, federated search, cluster bridge, customer scenarios.

**Possible chapters:**
- Multi-site indexer clustering
- Sizing exercises (S2 worksheet, hot/warm/cold tiering)
- ITSI overview and use cases
- SOAR integrations
- Cluster bridge between two deployments
- Federated search
- Splunk on Kubernetes (OpenShift via SOK)
- **SPLK-2002 Architect certification**

This phase is where the portfolio gets really interesting — write public blog posts, contribute to Splunk community, give talks. The repo becomes a teaching artifact, not just a learning one.

---

## Where I am right now

> Update this when phases complete.

- **Current phase:** Phase 0 — Setup
- **Next phase:** Phase 1 — Foundations
- **Last phase milestone:** none yet

---

## Rules of engagement

1. **Don't skip phases.** Even when something looks easy (e.g., Power User-level content in Phase 1), do the lab work. The cert is incidental; the muscle memory matters.
2. **Phases overlap is OK.** If I'm watching Phase 2 lectures while still finishing a Phase 1 synthesis, fine. But close one phase fully before starting the next.
3. **Synthesis before NBLM.** Don't bundle for NBLM before writing the `03-topics/` synthesis. NBLM amplifies what you give it.
4. **No deadlines, but momentum.** If two weeks pass with no lab journal entry, something's off. The repo's recent activity should reflect real engagement.
5. **Public repo means accountability.** Visible commit history is the deadline.
