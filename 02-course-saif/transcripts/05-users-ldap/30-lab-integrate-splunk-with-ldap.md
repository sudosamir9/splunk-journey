---
course: saif-admin
theme: 05-users-ldap
lecture: 30
lecture-title: "LAB: Integrate Splunk with LDAP"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/05-users-ldap, transcript, kind/video]
---

# Lecture 30 — LAB: Integrate Splunk with LDAP

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

In the previous section, we discussed user management as well as how to set up local accounts and Splunk.
Local accounts are easy to set up when it comes to few users, but it tends to be difficult to manage,
especially in the corporate world.
Now, to address this challenge, we use a central authentication mechanism to allow the same credentials
to log into Splunk and other corporate resources by relying on these directory services.
So let me explain this for a moment.
As corporations grow the need to organize user data and assets into our hierarchical structure becomes
pretty much critical.
To simplify storage access of those assets.
Now, LDAP enables organizations to store, manage and secure information about the organization as
well as the users and the assets.
The most common elder abuse case is serving as a central location for storing authentication information
such as usernames and passwords.
And he can use these stored authentication information on various applications to validate those uses.
And this is exactly the main reason why we would like to integrate Splunk with LDAP so we can use these
existing ADD configuration or Active Directory configuration to add, manage and update users in groups
and assign those groups to the Splunk pros.
Now, we already discussed previously about Splunk roles.
Now Splunk comes with preconfigured roles like the admin role, the power role, the user role, and
you can rely on those or you can create your own customized role.
So let's jump ahead and show you what it would look like.
So this is pretty much the live directory tree.
Now.
This is your organization.
Basically, it would be subdivided into different organizations based on the function or the GEO.
Now, these could the latter be subdivided into even more groups, or I would call them the or use the
organizational units.
And within the organizational unit you will have different users also assigned to or member of different
groups.
And these users typically will have different what I would call privilege, access to access, different
resources, internal resources within this whole organization.
Now, to maintain this in a hierarchical structure is pretty much straightforward and easy.
So we will rely on these existing users and the groups to map those groups to Splunk roles.
So we will rely on the username and password from these to access Splunk based on the group mapping.
So let me show you that.
So if we go to.
The this slide.
And let me explain that.
So you as a user here sitting and you have a Splunk instance which has been configured to with an LDAP
server in the back and the back end.
So as you enter the username and the password, the Splunk instance will send a bind request.
To the server and then it's going to authenticate with that LDAP server using the bind end user.
Then the LDAP server will locate that user and it will return it to the Splunk instance.
And then the Splunk instance is going to send back that user that you've just entered along with the
user to the LDAP server.
Now the server will locate and based on the privilege and the group mapping of that user.
It's going to grant you.
Either a success if the authentication is successful, Basically the password as well as the group is
mapped to a role within Splunk.
Then it's going to allow you to access the Splunk web.
Otherwise, it's going to fail.
And this is exactly what we will be doing.
Now, the steps to integrate Splunk instance with LDAP comprise of create an LDAP strategy and then
map the user group to that specific Splunk row.
But before we dive into the demo, let's go through the LDAP configuration prerequisites and discuss
those briefly.
Now you will be needing to have the host where LDAP is running like Active Directory.
Then the port.
Now typically in in production environments you will be using 636 the sstl, which is recommended.
In my case, I'm going to be using the insecure port, which is 389.
So no SSL now connection order.
In this case, if you have multiple LDAP configurations within Splunk, so you want to order this one
as one, two, three depending on the prior on the priority.
Now what is very much important is a service account that has permission to make a bind request, as
previously mentioned, to that LDAP server.
And it's recommended that you should not use a default ad administrator account.
But we will need to create a dedicated account for Splunk with no admin privilege.
So we can bind that request to the server.
To the server.
Of course the password.
And then we will need to know where to search for these users.
Of course, we will need to provide the user base distinguished name so Splunk could search those users
and of course the groups associated with these users.
So let me show you that.
And let's jump ahead to Splunk.
So again, let's go to Settings.
Authentication.
Mechanism, and then we will create our first LDAP settings, by the way.
I'm doing that via the web.
You can also do it through the file.
So I'll be showing that you that as well.
So let's create a new LDAP.
Let's give it a name.
So LDAP one.
Now, in my case, I have.
The hostname.
So let me just copy.
Copy it for a moment.
So this is pretty much the LDAP server that I have.
I'm going to be using Port 389.
Now the Biden distinguished name for that user.
So let's jump ahead to my LDAP server.
And show you that.
So.
I'm going to be creating a user.
I can I could rely on this one, but I will be creating a user in here.
So let's go and do new.
User.
So I'm going to name it as.
Splunk.
Service.
Count.
So I will be just sending that.
So Splunk service.
Next, I'm going to provide a password.
And then I'm not going to change that.
Cannot change it.
Password never expires.
Next.
This is the user finish.
So that's the binding of the bind.
Distinguished name.
Let's make it as part of a group.
I'm going to do like the security group.
So let's check that.
Let me check security.
Security group.
I couldn't find it.
So maybe we can put admin.
Let's check that.
We can put it as part of the administrators or.
Batman group.
Let's keep it as part of the administrators.
Let's hit OC.
Done.
So now I could rely on here for the user that I've just created.
So here you go.
I think I found it.
So let's go back.
There you go.
So if we open this one.
And we go into properties.
Then this is the distinguished.
Name.
So let me just copy the whole thing.
Copy.
And then we go back and we put it here.
And then I will put the password.
Then I'm going to be using the user base distinguished name.
Now, this is the location of your LDAP user specified by the distinguished name of your user subtree.
So let's go back to the LDAP.
I would like to take pretty much the organizational units, this one.
So this I want to integrate whatever the users are in here.
So let me just do properties and then locate this one.
So.
Let me just copy that.
And go back and hear.
So I'm going to paste it.
Or its good user attribute.
I'm just going to copy the default, which is this one.
Copy.
Paste real attribute.
This is just and so the common name I'm going to be relying on this attribute, email attribute, I'm
just going to put mail.
Group mapping attribute.
You can leave that now.
The group base distinguished name.
Let's go back to the LDAP and put that.
So.
The group is this one.
So what we need to do is go to properties and.
And copy this one.
So let's copy that.
Now let's go back to Splunk.
Based it.
There you go.
Now group name attribute as well.
C and static member that should be member.
So as the default value paste it.
Now.
I'm just going to save it.
So we have saved that.
So now.
Since the first step is done and we have created the LDAP strategy name.
So let's go to mapping the groups.
So we click on this group.
And then you can see here, these are the LDAP uses that we have pretty much imported.
So now I'm going to assign this group, maybe the admin group.
So the Admiralty.
So let's save that for a moment.
So now we are done.
And you can see that this group name has been assigned the admin role.
So now what I'm going to do, I'm going to open an incognito window.
And I'm going to use my credentials.
For that user.
Let's try to log in.
It's taking some time.
And there you go.
So I have been assigned the admin role for the semi user account and I'm able to log in.
So let's close this for a moment.
And let me show you actually the configuration via the CLI.
So let's go to the clay.
So I'll send two patient doctor calls.
He's a man.
So as you can see here, let me just bring back to the top.
Now, these are the configurations that we've just entered into the Web via the web for the LDAP configuration.
It's pretty much the same.
And as you can see here, the roadmap map for this LDAP.
For this group which has been imported.
It has been assigned the admin role, and this is exactly what we have done in here.
So.
What you can do.
You can do it either via the CLI and here you can copy paste.
And you can see here are the different attributes that we have provided.
So the group base name, the hosts, the LDAP hosts, the port and the user base where Splunk is going
to go ahead and search.
For that specific group that to search those users under that organizational unit and of course, under
that organizational unit, all the users which are a member of this group, which is part of that organizational
unit.
And this concludes basically the integration with LDAP.
