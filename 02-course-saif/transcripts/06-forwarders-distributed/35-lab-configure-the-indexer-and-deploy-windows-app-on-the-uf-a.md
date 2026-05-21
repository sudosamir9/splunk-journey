---
course: saif-admin
theme: 06-forwarders-distributed
lecture: 35
lecture-title: "LAB: configure the Indexer and deploy Windows App on the UF  and the Indexer"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/06-forwarders-distributed, transcript, kind/video]
---

# Lecture 35 — LAB: configure the Indexer and deploy Windows App on the UF  and the Indexer

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So let's go ahead at the second step to configure the Windows index.
So you can do it two ways.
Either by doing it via the configuration file or you can go pretty much.
From.
So I'm going to go under the admin course app because again, I would like to keep all my work under
one specific app so I know what things have changed.
So if we go to settings.
Indexes.
The easiest way.
Is to create the windows here from new index.
And pretty much.
So then the index name and etc..
I normally tend to do that via.
The clay.
So I'm going to go to.
CD Opt Splunk.
See?
Apps.
Under the apps directory.
I need to go to my admin app.
I need to be.
Splunk user.
I always forget passwords.
There you go.
So, CD admin.
I need to go to the local.
And then I will do.
Indexes.
So I already have the index security.
So what I'm going to do, I'm just going to copy.
These.
Sorry.
Let me just cancel that for a moment and start again.
I'm going to go to the end of the file.
I'm going to pace that.
And I'm going to just change this.
So I'm going to put windows and decks called baths.
Of course, you need to assign the right path for it.
So windows for cold DV buckets.
Data integrity check.
This is pretty much, you know, to check the integrity of it has not been tampered with.
And I'm talking about the index.
I'm going to change that to windows.
I will keep the max total size of the whole index to 500 and be sorry gigabytes because this is an empty
home path for the max data size, which is going to be for the hot and warm 300 and be no, I'm going
to keep it well under real life scenario.
That would be at least I would say.
100 gigabytes.
This is the max data size of the hot pocket.
I will keep that to 10,000.
So.
Thought path.
Fine.
Maximum hot buckets.
I would say three.
Then we will grow and that's it.
So control X, save the configuration.
What I'm going to do.
I'm going to just.
To take this effect.
So hit enter.
Just going to remove this.
Debug.
Refresh, hit enter.
So all the configuration changes that we've done to the indexes dot com under my app, it's going to
reload those.
So let's wait for this to finish.
Now you see, we don't have the windows yet.
We are done reloading the changes.
Let me just do a refresh.
And there you go.
We have the windows.
Index just created.
Of course, we can enable and it's already disabled, so I need to enable that.
Let me just enable, enable.
Let's see what things has changed when I have enabled that.
So let's do a refresh.
So now it's enabled.
Let's go back to the configuration.
Let's examine.
Now this is the windows.
Take a look.
Disabled equal to zero because I forgot to put that.
So again, disabled equal to zero means that this is now activated.
If I put it to one, that means the disabled is is enabled.
So that means this is going to be disabled.
So always when you want to enable something.
Put this equal to zero or put it equal to false.
So now we have created the Windows index.
We have configured the universal folder on this Windows machine, and we made sure that the internal
logs are being received at the indexer.
Now we will go ahead and deploy the windows, add on from Splunk Base.
Now this add on again, as in the previous slides, this is going to facilitate our life because this
is pretty much an app which is going to help us to pass those logs and do some regex extraction and
pretty much field extraction.
And then it's going to create for us all the different events throughout the parsing pipeline.
And you will see in a moment how this add ons and apps can make our life a lot easier.
So let's do.
Delete this.
Let's go to Splunk Base.
Let's hit enter.
Let me zoom out.
So I'm already logged in.
Let's search for the Windows app.
So windows.
I need the Windows add on for Microsoft.
And this is supported by Splunk.
It's maintained by Splunk.
So I'm going to download it.
Let's wait for it to finish.
By the way, if you see here, this is the app ID under Splunk based.
So let's download it.
Except agree.
Okay.
And download.
So let's open that.
I have it in a different window.
So bear with me a moment.
So I unzip the file.
And this is the file?
Pretty much.
Now what I'm going to do.
I'm going to take this file.
From here and I'm going to paste it here under Splunk, Etsy Apps.
Now, this file is there and ready.
But let's examine this file.
Let's go.
By the way, there's no local because this is the default.
So it's like the out of the box configurations, which is coming basically with the Splunk windows add
on.
So let's go to the default.
You see, these are different configuration files.
Let's take a look at the input stock of let's open that file.
See my notepad plus, plus.
Now you remember in the inputs dot com is where we are instructing the universal forwarder.
To either monitor, to listen on a specific port for incoming data or logs, which we want to monitor.
So let's go.
And this is self explanatory.
Or as long as it's disabled equal to one, I'm going to change that to zero because I want to collect
these logs from the event log application level logs whenever event log security.
Yes, I will switch that to zero as well.
Let me zoom in.
System level logs for my windows machine.
Yes.
I want to also collect those.
Those and those.
What else?
Let's take a look.
Let's leave this.
We don't need that.
This is when event logs inputs for Active Directory.
So if you want.
So pretty much this add on which is in the background takes care also of the Windows endpoints as well
as it provides configurations which are offered after the box to be activated to monitor certain lock
type also for Active Directory.
We don't need that because our Windows machine is just an endpoint.
It's not an Active Directory would have been logs for DNS.
I don't need that.
Windows update logs.
Yeah, I would go for it.
Monitor inputs for Active Directory.
We don't want that scripted inputs.
I don't want that.
Installed apps, no time sync status.
We don't need those Active Directory again.
We don't need those.
Scripted inputs for dance.
I don't need that host monitoring.
So for the computer, yes, I want that put zero instead of one.
Processes.
Yes, I want to know what processes are running in the background of my windows machine to be monitored.
This one as well.
Network adapters.
Yes, of my Windows Machine services which are running.
Yes.
Operating System Windows Postman.
Yes.
Disc.
I want to know more about my disc drivers.
Yes.
So all switch it to zero.
I think we are pretty much done.
Outbound traffic as well.
So network performance.
This is for the performance.
Of course you can do that as well.
Yeah, I'm going to go and activate it for the process for the network.
Process information.
Yeah.
You need, you know, to spend a bit time to go through these.
So and in the end, we want also to monitor any changes to the registry.
So let's go for that as well.
So this is for the hardware.
So this is sort of the software.
This is at the user level.
This is at the machine level.
So we should be good.
Let's save that.
Save it.
So now changes has been done on this.
There is one important thing that we forgot.
What is it?
Let me go back.
So we are we have activated this and this and this.
All of these.
A moment ago.
But if you take a look in here, we didn't specify the index.
So we are monitoring those logs.
But what index?
We want these logs to be monitored.
So we need also to do that.
So what we need to do is we need to specify index equal to windows because we have created this index
under our indexer.
So copy.
Based.
Paste in here.
We didn't touch anything about Active Directory.
Let's move on.
We didn't enable this one.
We enabled this one disabled equal to zero.
You see here.
And we didn't touch anything about these.
Let's move ahead.
Script network now disabled equal to one.
Still, we didn't touch these.
Also these we didn't up for host monitoring.
Yes we did that we need to confirm and put also the index as the destination.
Also for this one.
Network adapter, this one.
This one as well.
Operating system level logs disk.
Information, driver information.
We need to act.
We need to all send those to the Windows index.
No, this one is not.
One won this one as well.
Network monitoring, this one as well.
This one as well.
We didn't activate anything of these.
This one disabled equal to zero processes, of course.
This one as well.
System level logs.
Yes.
Nope.
Not this one.
Not this one, but I remember for the registry.
We have done it.
Yes.
By the way, it's of your choice.
You can create another index, you know, under the indexer, and then you can when you when you come
to the activation part of these stanzas at the inputs dot com, you can specify a different index.
It's really up to you.
This is to be discussed upfront with the customer.
So for performance logs you can put it into the performance index.
So let's say that.
And let's go.
To our services and restart.
Our universal forwarder.
So let's go back to our.
Indexer.
So what we have done now, let me show you.
We have configured the windows, the universal folder on this Windows machine, and we have deployed
also the add on for Windows and we have activated input icons, which we have shown you just a moment
ago activated some stanzas which are often out of the box from this add on and then which we're going
to instruct this universal forwarder through the inputs dot com to monitor these files.
Then forward those to our indexer under the Windows index.
So now let's go to the index windows.
And let's put the last maybe 15 minutes.
Take a look.
At this.
Look at the logs.
So we are receiving the logs from my machine.
I'm putting everything under the Windows index.
Look at the local ports.
Look at the processes.
Look at the process names.
The protocol that my Windows machine is using.
Remote addresses, sources.
These are the sources and the source types that we are collecting and that we have activated on that
input in that universal folder where it's deployed to my Windows machine.
Let me show you how this Windows app is making our life so easy by doing all the parsing and the field
extraction.
Now, within the last 15 minutes, we have been collecting all of these locks from the Windows machine.
The command lines that I've been using.
CPU load display name.
This is the host, which is my PC.
This is the index, local addresses.
Everything is being collected for this Windows machine.
The Mac addresses local ports.
Let me show you process CPU usage, Process ID.
Process memory, the different processes which are running in the background.
Process name or the product name and the protocol.
Take a look at the protocol ICMP.
So let's take a look at the ICMP.
Now, let me just open.
Kelly what I'm going to do.
I'm going to Pink.
First, let me change that to real time the last one minute.
Let me just think from my computer.
Take a look.
So start to come in ICMP remote address.
8.8.8.8.
What I'm going to do.
WW dot LinkedIn dot com.
There you go.
It's coming in.
So imagine all of this could be monitored in real time.
So spend some time on this app because it's pretty much very important to familiarize yourself with
all the different fields which are being extracted using this add on from Splunk Base.
