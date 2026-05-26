# NBLM generation — Topic 02.2 · Installation & Post-Install Setup (Linux & Windows)

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `installing Splunk Enterprise on Linux and Windows, plus mandatory OS best practices`
- **KEY DISTINCTIONS:** `the Linux tarball install sequence and why chown/non-root matters; running under systemd with boot-start; why THP must be disabled (both enabled and defrag) and the ≥30% performance hit; the recommended ulimit values and where they go under systemd vs limits.conf; the Windows MSI service-account decision; verifying with the Monitoring Console health check`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on installing Splunk Enterprise on Linux and Windows plus the mandatory OS
best practices. Prioritize the "why" behind each step. Make sure to clearly explain: the Linux
tarball install sequence and why non-root + chown matter; running under systemd with enable
boot-start; why Transparent Huge Pages must be disabled (BOTH enabled and defrag) and the ≥30%
performance impact; the recommended ulimit values (nofile 64000, nproc 16000, fsize unlimited)
and where they belong under systemd vs limits.conf; the Windows MSI install and its
service-account decision; and verifying health with the Monitoring Console.

Keep it concrete and practical (this is a procedure-heavy topic — treat it like a workflow
guide: what you do, what breaks, how you'd fix it). Call out the common mistakes (forgetting
chown, non-persistent THP, ulimit not applying under systemd). Near the end, pose a few drill
questions so the listener can self-check. Energetic and conversational, but dense and precise.
Aim for a thorough episode of roughly 25–30 minutes — go deep enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of installing Splunk on
Linux/Windows and the OS best practices, at an administrator level. Mix recall with
troubleshooting scenarios (e.g. "THP shows 'always' after reboot — what went wrong?"; "ulimits
not applying to a systemd-managed Splunk — why?"). Target: install sequence/chown, boot-start
systemd, THP (both enabled+defrag), ulimit values and placement, Windows service account.
Explain each answer.
```

## Flashcards
```
Make flashcards on installing Splunk and the OS best practices. Front = command/term/value or
scenario; back = tight definition or the exact value/command. Include the ulimit numbers, the
THP verify paths, the boot-start command, and the Windows service-account options.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
