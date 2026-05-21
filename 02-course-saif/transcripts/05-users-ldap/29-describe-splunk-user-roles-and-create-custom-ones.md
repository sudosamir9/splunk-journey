---
course: saif-admin
theme: 05-users-ldap
lecture: 29
lecture-title: "Describe Splunk User roles and create Custom ones"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/05-users-ldap, transcript, kind/video]
---

# Lecture 29 — Describe Splunk User roles and create Custom ones

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

In this section, we will be talking briefly about Splunk User Management.
So to add a user in Splunk using the Native or the local authentication offered by Splunk, simply go
to settings under users and authentication and click on users.
Now and here what you can do.
Just click on new user and you can do Splunk three as the user.
This is optional, email address is optional, and I'm going to provide a password for it.
Then I'm going to assign the user role.
This is one of the five predefined roles that Splunk comes with.
I'm going to uncheck the required password change at first login and I'm going to save that.
Now, this is the user that I've just created.
By the way, passwords for these users are stored in Splunk home at C password.
Let me show you that.
So if we go to the search, head under here.
And let me zoom in.
And de vie.
And as you can see, we have slunk, slunk one, slunk to three.
And, Victor, they use for these users.
So let's go back and discuss briefly all the roles that Splunk offers.
Now, as I've mentioned before, we have five roles.
We have the administrator role.
And we have the power role, which is privilege with respect to admin and more with respect to user.
And we have the user role, which is the least privileged role.
Now let's just discuss about Splunk system role.
Now, this one is a very much special role that would allow system level services to run without a defined
user context.
So imagine when you want to add a search peer a.k.a an indexer as part of the search head.
So we will be showing that in the subsequent slides.
So what does that mean?
That mean you will create a role or a user with this role under the indexers as well as will under the
search head.
And then you will be adding the search peer the indexer to the search head using this role.
Of course, you can always rely as well on the admin role, but as a best practice, use the Splunk
system role.
Now the role can delete.
So.
So when you want to search for specific data on an index and you want to delete that data, the way
you do it is that you can use the pipe to delete.
This is a special role that it's defined by itself in this dedicated role.
So to do that, let me show you exactly what I mean.
So let's open.
Search.
Let's expand and let's go to search and reporting.
Let me try to find.
The data in security.
Index date range may be.
Like.
Up to 1st of February.
Do we have any data?
Yes, we have some data.
What I'm going to do now, I'm going to pipe that to delete.
Error.
You have insufficient privileges to delete these events.
Why?
Because we have removed the can delete role.
So what we will do, we will edit that again.
And we will add the can delete, acknowledge, save, and then we will try that one more time.
And as you can see, we've just deleted these data.
By adding also the can delete role to the Splunk user.
Now let's move ahead and talk about how we can add a custom role.
So to add a custom role, just add a new role you as an administrator.
You can actually add a new role.
So I'm going to name this custom underscore role with spunk.
What you can do, you can actually inherit predefined.
So if I do admin, basically inheriting all the capabilities of the admin role, let's examine that
together.
And as you can see.
Next to the capability name.
It's inherited, by the way.
You cannot uncheck it because you have it inherited from the admin role.
But what you can do, you can add more roles to this custom role in addition to the inherited role from
the admin.
So let's uncheck that and go for the power.
And of course you can see you have less privilege with the power role and you're inheriting from there.
Now, bear in mind we are about to create, which is a custom role, is going to inherit everything
from the power role as well as whatever is being inherited at the index level.
But it's not going to show under the user interface.
And again, you cannot disable inherited capabilities or access when you inherit something from a different
or other role.
In this case, the power.
So you can see I cannot uncheck that.
So let's go to indexes.
Now, by default.
You can see that you cannot uncheck the indexes which are inherited by default from the power roll,
but you can add others and also when you check the defaults.
So for instance, let's check the box for history in here.
That means that the default checkbox will define the index that you as a user.
You don't specify when you go ahead and search for something.
So let's go ahead and actually create this role.
So I'm going to create that role.
I have just created that role, custom role, and this is pretty much showing the inherited capabilities.
So what I'm going to do, I'm going to go to the CLI and show you that.
So let's go.
Control X?
No.
Clear.
So let's move to CD.
Opt Splunk at C system local.
Local.
And let me show you.
So let's do sudo vi authorize.
And as you can see, this is the custom role that we've just created and it's inheriting.
The power user, the power roll.
This is exactly what I meant.
And this is under Splunk Etsy system local and the authorized dot com.
Now let's switch gears and talk about the different authentication mechanisms that Splunk offer.
So let's go to authentication methods.
Now, you can rely on authentication based on Splunk, local authentication, or what you can do.
You can add an LDAP configuration.
So you can integrate your LDAP Active Directory of your corporate organization to allow all of these
users within your corporate organization to log in to Splunk.
And then based on the group mapping, you can assign different roles and capabilities.
By the way, I will be demoing that briefly.
