---
course: saif-admin
theme: 07-data-flow-concepts
lecture: 39
lecture-title: "Why Sourcetype Matters?"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/07-data-flow-concepts, transcript, kind/video]
---

# Lecture 39 — Why Sourcetype Matters?

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So why source type matters?
So it's very crucial that before data onboarding and before you go ahead and discuss with the customer
what kind of data is set to be onboarded, it's very crucial to define a source type for the data to
be ingested.
Now, source type controls how Splunk formats the data by applying appropriate sets of controls to correctly
parse the data into events and allocate type step.
Splunk comes with a big set of sauce types defined for many different data types.
And you can find that actually under Splunk base.
Also, you can rely on the different apps add ons as they are also shipped with preconfigured source
types serving that data type within the app or add on.
So if no source type is found for your specific data, then you can always create a new one.
So.
Many searches, reports, dashboards actually rely on the source type.
So Splunk, again, will try to determine the source type for you.
If Splunk recognizes the data, then, of course, it's going to assign to one of the pre-trained source
types.
So let's take a look at that.
So let's go ahead and to.
Or Splunk.
And then let me show you how we can do that.
So, for instance, you have a sample data that you've been discussing with the customer and you want
to onboard that data.
So let's go ahead and show you that.
So as part of the onboarding, you need to test the data first.
So what you can do, you can do add data.
And then from here to this Splunk instance.
So I'm just going to select the file.
I'm just going to go for access.
Of course, the maximum file upload size is 500 mb B, so let's go for next.
Again here, as you can see.
We're actually able to rely because Splunk has already kind of recognized that data and it has set the
source type access combined web cookie.
So it's actually has basically recognized the data and is going to assign it the proper source type.
So Splunk is doing that for you out of particular.
And if we click on here, you can see the different categories.
So under application, you have the different source types, which comes like shipped within Splunk,
email log to metrics.
You know, it's an operating system, for instance, syslog message format web, which is this one.
Of course, these are the principles.
And these are the different source types that you have in here.
Of course, we will touch base on these event breaks because these are pretty much instructing on how
would you like to segment the data.
So for instance, you want to basically ingest the data.
And as you want to ingest and parse this data, you want to define actually how to break this data into
events.
Especially, this is very important when it comes to multi line kind of data.
So in this case, you will need to know where it's going to start and when it's going to end.
So basically you need to define the event boundaries, the beginning and the end, and then you can
break it.
So the data should be parsed correctly.
Now, these are the different source type that comes within Splunk.
What I can show you as well.
So if we go to settings source types.
And here you can find the different source types, which are part of the Splunk instance, anything
which is showing a system, these are the default.
But take a look at here config underscore file.
This is part of the Splunk to Linux.
So if you deploy or install an app which you can always find under Splunk based from here.
It was to deploy it to the Splunk instance.
Then automatically you will see all the different source types which are part of that app, and you
can begin to land in here and you can see them.
Now let's take an example and show you this.
So, for instance, I want to.
Install the Windows app.
So let's go ahead.
I think it's this one.
Yeah.
Let's click on it.
So I'm just going to download it first.
So let's go ahead and wait for it to.
Well, my Internet connection seems like it's slow.
Let me just download it.
Except agree and download.
So let's go back to here.
I don't see any Windows source types, of course, so I can rely on those apps which are found under
Splunk Base.
So it can make my life easier when I want to on board kind of Windows logs so I can actually rely on
the Splunk add on for Windows.
So let's first install a Windows app or the add on.
So I'm going to go under here.
And then I'm going to stole app from this file.
So let me just.
Do not upload.
So this has been done.
So let's go now to Settings again, of course, to make sure that that Windows is already Windows app
is already deployed.
Let's search for it.
So let me just do control F.
Windows.
And there you go.
We have that Windows Splunk add on that has been installed and of course, it's enabled.
So let's go again under settings and let's see what kind of source types have been imported into the
Splunk.
So I'm going to choose from here.
Where is it?
Windows, maybe.
Does.
And here you go.
You can see these are we have identified 139 source types which fall under the Splunk to four windows.
These are already source types which have already been configured.
So you can rely on these.
That's going to help you to onboard windows like logs into your Splunk instance.
So if we go back and to settings.
At data.
Upload data.
Select file.
I'm going to go for the access.
Let's go for next, of course, and hear if I'm going to search for Windows.
I will find now all of these new Windows source types, which are part of the Windows app add on.
So these can really help me a lot to kind of facilitate the onboarding of the Windows logs.
Of course, you can always rely on Windows, add on Splunk where it's going to show you.
It's a really good documentation that is going to walk you through the vendor products which are supported.
Buy Splunk for these different Windows platforms, operating systems, and of course, what kind of
source types that are coming within this Splunk.
Add on for Microsoft Windows and you can see these are all the different source types that we can find.
For instance, I want to search for Active Directory.
Let me just copy that.
We go back to our source type and here, let's search that one.
And you can see there you go.
This is the Active Directory source type, which is going to help me facilitate parsing the Active Directory
logs.
So if we go back to here, let's search for performance process.
Let me just copy that and go back in here.
And paste it.
And there you go, perform process.
So this is a good way that it's going to help you a lot to facilitate the onboarding process.
Now, bear in mind, sometimes there are certain data which you want to on board and there is no source
type defined under Splunk, nor you cannot find it under Splunk base.
So what you need to do, you can actually create that yourself.
But to do that, then you will need to take care of the event breaks.
You need to set the proper boundaries of the event.
So you need to know where to break the event to go to the next one and so on and so forth.
And of course you need to assign the timestamp, etc. and then you can save it as a new custom source
type for you.
And then you can define is it at the app system level, like globally, or you can actually create a
new app context and you can save all the settings under that app context for yourself.
For example, I have already created an admin course app context, so whatever changes I want to do
to this source type to actually pass these logs, then I could assign a new source type.
For instance, I'm going to call it admin.
Of course.
Source type.
I'm just going to save it under the admin course app context.
And then I'm going to save it in here.
So if we go back now under source source types, which is under settings and then source types in here.
That I can select actually my admin course.
And as you can see, this is exactly the admin course source type that I've just created.
So in here you can set the event breaking policy.
So this is a powder basically to break into a new line.
So we will we will cover this into as we progress throughout the course.
