---
course: saif-admin
theme: 03-apps-configs-layering
lecture: 17
lecture-title: "Introduction to Splunk Apps / Add-ons and deploying your first App via the web"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/03-apps-configs-layering, transcript, kind/video]
---

# Lecture 17 — Introduction to Splunk Apps / Add-ons and deploying your first App via the web

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So in this section we will be talking about Splunk apps and ad ops.
So and we will be talking about the difference between apps and add on.
But from the high level, let's first examine what are apps and adults.
It's nothing but a plug in that's going to extend Splunk functionality.
Now, think of it like, you know, there are different vendors out there, like different firewall
vendors.
I would say, for example, Checkpoint, FortiGate, Palos, Cisco Devices, to name a few.
Normally, customers would want to parse and find a way to help customers to actually parse those logs
and coming logs and make their life a lot easier.
The way you do it.
So there is a website which is called Splunk Base, where Splunk is maintaining some of these apps.
But also there are a possibility for you guys out there to actually create and package some apps and
upload them to Splunk Base so that others could use.
So it enhances the the parsing process and it's going to help a lot into create source types and improve
pretty much the the output.
Now let's first examine an add on.
So what is an add on?
It's typically a single component.
I'm going to be demoing that in a moment.
It doesn't have a navigation UI per se, like an app, and it's typically created for a single use case.
And by the way, it can extend apps functionality.
Think of it like a custom rest endpoint or custom field extraction.
It could contain like props, transforms and source type definitions or macros.
So it pretty much help into during the field extraction process.
While an app will contain a navigable user interface or possibly a setup screen.
And to contain many knowledge objects like lookups, stacks, event types, and even safe searches,
which is going to be viewed in kind of like a dashboard.
So let's go ahead and show you that in a moment.
So these are just logged in to the Splunk, the portal.
And I'm just going to go to apps.
Now you can see these are all the apps which are offered out of the box in here that you can see.
Now, these are the versions of these apps which are maintained and these are the update checking.
Also, you can see there's an option where this app is visible or not.
Now also, these are the app permission level.
So.
To which extent users are able to view or edit those apps so you can see based on the roles.
Now, if you see it's read, that means every user basically part of these roles which are offered out
of the box from Splunk, are able to read and view while editing.
It's only assigned to the power user.
So let's cancel that for a moment and move on.
Now, this is the status where it shows you is it enabled or disabled as an app.
Now let's go ahead to Splunk.
Base and actually install an add on.
So let's go for Cisco.
Let's find that one.
So Cisco Network known this one.
This is an app and this is an add on.
So again, as I've shown you, what is the difference between the both?
I'm just going to first install and deploy the add on.
So let me just click on it.
Oh, I need to log in.
So.
So I've just logged in to the Splunk base Splunk dot com.
By the way, if you don't have an account, you will need to go ahead and create an account.
So let's download.
That add on.
Let's hit.
Och!
There you go.
Now let's go to Splunk apps and under the install app from a file.
So there are different ways where you can actually install an add on or an app into Splunk.
This is I'm going to show you first through the web gooey.
So by going into install.
So let me just zoom in.
Then show you that so install app.
And then I'm just going to drag and drop.
Upload.
And it should be fine.
So I think it's already there.
So let me just search it.
Cisco, There you go.
So it's pretty much global.
It's shared globally, not at the app level context.
It's already enabled.
So let's go and see that.
Of course, it's not going to show in here because this is an add on.
Now, let's go ahead and actually also download the.
Splunk Cisco app.
So let's search for Cisco again.
So we have already downloaded and deployed the Splunk add on for Splunk Enterprise, which is the Cisco
one.
I'm going to deploy this one now.
So let's download it.
Confirm, by the way, just to explain to you guys, this app is not supported by the developer or Splunk.
So remember when I talked about Splunk Base?
So Splunk Base is kind of like a portal where it's a kind of a directory, if you will, and it contains
all the different apps and add ons which are supported by Splunk.
Now there are two categories.
There are apps and add ons which are actually maintained by Splunk.
So it went through a sanitation kind of check.
And there's also the possibility for you guys out there to develop your own Splunk app add on and you
can upload it to Splunk as well.
So let's confirm.
And agree to download.
There you go.
By the way, before we even go with that one, let me show you the Linux one.
So when we go to the Linux one.
You see Splunk support add on.
So this is the tag, you know, which shows that this is a Splunk supported kind of app.
When you don't see that one, you would see something like it's not supported.
So this is a distinction between the apps, which has gone through a citation check from Splunk themselves
versus the ones which are the ones that have been created by normal people outside of Splunk organization.
So let's go ahead and an upload the Cisco app.
So install app from a file.
And drag and drop.
Upload.
And let's search it real quick.
So this is the add on and this is actually the Cisco app.
It's already globally shared globally among the users and it's enabled.
So now if we just hit their.
You can see it's there.
This is Cisco Networks.
And this is the difference between an add on and an app.
So this is the app.
And you can see already there are this app contains dashboards, saved searches.
Now that we have installed an add on and an app for Cisco on Splunk from Splunk based via the web,
I would like to show you exactly how that would be seen in via the CLI.
So let's jump ahead and go there.
So CD upped Splunk.
Now this is the path where everything, all the configuration, the packages, etc. for Splunk Enterprise
now you see under Etsy.
So let's go under Etsy.
Now you can see the directory structure in here.
The ones which are of interest are system user.
And apps.
So under this directory are all the apps.
Which you would normally see.
Here or actually here.
Let me show you the ones which are visible and the ones which are not visible.
So all of these apps.
Under APS.
Are seen under the apps directory here.
So let's go ahead.
To apps.
And you can see.
The to Cisco for ICE.
And the Cisco iOS app.
So this is an app.
This is an add on.
Now, remember, we have just uploaded those via the web.
And this is how we see it under the CLI.
So what I'm going to do, I'm going to remove.
Both.
Remove minus R.
And then I'm going to remove the second one.
This is the way on how to delete.
An add on or an app.
So that we have deleted those.
Of course, if we do a refresh in here.
Let me show you.
And search.
It's still there.
Why would be that?
Because this is still in runtime.
So although we have deleted the apps in here, it's still in runtime.
So what we do to take that effect.
So what I'm going to do, I'm going to do debug refresh.
So this will update.
I would call the Splunk debugger refresh.
It's kind of like reloading Splunk configurations again.
So whatever you have.
Under here any changes that you have done?
Still, this is in memory, not at runtime.
When you do a debugger refresh, it's pretty much reloading all the configurations in here.
But since we've deleted those two, basically the Cisco app and the Cisco add on, we're not going to
be first able to see those being removed from here unless we do a reload of the configurations.
So now that we have done the reload under by using debug refresh, let me refresh it now again and let's
see if they have been gone or not.
So let's search for those.
In fact, we cannot find them anymore.
So they are gone.
