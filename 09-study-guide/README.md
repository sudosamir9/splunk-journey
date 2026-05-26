# Study Guide — enhanced + pre-class material

Course-aligned study material derived from the course transcripts, enhanced with current Splunk-docs research (2026). Two layers per **topic**:

- **`enhanced.md`** — deep, self-contained reference written as general Splunk material (no course/instructor references, reusable anywhere). **This is the NBLM source** (upload to generate podcasts, quizzes, flashcards, mind maps).
- **`pre-class.md`** — short primer to read *before* watching the lecture; pairs with the audio overview, and holds the official-doc reference links.

## Layout
```
09-study-guide/<NN-theme>/<n-topic>/{enhanced.md, pre-class.md}
```
Each **topic folder = one NBLM bundle = one optional podcast.** Themes mirror `02-course-saif/transcripts/`. A theme may hold one topic (small) or several (large themes are split for quality).

## Coverage map (topic → course lectures)

| Theme | Topic folder | Topic | Covers | Status |
|---|---|---|---|---|
| 01 Fundamentals | `1-fundamentals-and-architecture` | Fundamentals & Architecture | 1–4 | ✅ done |
| 02 Install & best practices | `1-prerequisites-and-sizing` | Prerequisites & sizing | 5–8 | ✅ done |
| 02 Install & best practices | `2-installation-linux-and-windows` | Installation & post-install setup: Linux + Windows | 9–16 | ✅ done |
| 03 Apps, configs, layering | `1-apps-and-addons` | Apps & add-ons | 17–18 | ✅ done |
| 03 Apps, configs, layering | `2-config-files-and-layering` | Configuration files & layering/precedence | 19–21 | ✅ done |
| 04 Indexes, buckets, retention | `1-indexes-and-bucket-lifecycle` | Indexes & bucket lifecycle | 22–24 | ✅ done |
| 04 Indexes, buckets, retention | `2-managing-indexes-and-fishbucket` | Managing indexes, backup/deletion & the fishbucket | 25–28 | ✅ done |
| 05 Users, roles, LDAP | `1-users-roles-and-ldap` | Users, roles & LDAP authentication | 29–30 | ✅ done |
| 06 Forwarders & distributed | `1-uf-and-forwarding-to-indexers` | Universal forwarders & forwarding to indexers | 31–33 | ✅ done |
| 06 Forwarders & distributed | `2-windows-forwarders-and-distributed-sh` | Windows forwarders & distributed search head | 34–36 | ✅ done |
| 07 Data flow concepts | `1-collection-metadata-sourcetypes` | Data collection, metadata & sourcetypes | 37–39 | ✅ done |
| 07 Data flow concepts | `2-routing-loadbalancing-event-breaking` | Routing, load balancing, event breaking & forwarder strategy | 40–43 | ✅ done |
| 08 Deployment Server | `1-deployment-server-and-server-classes` | Deployment Server, clients & server classes | 44–45 | ✅ done |
| 09 Data inputs deep dive | `1-monitoring-inputs-files-directories` | Monitoring inputs — files & directories | 46–50 | ✅ done |
| 09 Data inputs deep dive | `2-network-scripted-hec-inputs` | Network, scripted & HEC inputs | 51–53 | ✅ done |
| 10 Capstone (cloud-agnostic + Azure) | `1-distributed-buildout-components-forwarders` | Distributed build-out: components & forwarders | 54–58 | ✅ done |
| 10 Capstone (cloud-agnostic + Azure) | `2-base-apps-usecases-hf-firewall` | Base apps via DS, forwarder use cases & HF/firewall logs | 59–61 | ✅ done |
| 11 Data onboarding | `1-onboarding-parsing-props-transforms` | Onboarding & parsing with props/transforms | 62–65 | ✅ done |
| 11 Data onboarding | `2-field-extraction-sedcmd-masking` | Field extraction, SEDCMD & data masking | 66–68 | ✅ done |

**19 topics total.** Each topic folder holds `enhanced.md` + `pre-class.md` + `nblm.md`. Topics are sized so each sustains a ~25–30 min podcast — thin/short lectures are merged into a substantial neighbour rather than split out.
