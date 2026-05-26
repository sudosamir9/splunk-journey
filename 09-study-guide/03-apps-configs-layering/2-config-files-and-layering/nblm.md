# NBLM generation — Topic 03.2 · Configuration Files & Layering / Precedence

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Splunk configuration files and the layering / precedence model`
- **KEY DISTINCTIONS:** `the .conf stanza/attribute format (case-sensitive); the etc/system, etc/apps, etc/users structure and default vs local; the two contexts and their different precedence orders (global/index-time: system/local first; app-user/search-time: user/current-app first, system near bottom); lexicographic ASCII app ordering (numbers > uppercase > lowercase); how merging works per attribute (conflict → highest wins, else union); using btool to find the effective value and its source`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on Splunk configuration files and the layering / precedence model. This is
one of the most important admin topics, so go deep. Make sure to clearly explain: the .conf
stanza/attribute format and case sensitivity; the etc/system, etc/apps, etc/users structure and
the default-vs-local rule; the TWO contexts and why their precedence orders differ — global
(index-time) puts system/local first, while app/user (search-time) puts the user and current app
first with system near the bottom; lexicographic ASCII app ordering (numbers > uppercase >
lowercase) and how admins exploit it; how merging works per attribute (conflict → highest
precedence wins, non-conflict → union); and using btool to find the effective value and its source.

Keep it concrete — walk through a worked inputs.conf merge across system/local, two apps' local,
and system/default, choosing the winner for each attribute. Call out the common confusions
(precedence differs by context; editing default; "nothing changed" = override or no reload). Near
the end, pose a few of the drill questions so the listener can self-check. Energetic and
conversational, but dense and precise — this is learning, not entertainment. Aim for a thorough
episode of roughly 25–30 minutes — go deep enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of Splunk configuration
layering and precedence at an administrator level. Mix recall with scenario questions (given copies
of a conf file in several directories with conflicting attributes, what's the effective value?;
which of two apps wins by ASCII order?; index-time vs search-time precedence). Target: default vs
local, the two contexts' orders, lexicographic ordering, per-attribute merge, btool. Explain each answer.
```

## Flashcards
```
Make flashcards on Splunk configuration layering and precedence. Front = term/scenario; back = a
tight rule or ordering. Include the global vs app/user precedence orders, the lexicographic ASCII
rule, default-vs-local, the merge rule (conflict vs union), and the btool command.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
