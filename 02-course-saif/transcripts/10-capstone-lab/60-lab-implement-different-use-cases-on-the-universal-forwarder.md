---
course: saif-admin
theme: 10-capstone-lab
lecture: 60
lecture-title: "LAB: Implement different use cases on the Universal Forwarders"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/10-capstone-lab, transcript, kind/video]
---

# Lecture 60 — LAB: Implement different use cases on the Universal Forwarders

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So now that we have successfully deployed our Splunk components in a distributed environment and we
have verified that by going to the search head and run this spill query, and we can see that we're
actually receiving the logs from all the different Splunk components, which are the intermediate folders,
the universal forwarders and all the other ancillary Splunk components.
So now we go back to our diagram.
And before we go through discussing our different Splunk, use cases in terms of data collection methods,
what we need to do, we need to understand what kind of data we would like to ingest on the index or
one an index or two so we can go and create the respective indexes.
So for instance, in here on my Windows machine, I would like to monitor the logs generated on my Windows
machine and using the universal folder which is deployed on my local machine to forward the logs to
intermediate forwarder one and two.
So to do that, what we need to do, we need to deploy the windows.
Add on that we will need to download from Splunk Base.
So this is the first case that we need to do.
Now, to do that, obviously we need to go to Splunk Base and download that app, but before we do that,
we need also to go ahead and create the index windows on my indexer one, because obviously we can afford
whatever we're going to be monitoring in here to our index or one.
Now let's go ahead and first do that.
So what I'm going to do, I'm going to go to my index or one.
So let's go.
8000.
Let's log in.
Now let's go to Settings.
Indexes.
I will go ahead and create a new index.
And I'm going to call it Windows.
Of course.
You can go ahead and set the size of this entire index.
It's really up to you.
I'm going to leave it as it is and then I'm going to save it.
So now the Windows index is enabled and you can see in here.
So then I'm going to go ahead and search for the windows to.
And this is the one.
Let's click on this one.
Let's download it.
I've accept sharing.
It's fine.
Okay.
So this is the app.
So I'm just going to copy this app.
I'm going to paste it in here for later use.
So let's leave it as it is.
So now let's go back again to our diagram in here and let's discuss the other use cases.
So remember, we will need to deploy the windows, add on on this universal folder, which is deployed
on my Windows machine using the deployment server.
Now, let's move ahead to the second use case.
So here I have a universal folder deployed on my Linux machine.
And I would like for this specific use case to use the Linux to.
And we will activate some stanzas on this to to monitor certain files and directories on my Linux machine
and forward the logs to intimidate folder one and two.
So obviously what we need for that also we need to create an index Linux on my index or one so we can
ingest and write that data into disk inside index or one.
So first we will need to create the Linux index in here and as a second step, which is part of the
onboarding, we need to go ahead as well and download the Linux add on.
So let's go ahead and find that which is this one.
So let's download this one as well.
So I have downloaded it.
Let's copy it to my directory of apps, which I'm going to be using it later.
Once I will move those apps to my deployment server because I'm going to use the deployment server to
actually deploy those apps and add ons to the deployment clients, which are the universal folders in
this case.
So let's go back to our lab diagram.
And now I'm going to use a custom app.
If you remember from the previous sections where I'm going to leverage some scripted inputs inside the
Splunk, add on for Unix Linux to collect some OS level commands and then forward those logs to index
or one as well.
Now for this specific case, also I will need to create an index and I'm going to call it Linux underscore
system and I'm going to create it under index or one.
So moving ahead, let's take the fourth use case in here, which is I have a FortiGate firewall.
And I would like to configure this FortiGate firewall to forward the SIS logs messages via port, maybe
514 by default.
Or I could also customize it and use maybe five, five, five, five.
And I'm going to use the heavy forwarder as the collection for these logs, and then I'm going to instruct
this heavy forwarder to receive those logs and then forward those logs to index or two.
So for this specific use case, what I would need to do as well, I will need first to create an index
in here and I'm going to call it Fortinet.
At the same time, we already have an add on basically to handle and parse the FortiGate firewall logs.
So let's go ahead and do that as well.
So on Splunk Base, what I'm going to do, I'm going to type FortiGate.
Let's examine that.
And I actually have a Fortinet FortiGate add on for Splunk, and I'm just going to download this one
as well, because this is offered by Splunk.
And we can use it basically.
So we can it can help us to parse the logs which are generated from the FortiGate firewall.
So I'm going to copy this one as well, and I'm going to paste it in my APS directory.
So let's go ahead and paste it as well in here.
Now, we have identified that we would need the Windows to the Unix Linux to and the FortiGate for our
use cases.
So let's go back to the diagram in here.
Also, if you remember from the previous discussions, we've already configured the hack.
So what I'm going to do, I'm also going to create an index for all the incoming traffic for the hack,
and I'm going to create it under Indexer too.
So if we go back to our notes, I'm also going to create an index, which is the heck index, and I'm
going to place it on index or two.
So let's go ahead and start with those.
So first I'm going to create the Linux index.
So let's go to my index or one.
I'm going to go ahead and create the Linux index.
I'm going to leave everything as default.
I'm going to save it.
Now I have the Linux index, which is also enabled.
And then.
I'm going to create also the Linux system index for my scripted inputs.
So let's go ahead and create that.
So I'm going to paste it in here.
I'm going to save it.
So now I have those three indexes enabled on my indexer one.
Now, as per our requirement, what I'm going to do based on my notes, I also need to create the index
Fortinet and the index heck on my index or two.
So let's go ahead and log in to our index or two.
So let me copy the public IP.
8000.
Let's log in.
Now I'm going to go to Settings.
Indexes.
And I'm going to create my index 40 net for fourth use case.
Save it.
I'm going to create another index, which is the heck index.
And I'm going to save it.
So now.
You can see that I have the heck index enabled as well as I have the Fortinet index enabled.
So let's go back to our diagram.
So now that we have identified what kind of indexes we want based on our use cases, what I'm going
to do, I'm going to go ahead and first deploy the windows, add on on my windows machine.
Now, to do that, what I need to do, I need first to copy.
Those add ons, and I'm going to use WinZip to copy those to my deployment server.
So let's go ahead and connect to my deployment server via ACP.
So here I'm just going to save it and I'm going to log in.
Yes.
Now I am located under OPT Splunk Etsy deployment apps.
So I'm just going to copy.
Those three add ons to here.
And now I'm going to go ahead via SSH.
And connect to my deployment server.
So let's see to opt Splunk.
See deployment apps.
And now I have here my Fortinet, my slack add on for Microsoft Windows as well as the Splunk add on
for Unix and Linux.
So what I'm going to do, I'm going to enter those three.
So sudo tor minus exit VRF.
Fortinet.
So this is the first one.
And you can see it's here and I'm going to do the second one sudo r minus x set v f and then.
Splunk for Microsoft.
Then let's do for the third one.
So sudo tar.
Minus exit VF.
Splunk for.
Unix.
And it.
So now we have all three on target.
So what I need to do, I just need to delete those three.
So sudo remove.
This is the first one.
Let's do the second one.
Sudo remove dash splunk.
Add on for microsoft.
And I'm going to do the third one.
So basically now we have those three.
What I'm going to do, I'm going to change the ownership, of course, of those.
So.
Pseudo.
Chong minus are Splunk.
Splunk.
Then I'm going to do.
T Splunk.
At sea.
Deployment apps.
So now we have changed the ownership of all those three tags.
Now that we are done in here, let's go to our deployment server via the web.
So it should be actually not this one, this one.
So let's go to our apps.
Let's do a refresh.
And now we have those tos reflected correctly in here.
So the first use case that I'm going to be doing is I'm going to deploy the windows to on my local windows
machine where my universal folder is installed.
Let's go ahead and do that.
So let's go to the folder management.
Let's create a new server class.
So a new server class and I'm going to call it Windows to.
Save it.
Let's go to my ad apps.
In this case, I'm going to use this one to for Windows.
Save it.
And I'm going to use my client where I want to deploy this app to.
And I'm going to be choosing my desktop for LX 6681 and N and this is my local machine.
So let's do a preview.
So there is a check mark in here.
So let's save that.
And let's do an edit to also trigger a restart of the slug demon.
So now let's wait.
Let's see.
Now I see that the Splunk to Windows is already deployed 100% to my desktop.
So what we can do, we can verify this by going.
To our search.
And believe me, we're not going to find anything.
And I will tell you why.
So let's do index windows.
Why?
Because if you remember from the previous slides or lessons, you also need to go ahead into the windows
to and you need to to do some changes to the configuration because you need to specify as well the Windows
index in there.
And to do that, let's go back to our deployment apps.
Let's do CD to Splunk.
To four windows.
Let's do that.
LS latch.
And let's go to the local CD.
Local?
Let's see.
What do we have in here?
So what we need to do Zu slunk.
Now cede to local.
Let's examine.
What do we have in here?
Nothing.
So what we need to do as a best practice, it's always advised not to change anything under the default.
So make those changes into the local directory.
So what we can do, we can go back to our default.
And then we can copy the inputs from here and paste it into under the local directory.
So what I'm going to do, I'm going to do copy.
Minus R.
Of the inputs and I'm going to paste it under opt Splunk.
Its C deployment apps splunk to for windows under the local.
So we have done that.
Let's go one directory up and let's go back to our local.
And now we have the inputs.
So let's examine the inputs and let's make those changes.
Inputs dot com now.
And here what I would like if you remember from the previous lessons, I would like actually to monitor
the event log for application.
So I'm going to change that to zero.
So I'm going to activate it.
But also, if you remember, we have already specified the index windows under the index or one, and
we need to also specify this in the inputs dot com.
So let's do that.
What I'm going to do in here, I'm going to add index equal to Windows as the destination index for
the monitored logs that I'll be collecting from here.
Let's go further down.
I'm going to do the same in here as well.
So to zero.
And I'm going to include as well my index equal to Windows for system level logs as well.
I'm going to activate it and I'm going to add also the index equal to Windows, which is the one that
we've created earlier under the index or one.
Now, for forward events, I'm not going to do that.
Let's move ahead.
Directory services, No key management, DNS server, no DHCP.
No, we don't need that.
Maybe Windows update.
Let's do that as well.
Let's keep it to zero and then index equal to Windows PowerShell.
It's up to you.
You can enable that or not, but for the sake of this demo, I'm not going to do it.
So let's move ahead.
Scripted inputs.
Yeah.
Listening ports.
Yeah, we can do that.
So let's change that to zero.
And let's include the index windows in here.
And installed apps.
I'm not going to do that.
Time sink.
Net address?
No.
Let's move ahead.
So health and topology information and six No.
Let's move ahead and examine the other monitoring input stanzas in here.
So no host monitoring.
Yes, let's actually enable that one.
This is scripted input.
So enable that and then include the index windows.
This is going to run on a time interval of 5 minutes.
So actually 10 minutes because there's 600.
Ten times 60.
So in the wind host as well.
I'm going to include that as well here so index.
Equal to Windows and I'm going to activate it as well.
Processes.
Yes, definitely.
Index equal to windows.
I think this is enough.
So let's save that.
Let's make sure that the ownership is Splunk.
Splunk?
Yes.
Now, let's deploy this to again.
So let's go to our folder management.
And let's go back in here.
So what I can do, actually.
We can reload the app.
So all the apps that we have under the deployment apps which are here, we can reload them.
So.
Let's do that then.
Splunk.
Reload.
Deploy.
Server.
So the reloading of the server classes has been done.
Now let's do a refresh.
Let's wait for a while.
So now that we have reloaded our server classes by running this command.
So let's go ahead and do a refresh.
So let's go now to our search head.
And let's examine if we're actually receiving anything on the index windows.
So now we have successfully deployed the windows to on my windows local machine, which is this one
in here.
And we have made some changes to our windows to by copying the input from the default directory to the
local directory, which is regarded as a best practice.
Never touch the default, always make the changes under the local because the local directory takes
precedence over the default directory.
And now we can see actually the logs in here.
So now we are done with the first use case, which is this one.
Let's go ahead and actually deploy the Linux to on the universal folder which is deployed on this Linux
machine.
So to do that, let's go ahead to the folder management again.
Let's go to server class.
Remember, I'm not going to first deploy the Linux to because first, as we have done that on the Windows
day, we need to make some changes to that.
To So you remember that we have named our index Linux on our Indexer one.
So we need to make sure we include that and the Linux to.
So let's go ahead to our deployment server.
And examine the Linux to sow seed opt Splunk at C deployment apps.
Let's check the different apps.
And this is the app that I'm going to be changing the configuration to.
So CD Splunk to NICS.
Now we have the default and let's make sure to create.
First the local directory.
So do.
Make directory local.
And now let's go to the default and copy whatever we have under the inputs to the local.
So seed default.
I'm going to go to the inputs dot com.
So copy.
Pseudo copy minus ah inputs dot com to.
Opt.
Splunk.
C deployment apps.
Splunk to NICS and then local.
So let's move one directory up and let's go to the local now.
We have the inputs in here.
So sudo nano inputs dot com.
Now and here what I'm going to do, I'm going to leave the scripted inputs.
And I'm going to actually check.
If we have some monitoring stanzas in here.
So let's examine.
So these are scripted inputs.
Still.
Scripted inputs.
Yeah.
Monitor.
So I'm going to change that one.
So I'm going to put zero and I'm going to include here the index Linux.
Here as well.
Zero.
And index equal to Linux.
Let's move ahead.
Monitor it sea.
I'm not going to meet that anyways.
BASH History.
Yeah, we can do that as well.
So false.
And then index equal to Linux.
Let's examine the other stanzas, what we have.
Again, I'm going to leave the scripted inputs because we're going to deploy those to our next use case.
So these are all scripted inputs.
So let's go ahead and save that.
That should be OC.
Now, remember.
Don't forget to change the ownership in here.
So sudo chan minus are splunk Splunk to the local.
Hit enter.
And now what I'm going to do, I'm going to go ahead.
So now that we have the links to ready, let's go and create a new server class.
I'm going to call it Linux underscore to.
So let's save that.
So now I'm going to choose the Splunk tier for next.
Save it.
At clients, of course.
And here I'm not going to deploy it to all my universal photos, so maybe I could deploy that to universal
forward or two.
So let's do that together.
So let's go back in here.
This is the universal folder, too.
So what I'm going to do, I'm going to copy this.
Paste it and I'm going to put a star for Wild Card.
So let's review.
And here you see.
So there is a check mark in front of it.
So let's save that.
Let's edit it.
And let's trigger also a restart of the Splunk demon.
So let's click on the T and you can see it has been deployed.
So now what we need to do, we need to go to the search head to verify we're actually receiving anything
at all.
So let's check that.
It's going to take a while, but let's give it a moment.
And as you can see now, we have verified as well that we're receiving the logs from our universal forwarder
to where we have just deployed the Linux to to.
So basically.
This one.
So we have successfully done that for the windows or the universal folder too, as well.
So now what I'm going to do, I'm going to deploy the same Linux to to the universal folder one, but
I will make some changes to that, Linux to.
So basically I'm going to create another to this one, but I'm going to just activate some of the scripted
inputs and I'm going to deploy it only to my first universal folder.
So to do that I'm going to do sudo copy minus R.
Splunk to NICS, and I'm going to name it, maybe Splunk to NICS.
Underscore scripted underscore inputs.
So now.
We actually have a new TA, which is this one.
So let's examine that.
So CD to Splunk, to NICS.
Scripted inputs.
La la.
Of course I need to go to the local now.
So seed local.
So now I'm going to do sudo nano input scum.
And here I'm going to do enable this one.
And I'm going to put in dex equal to Linux underscore system.
Now, if you remember from the previous section, I have created the index Linux underscore system under
index r one.
And we have discussed that this one is going to be only for system level logs which are going to be
generated as a result from running these scripts.
And this is exactly what I'm doing.
So let's go to the PS Matrix zero.
Index equal to Linux underscore system.
Let's check the other ones.
Maybe interfaces.
That would be a good one.
So.
Index equal to Linux underscore system.
Let's check the other ones.
Maybe CPU.
That would be a good one as well.
Zero.
So index equal to Linux underscore system.
VM stats.
No, let's check the PRS.
Yeah, this one would be okay as well.
So let's include the index Linux underscore system.
Top.
That would be a very good example.
Index equal to Linux underscore system.
So basically these Tas is going to make our life a lot easier because it's going to facilitate the onboarding
of the data and you have already everything parsed correctly.
But of course there are some scenarios where you don't have a TA and Splunk base, and for that case
we will need to actually do the onboarding and the parsing of the data manually, which we will do it
in our next section.
So let's do index equal.
Index equal to Linux underscore system.
So I think that should be enough.
Let's save that.
Let's do check that.
Of course, we need to go in here and let's do sudo chon minus r splunk splunk opt.
Splunk, it's C deployment apps.
So I'm making sure to change the ownership of my
directories.
So you can see now it's Splunk.
Splunk.
So now that we have our add on ready, let's go to here under the forwarder management.
And let's deploy this add on to our first universal forwarder, which is this one here.
So let's do.
Delete that and let's create a new server class.
So I'm going to call this one Linux underscore to underscore scripted inputs.
And this is destined only for Universal folder one.
So let's save it.
Let's add the app that we have just created.
So scripted inputs.
That's the one.
Save it.
Let's add now the client, which is the UDF one.
Of course, the UDF one.
If you remember, I didn't name it correctly and it should be this one.
So let's copy it, paste it, preview, Save that.
So now let's do an edit to trigger the Splunk restart.
Save it.
Let's go now to our next scripted inputs.
And you can see it has been deployed successfully.
Now, to verify if you are receiving anything, let's go now to our Linux underscore system.
And let's check if we are actually receiving anything at all.
If you remember, this is a scripted input which runs on intervals.
So we need to give it some time.
And here you go.
So you see that we are now receiving the logs from our universal forwarder one.
