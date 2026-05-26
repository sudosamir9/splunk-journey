# NBLM generation — Topic 09.1 · Data Inputs: Monitoring Files and Directories

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Splunk monitor inputs — files, directories, wildcards, and the fishbucket`
- **KEY DISTINCTIONS:** `the [monitor://] stanza and its attributes (index, sourcetype, host, disabled, followTail, recursive); monitoring a file vs a directory; the two wildcards (* = single segment, ... = recursive multi-segment) and what each matches; host_segment vs host_regex for dynamic host derivation (mutually exclusive); allowlist/denylist regex filtering with denylist precedence; the fishbucket (CRC fingerprint + seek offset, location, what clearing it does); crcSalt = <SOURCE> to prevent CRC collision; batch (destructive, move_policy = sinkhole) vs monitor vs oneshot`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on Splunk data inputs — specifically the monitor input for files and
directories. Go deep on: the [monitor://] stanza and its full attribute set (index,
sourcetype, host, disabled, followTail, recursive, crcSalt, initCrcLength); the critical
difference between the two path wildcards — * matches within one path segment and never
crosses directory separators, while ... crosses any number of directory levels recursively;
how host_segment and host_regex extract a useful host value from the file path (and why
they're mutually exclusive); allowlist/denylist regex filters applied to the full path (and
that denylist wins on conflict); and the fishbucket — what it stores (CRC fingerprint of
the first N bytes plus the byte-offset read so far), why CRC collisions occur on
identical-header files, and how crcSalt = <SOURCE> fixes them. Also cover batch vs
monitor vs oneshot clearly: monitor is continuous and non-destructive; batch is one-shot
and deletes the file (requires move_policy = sinkhole); oneshot is a CLI command with no
persistent stanza. Walk through a realistic inputs.conf example collecting from a
multi-server directory tree. Call out the classic mistakes: using * when you meant ...,
forgetting crcSalt on identical-header files, clearing the fishbucket in production. Aim
for a thorough episode of roughly 25–30 minutes — go deep enough to fill that, but don't
pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of Splunk monitor
inputs at an administrator level. Mix recall with scenario questions: given a directory
tree, which wildcard expression matches which files?; if two files share identical first
256 bytes, what goes wrong and how do you fix it?; a colleague cleared the fishbucket on
a production forwarder — what happens next?; when would you choose host_regex over
host_segment? Cover: * vs ... wildcard behavior, allowlist/denylist precedence, fishbucket
mechanics, crcSalt, followTail semantics, batch vs monitor vs oneshot. Explain each
answer.
```

## Flashcards
```
Make flashcards on Splunk monitor inputs. Front = term, attribute, or scenario; back = a
tight rule or definition. Include: [monitor://] stanza purpose, * wildcard rule, ...
wildcard rule, host_segment vs host_regex (and their mutual exclusivity), allowlist vs
denylist (and precedence), fishbucket contents and location, crcSalt = <SOURCE> purpose,
followTail = 1 behavior, batch input key differences from monitor.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
