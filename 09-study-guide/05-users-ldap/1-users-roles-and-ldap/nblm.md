# NBLM generation — Topic 05.1 · Users, Roles & LDAP

**Source to upload:** `enhanced.md` (optionally also `pre-class.md`). One notebook for this topic.

Slots:
- **TOPIC NAME:** `Splunk users, roles, capabilities, and LDAP integration`
- **KEY DISTINCTIONS:** `authentication (who are you?) vs authorization (what can you do?) as separate layers; the five built-in roles (admin, power, user, can_delete, splunk-system-role) and their purpose; role inheritance (importRoles — additive, cannot remove inherited capabilities); the authorize.conf role stanza (srchIndexesAllowed, srchIndexesDefault, srchFilter, srchJobsQuota, srchDiskQuota, rtSrchJobsQuota); multiple roles are additive/most-permissive (quotas take maximum); authentication order when native + LDAP coexist (native-first, no fallthrough on wrong password); LDAP integration flow (bind → locate user → validate → resolve groups → roleMap lookup); authentication.conf stanza structure (bindDN, userBaseDN, groupBaseDN, roleMap_strategyName); multiple strategies and ordering; LDAPS on port 636`

---

## Podcast (Audio Overview)
Settings: **Deep Dive · Default length · English.** (Not Long — it runs ~45–60 min.)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on Splunk users, roles, and LDAP integration. This is a foundational access
control topic, so go deep on the architecture. Make sure to clearly explain: the separation
between authentication (proving identity) and authorization (granting permissions) and why
they are distinct layers — LDAP handles the first, Splunk's role model handles the second,
and the roleMap is the bridge; the five built-in roles (admin, power, user, can_delete,
splunk-system-role) and the design reasoning behind having can_delete as a standalone role;
role inheritance via importRoles (additive, cannot remove inherited capabilities, transitive);
the full authorize.conf role stanza — srchIndexesAllowed vs srchIndexesDefault, srchFilter as
a row-level restriction, srchJobsQuota/rtSrchJobsQuota/srchDiskQuota and the most-permissive
rule when a user holds multiple roles; the authentication order when native Splunk auth and
LDAP coexist (native-first, no LDAP fallthrough if local account exists with wrong password);
the end-to-end LDAP login flow step by step (bind request, user locate, credential validation,
group resolution, roleMap lookup); the authentication.conf stanza structure in detail (the
[authentication] stanza, the strategy stanza with bindDN/userBaseDN/groupBaseDN/userNameAttribute/
groupMemberAttribute, and the [roleMap_strategyName] stanza); multiple LDAP strategies and
their query ordering; SSL/LDAPS on port 636 and why plain LDAP is unacceptable in production.

Walk through a concrete custom role example: an authorize.conf stanza for a SOC analyst role
with specific index access, a srchFilter, and quotas. Then walk through what the authentication.conf
looks like for a corporate AD integration — strategy stanza and roleMap. Call out the key
misconceptions (auth and authz conflated; inherited capabilities can be removed; multiple roles
are restrictive not additive; srchJobsQuota is summed; LDAP group membership is stored in Splunk).
Near the end, pose a few of the drill questions so the listener can self-check.

Energetic and conversational, but dense and precise — this is learning, not entertainment.
Aim for a thorough episode of roughly 25–30 minutes — go deep enough to fill that, but don't pad.
```

## Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of Splunk users, roles,
and LDAP integration at an administrator level. Mix recall with scenario questions — for example:
given two roles with different quotas assigned to one user, what is the effective limit and why?;
a user fails login with native auth — does Splunk try LDAP next?; what happens when an LDAP user's
group is not in the roleMap?; write or interpret an authorize.conf stanza for a custom role.
Target: authentication vs authorization distinction, built-in roles and their purpose,
role inheritance (importRoles) and the lock on inherited capabilities, the authorize.conf stanza
attributes (srchIndexesAllowed, srchIndexesDefault, srchFilter, quotas), the additive/most-
permissive rule for multiple roles, the authentication order for native + LDAP, and the
authentication.conf stanza structure (bindDN, userBaseDN, groupBaseDN, roleMap_). Explain each answer.
```

## Flashcards
```
Make flashcards on Splunk users, roles, capabilities, and LDAP integration. Front = term or
scenario; back = a tight rule or definition. Include: authentication vs authorization (one-line
each); the five built-in roles and their key characteristic; the importRoles inheritance rule
(what is inherited, what cannot be changed); the multiple-roles rule (additive capabilities,
maximum quotas); srchIndexesAllowed vs srchIndexesDefault; what srchFilter does; the
authentication order when native + LDAP coexist; the LDAP login flow in 4–5 steps; the
[roleMap_strategyName] stanza format; why LDAPS (port 636) not plain LDAP.
```

## Mind map & Infographic
No prompt — generated from `enhanced.md`. Keep it the only source so the output stays scoped to this topic.
