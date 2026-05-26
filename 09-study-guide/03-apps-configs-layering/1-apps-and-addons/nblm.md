# NBLM generation — Topic 03.1 · Apps & Add-ons

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Splunk apps and add-ons`
- **KEY DISTINCTIONS:** `app (UI/solution) vs add-on (UI-less reusable component) and how a vendor solution ships as both; what a TA is and its role in CIM/Enterprise Security; the app directory anatomy (default vs local, metadata, bin); installing via web vs CLI (untar + chown) and why a reload/restart is needed; sharing scopes private/app/global`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on Splunk apps and add-ons. Prioritize understanding and the trade-offs an
admin makes. Make sure to clearly explain: app (a UI/solution) vs add-on (a UI-less reusable
component) and how one vendor solution often ships as both; what a Technology Add-on (TA) is and
its role in CIM normalization and Enterprise Security; the app directory anatomy (default vs
local, metadata, bin); installing via the web vs the CLI (untar into etc/apps + chown) and why a
reload/restart is needed for changes to go live; and the three sharing scopes (private/app/global).

Keep it concrete — use the Cisco app + add-on example (the add-on parses, the app visualizes).
Call out common misconceptions (editing default vs local, "the add-on has no dashboards", deleted
app still showing until reload). Near the end, pose a few of the drill questions so the listener
can self-check. Energetic and conversational, but dense and precise — this is learning, not
entertainment. Aim for a thorough episode of roughly 25–30 minutes — go deep enough to fill that,
but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of Splunk apps and add-ons
at an administrator level. Mix recall with scenario questions ("you installed an add-on but see no
dashboard — why?"; "you edited default/ and a change vanished after upgrade — why?"). Target:
app vs add-on, TA/CIM, default vs local, web vs CLI install + reload, sharing scopes. Explain each answer.
```

## Flashcards
```
Make flashcards on Splunk apps and add-ons. Front = term/scenario; back = a tight, precise
definition or rule. Include app-vs-add-on, the app subdirectories and their purpose, the install
steps, and the three sharing scopes.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
