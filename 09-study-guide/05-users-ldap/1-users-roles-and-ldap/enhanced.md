---
type: enhanced
theme: 05-users-ldap
topic: users-roles-and-ldap
covers: "Lectures 29–30"
tags: [study-guide/enhanced, theme/05-users-ldap]
sources: docs.splunk.com (Splunk 9.x / latest, 2026)
---

# Users, Roles & LDAP

> Deep reference on Splunk access control: the two-layer model of authentication (who are you?) and authorization (what can you do?); the full roles and capabilities system including built-in roles, `authorize.conf` stanzas, index access controls, and search restrictions; creating and managing users and custom roles via Splunk Web and the CLI; and integrating with LDAP/Active Directory via `authentication.conf` — strategies, bind accounts, user/group base DNs, role mapping, multiple strategies, and SSL. This is one of the most operationally critical admin topics — nearly every "why can't this user see this data?" traces back to it. Companion `pre-class.md` holds the short primer and official-doc links.

---

## 0. Orientation

Splunk's access control system has two distinct, separable layers:

1. **Authentication** — proves the identity of the person logging in. Answers: *who is this person, and are they who they claim to be?*
2. **Authorization** — determines what that authenticated identity is allowed to do. Answers: *which indexes can this user search, which capabilities do they hold, what data can they see?*

These two layers can use completely different mechanisms. In the most common enterprise scenario, **authentication is handled by LDAP/Active Directory** and **authorization is handled by Splunk's role system**. The bridge between them is the LDAP group-to-role mapping: LDAP proves identity; Splunk's role model grants permissions.

Understanding this separation is the foundation of everything in this topic.

---

## 1. Authentication — options and order

Splunk supports four authentication mechanisms:

| Mechanism | How it works | Typical use |
|---|---|---|
| **Splunk (native)** | Credentials stored in `$SPLUNK_HOME/etc/passwd`; Splunk validates locally | Dev, small deployments, break-glass accounts |
| **LDAP** | Splunk binds to an LDAP/AD server; that server validates the credential | Most enterprise deployments |
| **SAML/SSO** | Browser-based SSO via a SAML 2.0 Identity Provider (Okta, ADFS, etc.) | Large orgs with centralized SSO |
| **Scripted** | Custom external script validates credentials | Edge cases, legacy, non-standard directories |

**Authentication order (native + LDAP configured):**

When both native and LDAP are configured, Splunk applies this sequence:

1. If the user has a native (local) Splunk account, attempt native authentication first.
2. If native authentication succeeds → grant access based on the local account's roles.
3. If the account exists locally but the password fails → **stop; do not fall through to LDAP**. This prevents a local shadow account from being bypassed by a valid LDAP password.
4. If no local account exists for that username → fall through and attempt LDAP.

This ordering is important for security: having a local account for a username creates a definitive gate — LDAP will never be tried for that account unless you remove the local one. The practical implication: always keep a local `admin` account as a break-glass credential, and manage most users through LDAP.

---

## 2. The roles and capabilities model

**Authorization in Splunk is entirely role-based.** There are no per-user permission grants — every permission a user holds comes from one or more roles assigned to that user. Understanding roles is understanding authorization.

### 2.1 What a role contains

A role bundles three types of settings:

| Setting type | Controls |
|---|---|
| **Capabilities** | Granular permissions (search, edit_user, indexes_edit, schedule_search, etc.) |
| **Index access** | Which indexes the role is allowed to search (`srchIndexesAllowed`) and which are searched by default (`srchIndexesDefault`) |
| **Search restrictions** | Quotas and filters: `srchFilter`, `srchJobsQuota`, `srchDiskQuota`, `rtSrchJobsQuota` |

### 2.2 Users holding multiple roles

A user can be assigned more than one role. The effective permissions are a **union** — the user receives the most permissive combination of all their roles. If role A grants capability X and role B does not, the user still has capability X. If role A allows index `security` and role B allows index `network`, the user can search both.

This means roles are additive. The only way to restrict a permission is to ensure none of the user's roles grant it.

---

## 3. Built-in roles

Splunk ships with five built-in roles:

| Role | Purpose | Key characteristics |
|---|---|---|
| `admin` | Full administrative access | All capabilities; can edit all objects and settings; the highest-privilege human role |
| `power` | Power user | Can create and share objects (reports, dashboards) with other users; can tag events; cannot make system-level changes |
| `user` | Standard user | Can create and run searches; can save personal objects; limited to objects shared to them |
| `can_delete` | Allows the `\| delete` search command | Not normally assigned directly; added to a user who needs to delete indexed events using `\| delete` |
| `splunk-system-role` | Internal service-level identity | Used for inter-component communication (e.g., connecting a search head to indexer peers); not for human users |

A few important details:

- `can_delete` exists as a standalone role specifically because the `| delete` operator is dangerous — it permanently removes events from an index. Keeping this capability in its own dedicated role forces an explicit assignment decision. You add it to an existing user as a second role; you don't normally have a user whose *only* role is `can_delete`.

- `splunk-system-role` enables system-level services to run without a defined user context. When connecting distributed components (e.g., adding an indexer as a search peer on a search head), best practice is to create a dedicated service account user and assign this role rather than using an `admin` account for the connection. This follows the principle of least privilege for inter-component trust.

- The `user` role is the **floor** — all other roles implicitly inherit from it through the role inheritance chain built into the defaults.

---

## 4. Role inheritance

Roles can import (inherit) other roles. When role B imports role A:

- **All capabilities** that role A grants are automatically granted to role B — and cannot be removed. Inherited capabilities show as read-only in Splunk Web.
- **All index access** that role A allows is added to role B.
- **Inheritance is additive and transitive.** If C imports B, and B imports A, then C has everything from both A and B plus its own direct grants.
- You can import multiple roles. The result is the union of all imported roles plus the role's own settings.

This is the mechanism for building layered roles: create a base role with shared permissions, then create more specific roles that import the base. Never grant wide permissions to individuals — grant them a role that inherits the minimum necessary base.

```
[authorize.conf — inheritance example]

[role_soc_analyst]
importRoles = user
srchIndexesAllowed = security;network;endpoint
srchIndexesDefault = security
srchJobsQuota = 10
```

`importRoles` takes a semicolon-separated list. The role above inherits all `user` capabilities and adds specific index access.

---

## 5. `authorize.conf` — the role definition file

All roles live in `$SPLUNK_HOME/etc/system/local/authorize.conf` (for system-wide roles) or in an app's `local/authorize.conf`. The stanza format is `[role_<roleName>]`.

**Important:** never edit `$SPLUNK_HOME/etc/system/default/authorize.conf`. Changes there are overwritten on upgrade.

### 5.1 Complete stanza reference

```ini
[role_<roleName>]

# Role inheritance
importRoles = <role1>;<role2>

# Index access
srchIndexesAllowed = <index1>;<index2>;*
srchIndexesDefault = <index1>;<index2>

# Capabilities (each listed = granted to this role)
# (see Section 6 for the full capability list)

# Search quotas
srchJobsQuota       = <integer>   # max concurrent scheduled+ad-hoc jobs
rtSrchJobsQuota     = <integer>   # max concurrent real-time search jobs
srchDiskQuota       = <MB>        # total disk a user's jobs may consume

# Search filter (row-level restriction)
srchFilter          = <SPL-filter-expression>
```

**`srchIndexesAllowed` and `srchIndexesDefault`:**

- `srchIndexesAllowed` — the set of indexes this role is *permitted* to search. Use `*` for all (but note: `_internal`, `_audit`, etc., are still restricted by separate capabilities). Separate multiple values with semicolons.
- `srchIndexesDefault` — the indexes searched when the user does not specify an index in their search. This must be a subset of (or equal to) `srchIndexesAllowed`. If a user holds multiple roles, the effective `srchIndexesDefault` is the union of all roles' defaults.

**`srchFilter`:**

A search-filter expression that restricts what events a user can see. For example, `srchFilter = host=webserver*` means users with this role can only see events where `host` matches `webserver*`. The filter is applied as an implicit AND to every search — the user cannot opt out of it. This is a powerful row-level security tool but has performance implications at scale.

**`srchJobsQuota` and `rtSrchJobsQuota`:**

Cap the number of concurrent jobs. When a user holds multiple roles, the **highest quota wins** — quotas are not summed, they take the maximum across all assigned roles.

**`srchDiskQuota`:**

The maximum disk space (MB) all of a user's jobs may consume simultaneously. Again, the maximum across all roles wins.

### 5.2 A worked custom role example

Scenario: a SOC analyst needs to search security and endpoint indexes, see only events from a specific host range, run up to 10 jobs, and not be able to edit saved searches belonging to others.

```ini
[role_soc_tier1]
importRoles         = user
srchIndexesAllowed  = security;endpoint;network
srchIndexesDefault  = security
srchFilter          = host=prod-*
srchJobsQuota       = 10
rtSrchJobsQuota     = 3
srchDiskQuota       = 200
```

This role does not import `power`, so the analyst cannot share objects or edit others' saved searches. They inherit only `user` capabilities, restricting them to personal objects and basic search.

---

## 6. Capabilities — the granular permission layer

Capabilities are the individual atomic permissions within a role. There are dozens; these are the most consequential for an administrator to know:

| Capability | What it grants |
|---|---|
| `admin_all_objects` | Full read/write access to all objects on the system |
| `edit_user` | Create, modify, and delete users |
| `change_own_password` | Change the user's own password |
| `change_authentication` | Modify authentication settings |
| `indexes_edit` | Create, modify, and delete indexes |
| `edit_roles` | Create and modify roles |
| `schedule_search` | Create scheduled searches and alerts |
| `rest_apps_management` | Install and manage apps via REST |
| `search` | Run searches (every interactive user needs this) |
| `real_time_search` | Run real-time searches |
| `rtsearch` | Same as `real_time_search` in some contexts |
| `delete_by_keyword` | Delete events using `\| delete` (the `can_delete` capability) |
| `get_diag` | Generate a `diag` bundle (diagnostic archive) |
| `edit_sourcetypes` | Modify sourcetype definitions |
| `list_inputs` | View data inputs |
| `edit_inputs_*` | Edit specific input types |

**Naming convention:** capabilities whose names begin with `edit_` generally grant full CRUD (create, read, update, delete) for the named feature. `list_` capabilities grant read-only visibility.

Capabilities are defined in `authorize.conf` under the role stanza. Each listed capability is granted; capabilities not listed are not granted. There is no explicit "deny" — the absence of a capability is the denial.

---

## 7. Where users live: `passwd` and `users.conf`

Native Splunk users are stored in two places:

- **`$SPLUNK_HOME/etc/passwd`** — hashed passwords for native auth. Splunk manages this file; do not edit it by hand. The password hashing algorithm is configurable in `authentication.conf` (`passwordHashAlgorithm`; default is a SHA-512-based crypt variant in modern Splunk versions).

- **`$SPLUNK_HOME/etc/users/<username>/user-prefs/local/user-prefs.conf`** — per-user preferences.

Role assignments for native users are stored in `$SPLUNK_HOME/etc/system/local/user-seed.conf` (for the initial `admin` seed) and in `authorize.conf` indirectly via role stanzas — but the **user → role assignment** is recorded in Splunk's internal user store and reflected in the Splunk Web UI under Settings > Access controls > Users.

When LDAP is in use, there is no Splunk-local password entry for LDAP users — they authenticate externally. Their role membership is determined at login by the LDAP group-to-role mapping, not stored persistently.

---

## 8. Password policy

Password policies apply **only to native Splunk authentication**. When LDAP or SAML is configured, password policy is managed by the external identity provider — Splunk's password settings have no effect on those users.

Key settings in `authentication.conf` under `[splunk_auth]`:

```ini
[splunk_auth]
minPasswordLength    = 8
minPasswordUppercase = 1
minPasswordLowercase = 1
minPasswordSpecial   = 1
minPasswordDigit     = 1
lockoutAttempts      = 5
lockoutThresholdMins = 30
lockoutMins          = 30
```

`lockoutAttempts` — number of consecutive failed logins before the account is locked. `lockoutThresholdMins` — the rolling window for those attempts. `lockoutMins` — how long the lockout lasts. These are often tightened in security-conscious deployments.

The `forceWeakPasswordChange` setting, if set to `true`, forces users to change a password that doesn't meet current policy on next login. This is useful when tightening policy on an existing deployment.

---

## 9. Creating users and roles — Web and CLI

### 9.1 Via Splunk Web

Navigate to **Settings → Access controls → Users** (or Roles). Both paths are straightforward:

- **New user:** provide username, display name (optional), email (optional), password, role(s). Uncheck "Require password change on first login" if managing credentials programmatically.
- **New role:** provide role name, import roles (optional), select capabilities, configure index access and quotas.

Changes via Splunk Web write immediately to `authorize.conf` (for roles) and Splunk's internal user store.

### 9.2 Via the CLI (`splunk` command)

```bash
# Add a user
splunk add user samir -role analyst -password 'S3cr3t!' -auth admin:adminpass

# Edit a user's role
splunk edit user samir -role analyst -role soc_tier1 -auth admin:adminpass

# Remove a user
splunk remove user samir -auth admin:adminpass

# List users
splunk list user -auth admin:adminpass

# Add a role (note: complex roles are better done via conf file)
splunk add role soc_tier1 -auth admin:adminpass
```

### 9.3 Via `authorize.conf` directly

For custom roles with specific stanza settings (quotas, filters), editing `authorize.conf` directly gives the most control and is the recommended approach for automation/IaC:

```bash
# After editing $SPLUNK_HOME/etc/system/local/authorize.conf
splunk reload auth   # or: splunk restart
```

A reload of auth (`splunk reload auth`) is sufficient for most role changes. A full restart is not required for `authorize.conf` edits in most cases, but is needed for some authentication method changes.

---

## 10. LDAP integration — architecture

The LDAP integration follows a clear sequence:

```
User enters username + password in Splunk Web
          │
          ▼
Splunk sends a bind request to the LDAP server
using the configured service account (bindDN + password)
          │
          ▼
LDAP server locates the user object
          │
          ▼
Splunk sends user's credentials to LDAP for validation
          │
          ▼
LDAP returns success/failure + group memberships
          │
          ▼
Splunk looks up the user's groups in the roleMap stanza
→ maps each LDAP group to one or more Splunk roles
          │
          ▼
User is logged in with the union of all mapped roles
```

The critical separation: **LDAP handles authentication** (proving identity), **Splunk's role system handles authorization** (granting permissions). The roleMap is the bridge.

---

## 11. `authentication.conf` — full LDAP configuration

LDAP configuration lives in `$SPLUNK_HOME/etc/system/local/authentication.conf`. There are two stanza types for LDAP:

1. A **`[authentication]`** stanza — declares that LDAP is in use and lists the strategy names.
2. One **`[<strategyName>]`** stanza per LDAP server — contains the connection and search parameters.
3. One **`[roleMap_<strategyName>]`** stanza per strategy — maps LDAP groups to Splunk roles.

### 11.1 The `[authentication]` stanza

```ini
[authentication]
authType     = LDAP
authSettings = ldap_corp
```

`authSettings` is a comma-separated list of strategy names (stanza names defined below). The order here determines the order in which Splunk queries LDAP servers when the user's account is not found in an earlier strategy.

### 11.2 The strategy stanza

```ini
[ldap_corp]
host                = ad.corp.example.com
port                = 636
SSLEnabled          = 1
bindDN              = CN=splunk-svc,OU=ServiceAccounts,DC=corp,DC=example,DC=com
bindDNpassword      = <encrypted-at-rest-by-Splunk>
userBaseDN          = OU=Users,DC=corp,DC=example,DC=com
userBaseFilter      = (objectClass=person)
userNameAttribute   = sAMAccountName
realNameAttribute   = cn
emailAttribute      = mail
groupBaseDN         = OU=Groups,DC=corp,DC=example,DC=com
groupBaseFilter     = (objectClass=group)
groupNameAttribute  = cn
groupMemberAttribute= member
```

Key attributes explained:

| Attribute | Purpose |
|---|---|
| `host` | LDAP server hostname or IP |
| `port` | 389 (plain) or 636 (LDAPS/SSL). Always use 636 in production |
| `SSLEnabled` | `1` = use SSL/TLS (LDAPS); `0` = plain (development only) |
| `bindDN` | The Distinguished Name of the service account Splunk uses to bind to LDAP and search for users/groups. Should be a dedicated, low-privilege service account — not a domain admin |
| `bindDNpassword` | Password for the bindDN account. Splunk encrypts this at rest in the stored configuration |
| `userBaseDN` | The DN of the subtree (OU) where Splunk will search for user objects. Scope is the entire subtree |
| `userBaseFilter` | Optional LDAP filter to restrict which user objects are considered (e.g., `(objectClass=person)`) |
| `userNameAttribute` | The LDAP attribute that holds the login username. In Active Directory this is `sAMAccountName`; in OpenLDAP it is typically `uid` |
| `realNameAttribute` | Attribute for the user's display name (usually `cn`) |
| `emailAttribute` | Attribute for email |
| `groupBaseDN` | The DN of the subtree where Splunk searches for groups |
| `groupBaseFilter` | Optional filter for group objects |
| `groupNameAttribute` | Attribute that holds the group's name (usually `cn`) |
| `groupMemberAttribute` | Attribute on the group object that lists its members (AD: `member`; some systems: `memberOf` on user objects) |

### 11.3 The `[roleMap_<strategyName>]` stanza

```ini
[roleMap_ldap_corp]
admin   = Domain Admins;Splunk-Admins
power   = Splunk-PowerUsers
user    = Splunk-Users;Domain Users
soc_tier1 = SOC-Analysts
```

Format: `<splunk_role> = <LDAPGroup1>;<LDAPGroup2>`. Multiple LDAP groups are separated by **semicolons**. A user is assigned a Splunk role if they are a member of *any* of the listed LDAP groups for that role.

**If a user belongs to multiple mapped groups**, they receive the union of all corresponding Splunk roles — the most permissive combination, consistent with how multi-role assignment works.

**Custom roles work here too**: if you've created `soc_tier1` in `authorize.conf`, you can map LDAP groups to it in `roleMap_` just as you would a built-in role.

---

## 12. Multiple LDAP strategies

When the environment has more than one directory (e.g., a corporate AD and a partner AD):

```ini
[authentication]
authType     = LDAP
authSettings = ldap_corp,ldap_partner
```

Splunk queries strategies in the order listed. For a given login attempt:

1. Splunk tries `ldap_corp` first — binds with the service account, searches for the username in `userBaseDN`.
2. If the user is found, authentication proceeds against `ldap_corp`. If successful, group membership is resolved using `ldap_corp`'s `groupBaseDN` and `roleMap_ldap_corp`.
3. If the user is **not found** in `ldap_corp`, Splunk proceeds to `ldap_partner`.
4. If not found in any strategy, authentication fails.

Each strategy has its own independent `roleMap_<strategyName>` stanza. Users are never cross-mapped between strategies — a user found in `ldap_corp` is authorized by `roleMap_ldap_corp` only.

---

## 13. SSL/LDAPS configuration

Using plain LDAP (port 389) in production is a significant risk — credentials travel in cleartext. Always configure LDAPS (port 636) or LDAP with STARTTLS.

For LDAPS in `authentication.conf`:

```ini
[ldap_corp]
port      = 636
SSLEnabled = 1
```

Splunk also requires the LDAP server's CA certificate to be trusted. For AD environments using a private CA, you need to either:

1. Import the CA certificate into the OS trust store on the Splunk host, or
2. Reference it in Splunk's SSL configuration (`$SPLUNK_HOME/etc/system/local/server.conf` under `[sslConfig]`, `sslRootCAPath`).

The documentation also references an `ldap.conf` file for additional SSL parameter configuration when needed in complex PKI environments.

---

## 14. Configuring LDAP via Splunk Web

The Web UI path: **Settings → Access controls → Authentication method → LDAP → Configure Splunk to use LDAP and map groups**.

The Splunk Web flow:

1. **Create a new LDAP strategy** — fill in host, port, bind DN, bind password, user base DN, group base DN, and attribute mappings.
2. **Test the connection** — Splunk provides a built-in test that attempts a bind and searches for a sample user. Use this before saving.
3. **Map groups** — after the strategy is saved, navigate to the group mapping section; Splunk queries the LDAP server and presents the groups found under `groupBaseDN`. Assign each group to a Splunk role.
4. **Set authentication order** — if multiple strategies are configured, order them by priority.

The Web UI writes to `authentication.conf` exactly as if you had edited the file by hand. Reviewing the resulting file is a good way to learn the conf format — do the Web flow once, then read the file.

---

## 15. Testing and troubleshooting LDAP

**In Splunk Web:** Settings → Access controls → Authentication method → LDAP → the strategy page has a "Test" button. It attempts a bind and user search and reports success or specific errors.

**In `authentication.conf`:** after changes, run:
```bash
splunk reload auth
```
or restart. LDAP errors are logged in `$SPLUNK_HOME/var/log/splunk/splunkd.log` — search for `LDAP` or `ldap` in that log.

**Common failure modes:**

| Symptom | Likely cause |
|---|---|
| "Cannot connect to LDAP server" | Wrong host/port, network/firewall block, SSL cert untrusted |
| "Bind failed" | Wrong `bindDN` or `bindDNpassword`; service account locked/expired |
| "User not found" | `userBaseDN` points to wrong OU; `userNameAttribute` mismatch (`sAMAccountName` vs `uid`) |
| "Login succeeds but wrong roles" | `roleMap_` stanza is wrong or references a group name that doesn't match exactly |
| "Login succeeds but no roles" | User's LDAP group is not mapped in `roleMap_`; result: user has no roles, cannot do anything |
| Plain LDAP vs LDAPS port mismatch | `SSLEnabled = 1` with `port = 389` or vice versa |

When a user's LDAP group is not mapped to any Splunk role, the login technically succeeds (LDAP authenticated them) but the user will have no roles and Splunk Web will show a permissions error. This is a common misconfiguration — always verify group mapping after login.

---

## 16. Inclusive language in Splunk terminology (version note)

In Splunk 9.0+, several terms were updated to remove exclusive language. The `splunk-system-role` was previously referred to as `system` in some internal documentation. In distributed architectures, what was once called a "slave node" (for indexer clustering) is now "peer" and "cluster manager" replaces "master node." These changes affect documentation but not functional behavior.

---

## 17. Terminology & version notes

- The roles and capabilities model (`authorize.conf`) is stable across Splunk 7.x–9.x. Specific capabilities have been added over versions but the stanza format is unchanged.
- `authentication.conf` LDAP integration works the same way across 7.x–9.x. The field names (`bindDN`, `userBaseDN`, `groupBaseDN`, etc.) are stable.
- In Splunk 9.0+, the `splunk-system-role` is the recommended role for inter-component service accounts, replacing the informal practice of using the `admin` role.
- SAML configuration has expanded significantly in 9.x, particularly for Splunk Cloud, but the basic LDAP integration covered here is unchanged.
- The `roleMap_` stanza prefix is the authoritative way to do group-to-role mapping and has not changed.

---

## 18. Common misconceptions

- **"Authentication and authorization are the same thing."** They are not — authentication proves identity, authorization grants permissions. LDAP handles the first; `authorize.conf` handles the second. The roleMap bridges them.

- **"If I configure LDAP, all users authenticate through it."** No — native Splunk accounts authenticate natively first. The ordering rule means a local `admin` account always authenticates locally, regardless of LDAP configuration.

- **"Removing a capability from an imported role removes it from the child role."** Inherited capabilities cannot be removed from a child role. If you inherit from `admin`, you have all `admin` capabilities and cannot drop any of them. Design role hierarchies carefully.

- **"Users with multiple roles get the most restrictive combination."** The opposite — multiple roles are additive/most-permissive. Each role adds to what the user can do, never subtracts.

- **"srchJobsQuota is summed across roles."** No — when a user holds multiple roles with different quotas, the **maximum** quota wins, not the sum.

- **"LDAP groups are stored permanently in Splunk."** No — LDAP group membership is re-evaluated at each login. If a user is removed from a group in AD, their Splunk roles change at their next login, with no change needed in Splunk.

- **"The `can_delete` role lets you delete the index itself."** No — `can_delete` (technically the `delete_by_keyword` capability) only allows the `| delete` search command, which removes specific events matching a search. Deleting an index definition requires `indexes_edit` capability, which is a completely different permission.

- **"Password policy applies to LDAP users."** Password policy configured in `authentication.conf` under `[splunk_auth]` applies only to native Splunk accounts. LDAP/SAML users are governed by their IdP's password policy.

---

## 19. Mastery checklist — what you should be able to explain

- The distinction between authentication and authorization, and which system handles each.
- All four authentication mechanisms, and the precedence/fallthrough order when native + LDAP coexist.
- The five built-in roles (`admin`, `power`, `user`, `can_delete`, `splunk-system-role`), their purpose, and their relative privilege levels.
- What role inheritance means, why inherited capabilities cannot be removed, and how to design a role hierarchy.
- The full set of `authorize.conf` role stanza settings: `importRoles`, `srchIndexesAllowed`, `srchIndexesDefault`, `srchFilter`, `srchJobsQuota`, `srchDiskQuota`, `rtSrchJobsQuota`.
- How multiple-role assignment works (additive/most-permissive) for both capabilities and quotas.
- Where native user passwords are stored and which password-policy settings apply only to native auth.
- The end-to-end LDAP flow: bind request, user locate, credential validation, group resolution, roleMap lookup.
- All major `authentication.conf` stanza attributes for LDAP: `host`, `port`, `SSLEnabled`, `bindDN`, `bindDNpassword`, `userBaseDN`, `groupBaseDN`, `userNameAttribute`, `groupMemberAttribute`.
- The `[roleMap_<strategyName>]` stanza syntax and how to map multiple LDAP groups to one Splunk role.
- How multiple LDAP strategies are ordered and when Splunk moves to the next strategy.
- Why LDAPS (port 636) must be used in production and what SSL configuration is needed.
- How to test an LDAP strategy in Splunk Web and where to look for LDAP errors.

---

## 20. Key terms (flashcard seeds)

- **Authentication** — proving identity; separate from authorization; handled by native, LDAP, SAML, or scripted.
- **Authorization** — what the authenticated identity can do; entirely role-based in Splunk.
- **Native (Splunk) auth** — credentials in `etc/passwd`; used first if a local account exists.
- **Authentication order** — local account exists → try native first; if native fails by wrong password → stop (no LDAP fallthrough); no local account → try LDAP.
- **Role** — a named bundle of capabilities + index access + search restrictions; assigned to users.
- **Capability** — an atomic permission within a role (e.g., `edit_user`, `schedule_search`, `delete_by_keyword`).
- **`admin` role** — highest-privilege built-in role; all capabilities.
- **`power` role** — can share objects, tag events; below admin.
- **`user` role** — baseline role; personal search and saved objects only.
- **`can_delete` role** — grants `delete_by_keyword` for the `\| delete` command; added as a second role.
- **`splunk-system-role`** — service-level inter-component identity; not for humans.
- **Role inheritance (`importRoles`)** — child role gets all capabilities of imported role(s); cannot remove inherited capabilities; transitive.
- **Multiple roles** — user gets most permissive union of all assigned roles; quotas take the maximum.
- **`authorize.conf`** — `[role_<name>]` stanzas in `etc/system/local/`; never edit `default/`.
- **`srchIndexesAllowed`** — semicolon-separated list of indexes a role may search.
- **`srchIndexesDefault`** — indexes searched when user specifies no index.
- **`srchFilter`** — implicit AND appended to all searches; row-level restriction.
- **`srchJobsQuota` / `rtSrchJobsQuota`** — concurrent job caps; maximum across roles wins.
- **`srchDiskQuota`** — disk cap for a user's jobs; maximum across roles wins.
- **LDAP strategy** — one stanza in `authentication.conf` representing one LDAP/AD server; named by admin.
- **`bindDN`** — service account DN used by Splunk to authenticate to and search LDAP.
- **`userBaseDN`** — the OU subtree Splunk searches for user objects.
- **`groupBaseDN`** — the OU subtree Splunk searches for group objects.
- **`[roleMap_<strategyName>]`** — maps Splunk role names to LDAP group names; semicolons separate multiple groups per role.
- **Multiple strategies** — ordered in `authSettings`; Splunk queries in order, stops at first strategy where user is found.
- **LDAPS** — LDAP over SSL on port 636; required in production; `SSLEnabled = 1`.
- **Authentication fallthrough** — if no local account, Splunk tries LDAP; if local account exists with wrong password, Splunk stops (no LDAP fallback).

---

## 21. Questions to drill (quiz seeds)

1. What is the difference between authentication and authorization? In a Splunk + LDAP setup, which component handles each?
2. A user has a native Splunk account with the wrong password. Splunk is also configured for LDAP where that user exists with a valid password. What happens when they try to log in? Why?
3. List the five built-in roles. Which one is not meant for human users, and why does it exist?
4. Why does the `can_delete` permission exist as a separate role rather than being part of the `admin` role granted to all admins?
5. Role A imports role B. Role B has capability X. An admin tries to uncheck capability X on role A. Is this possible? Why or why not?
6. A user is assigned roles `soc_tier1` (srchJobsQuota = 5) and `power` (srchJobsQuota = 20). What is their effective concurrent job limit?
7. Write a complete `authorize.conf` role stanza for a role called `ir_analyst` that: inherits from `user`, can search indexes `security` and `endpoint`, defaults to `security`, sees only events where `sourcetype=windows*`, and may run 8 concurrent jobs with 100 MB disk.
8. What is the `srchIndexesDefault` setting and how does it differ from `srchIndexesAllowed`?
9. Walk through the end-to-end flow of an LDAP login: what does Splunk do step by step from username entry to the user seeing Splunk Web?
10. In `authentication.conf`, what does `bindDN` represent? Why should it not be a domain administrator account?
11. What is the format of `[roleMap_ldap_corp]`? How do you map a single Splunk role to two different LDAP groups?
12. You have two LDAP strategies: `ldap_corp` and `ldap_partner`. A user exists in `ldap_partner` but not `ldap_corp`. How does Splunk find them, and which `roleMap_` stanza governs their Splunk roles?
13. Why is port 389 (plain LDAP) unacceptable in a production environment? What configuration change enables LDAPS?
14. An LDAP user logs in successfully (LDAP authenticated them) but gets a "you don't have permission" error in Splunk Web. What is the most likely cause?
15. Where in `$SPLUNK_HOME` is the native user password file, and why should you not edit it by hand?
