---
type: pre-class
theme: 05-users-ldap
topic: users-roles-and-ldap
covers: "Lectures 29–30"
read_time: "~4–5 min"
tags: [study-guide/pre-class, theme/05-users-ldap]
---

# Pre-class — Users, Roles & LDAP

> Read before the video (covers lectures 29–30). ~4–5 min. The video moves fast and assumes you already accept that "authentication" and "authorization" are different things — walk in with that separation already loaded.

## Why this matters
Every Splunk deployment has users, and every user needs precisely scoped access — not too much, not too little. The roles and capabilities model is how Splunk enforces that. LDAP integration is how every real enterprise deployment actually manages users — otherwise you're maintaining a separate set of credentials for every Splunk user. These two topics together (the role model + LDAP) are the foundation of Splunk access control.

## The mental model (hold these)
1. **Authentication ≠ authorization — they are separate layers.** Authentication proves *who you are* (native Splunk password, LDAP, SAML). Authorization determines *what you can do* (roles and capabilities). In a typical enterprise setup, LDAP handles authentication and Splunk's role model handles authorization. The bridge is group-to-role mapping.
2. **Authorization in Splunk is entirely role-based.** There are no per-user permissions — every permission comes from a role assigned to the user. A role bundles three things: **capabilities** (atomic permissions like `edit_user`, `schedule_search`), **index access** (`srchIndexesAllowed`, `srchIndexesDefault`), and **search restrictions** (quotas and `srchFilter`).
3. **Multiple roles are additive — most permissive wins.** If a user holds two roles, they get the union of all capabilities and index access. Quotas take the maximum, not the sum.
4. **Role inheritance is one-way and locked.** A child role that imports a parent inherits all of the parent's capabilities. Those inherited capabilities cannot be removed from the child. Design hierarchies with this in mind.
5. **Authentication order matters when native + LDAP coexist.** If a native Splunk account exists for a username, Splunk tries that first. If native auth fails because the password is wrong, Splunk *stops* — it does not fall through to LDAP. LDAP is only tried when no local account exists for that username. This means a local account always takes priority.
6. **LDAP integration: authenticate externally, authorize via roleMap.** LDAP proves the user is who they claim. Splunk then looks up the user's LDAP group memberships and consults `[roleMap_<strategyName>]` in `authentication.conf` to assign Splunk roles. If a user's group isn't in the roleMap, they log in with no roles and see a permissions error.

## Key terms (quick definitions)
- **Authentication** — proving identity; handled by native, LDAP, SAML, or scripted auth.
- **Authorization** — what an authenticated user can do; entirely via roles in Splunk.
- **Role** — bundle of capabilities + index access + search restrictions; assigned to users.
- **Capability** — atomic permission (e.g., `edit_user`, `delete_by_keyword`, `schedule_search`).
- **`admin` / `power` / `user`** — the three main built-in roles in descending privilege order.
- **`can_delete`** — a standalone role that grants the `| delete` search command; added as a second role when needed.
- **`splunk-system-role`** — for inter-component service accounts (not human users).
- **`importRoles`** — role stanza setting that inherits capabilities + index access from another role.
- **`srchIndexesAllowed`** — indexes this role may search (semicolon-separated).
- **`srchIndexesDefault`** — indexes searched when user specifies no index.
- **`srchFilter`** — row-level filter implicit-ANDed to every search for this role.
- **`authorize.conf`** — `[role_<name>]` stanzas at `etc/system/local/`; defines all roles.
- **LDAP strategy** — one named LDAP server configuration in `authentication.conf`.
- **`bindDN`** — service account used by Splunk to bind to and search LDAP; should be low-privilege.
- **`userBaseDN` / `groupBaseDN`** — the OU subtrees Splunk searches for users and groups.
- **`[roleMap_<strategyName>]`** — maps Splunk role names to LDAP group names.

## Watch for this in the video
- The video demonstrates how adding the `can_delete` role to a user enables the `| delete` command — notice that the capability is separated into its own role intentionally, not an oversight.
- Watch how the `custom_role` inherits capabilities from `power` — and how those inherited capabilities are greyed out and cannot be unchecked. This is the lock-in of inheritance.
- The LDAP lab shows the full flow in one take: create the LDAP strategy in Splunk Web, configure bind account and base DNs, map LDAP groups to Splunk roles, then test with an incognito window. Follow *which fields map to what* in the directory tree.
- The video shows the resulting `authentication.conf` in the CLI after doing it via the Web. The file content is the ground truth — the Web just fills in the same attributes.

## Questions to hold in mind while watching
1. When both native auth and LDAP are configured, under what exact conditions does Splunk try LDAP — and when does it stop at native?
2. If a user is assigned two roles and role A has `srchJobsQuota = 5` and role B has `srchJobsQuota = 20`, what is the effective limit? Why?
3. What does the `bindDN` account actually do — and why should it *not* be a domain admin?
4. If a user logs in via LDAP successfully but gets a permissions error in Splunk Web, what has been misconfigured?

## How this connects forward
- **Distributed architecture:** in a search head cluster or distributed environment, role definitions and `authentication.conf` need to be consistent across all search heads — typically managed via the Deployer (for SHC) or Deployment Server.
- **ES and premium apps:** Splunk Enterprise Security adds its own roles (`ess_analyst`, `ess_admin`, etc.) built on top of the same role model — understanding the base model is prerequisite.
- **`authorize.conf` + `props.conf`/`transforms.conf`:** `srchFilter` in a role is a powerful tool, but for data onboarding segmentation, index-level access controls in roles remain the primary mechanism.
- **Monitoring Console:** access control to MC itself is governed by the same role model — the `can_use_mc` capability controls who can see it.

---

## Official references (for verification / deeper reading)

| Topic | Splunk Docs page |
|---|---|
| About configuring role-based user access | https://docs.splunk.com/Documentation/Splunk/latest/Security/Aboutusersandroles |
| Define roles with capabilities | https://docs.splunk.com/Documentation/Splunk/latest/Security/Rolesandcapabilities |
| Create and manage roles (authorize.conf) | https://docs.splunk.com/Documentation/Splunk/latest/Security/Addandeditroleswithauthorizeconf |
| authorize.conf reference | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Authorizeconf |
| Set up LDAP authentication | https://docs.splunk.com/Documentation/Splunk/latest/Security/SetupuserauthenticationwithLDAP |
| Configure LDAP with Splunk Web | https://docs.splunk.com/Documentation/Splunk/9.4.2/Security/ConfigureLDAPwithSplunkWeb |
| Configure LDAP with configuration files | https://docs.splunk.com/Documentation/Splunk/9.4.1/Security/ConfigureLDAPwithconfigurationfiles |
| Map LDAP groups to Splunk roles | https://docs.splunk.com/Documentation/Splunk/latest/Security/MapLDAPgroupstoSplunkroles |
| authentication.conf reference | https://docs.splunk.com/Documentation/Splunk/latest/Admin/Authenticationconf |
| Configure password policies | https://docs.splunk.com/Documentation/Splunk/9.4.0/Security/Configurepasswordsinspecfile |
