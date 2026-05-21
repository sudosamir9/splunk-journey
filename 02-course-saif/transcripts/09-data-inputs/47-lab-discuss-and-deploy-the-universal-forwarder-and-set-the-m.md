---
course: saif-admin
theme: 09-data-inputs
lecture: 47
lecture-title: "LAB: Discuss and deploy the Universal Forwarder and set the monitoring inputs"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/09-data-inputs, transcript, kind/video]
---

# Lecture 47 — LAB: Discuss and deploy the Universal Forwarder and set the monitoring inputs

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So let's go through the first option of the data collection methodology, which is deploying a universal
forwarder on a Linux machine and then instructing this universal forwarder through configuring the inputs
dot com to monitor specific files inside this end machine and forward the logs to the indexer.
For simplicity sake, I'm going to be ignoring having a universal forwarder acting as an automated forwarder.
So mainly I'll be working with the indexer and with the forwarder thinks as well that I will need you
to know prior to this lab is that on this indexer I've already configured the inputs dot com to listen
for incoming traffic from this universal forwarder.
And also I have configured the outputs dot com on this universal forwarder to forward the logs to the
indexer.
I'll be showing you that in a moment.
Also, we will create an application or an app on this universal forwarder.
So let me show you that.
So here I have my universal forwarder.
And here I have the indexer.
So let's jump ahead first and create the indexer in here.
So I'm going to be going to settings.
Index.
I'll create a new index.
So I'm going to call it security.
Save that.
We already have a security, so I'm going to just call Linux.
Save that.
We already have the Linux here.
And it's enabled.
So now we're done with that part.
Let's go back to our diagram.
So what I'm going to do is.
I'll be creating an app.
Under the universal forwarder.
And I'm going to configure the input stock conf in that app.
So let's jump ahead to the universal forwarder.
So first.
Let's go.
To see.
Apps.
So let me just create zero.
Make directory UDF underscore.
So you need to follow a kind of a certain naming convention for this.
You have base inputs.
Simple.
It's great that.
Now under here.
To the UDF base.
The structure is you need to create a local and a metadata file, a directory.
So let's do.
Local.
And.
Create a meter.
Data.
So now I have the local.
And I have the metadata.
So before I start to actually create the inputs dot com in here.
Let's examine the metadata.
So let's go ahead into the metadata.
And let's create.
Local.
Dot metta.
So what is the local matter?
So the dot meter extension files contain ownership, information, access control and export settings
for Splunk, objects like safe searches, event types and views.
Each app I would recommend when you create it, create always that and do copy the following.
And put it like this.
So you're providing pretty much access, read access to everyone and write access only to admin and
you want to export that to system so everyone you can declare this as global.
So let's save that.
So now.
We have the local matter.
Of course, you need to bear in mind that this is root, root.
And we need to change that to Splunk.
Splunk.
But let's ignore that for a moment.
And now we have local and metadata.
So let's go to local and let's create.
The inputs.
Actually, before I want to jump ahead and create the input scores, I would like you to share.
I would like to show you something.
So let me just add la var log.
So let me just expand this a bit.
Now you see.
These are all the log files of the system level of this Linux machine, which are all of these?
Now, what I would like to do is the first use case scenario.
I would like to create an input of where I would like to monitor everything in here, how we do that.
So let's go ahead and remember, this is under.
Var log directory.
Everything in here I want to to monitor.
How are we going to do that?
So sudo nano.
Inputs.
Don't cough.
So.
The first thing that I will do.
I will create the input stock of.
So let me just copy and paste.
Now, this is the monitor stanza.
And this is exactly the, you know, the path to that directory, which is the VAR log.
And underneath you will have all the logs that you would like to monitor.
So pretty much you're instructing Splunk Universal forwarder to monitor everything under this.
So the index, of course, is not test.
As you remember, we have created the Linux index.
So I want to instruct whatever you're going to be monitoring under that log.
Please send it to the Linux index source type Linux secure.
So let's save that.
Now what I'm going to do.
We have created this first app.
So now I'm Jonah.
I'm going to.
Sudo change ownership of this file and directory and all subdirectories.
So by doing.
Splunk.
Splunk minus R recursive.
And then.
US.
So I have changed the ownership.
Splunk.
Now, if we do UDF, also this.
So our application or our app is now ready.
Of course, if we go back to the diagram, I've only configured the index, the input stock in here,
but I never configured the output stock conf to forward these logs to the indexer.
So let me just do that.
So let's delete this.
Go back in here.
City local.
Actually we need to do D udf local and then sudo nano outputs dot com.
So let's create the output scope as well.
No.
This is the TCP out stanza default group indexes.
And I have also mentioned that in here and the server IP address is ten 10.10.
So.
It's this one.
This is the indexer.
So IP address stand up 10.10 ten and I want the destination port to be 9997.
So let's save that.
Don't forget that it's now root.
Root.
Of course we need to do that as well.
So sudo chon.
Minus R or without an R in this case, because we want to do that only for the outputs.
So.
System is ready.
So let's go back to the indexer.
So I have changed those configurations, but yet I didn't enforce it.
So whatever changes I've done to the configuration file still didn't enforce it.
So I need to restart the universal folder.
But let's examine the indexer first.
So Linux.
So I don't have anything within the last 24 hours.
So what I'm going to do.
Sue slunk.
So I've changed to Splunk.
So let's do.
Restart the slunk.
Restart.
Provide the password.
Stopping.
We're starting the demon.
Now.
Let's wait.
Now to know that even if the universal forwarder is actually sending the internal logs to the indexer.
Let's go back just to make sure that it is.
Let's go to Internal.
Let's see the host.
Actually, we have.
So let's.
You know, do that the last 15 minutes.
Just making sure that the universal forwarder is actually forwarding the logs and we are receiving the
logs from this universal folder.
And in fact, we are receiving the logs from the universal folder.
And as you can see in here, this is the timestamp.
So yeah.
So we can even do stat's account by host one of the last 15 minutes.
And in fact, this is the universal folder that we have we are receiving.
So let me just delete that now and let's examine if we're actually.
Did that successfully.
I was receiving any logs.
Oh.
And here we are.
So to examine the data.
I've done it for the last 15 minutes.
The host is the universal forwarder.
As you can see, the indexer is Linux, the one that we've created the processes.
Sources.
So we are actually receiving, but we need to wait for more time.
So let's actually do all time.
Let's see if we're actually receiving more and more.
In fact, as you can see.
Var log.
So let's do that actually by source.
So stats count by.
Source.
Let's examine that closely.
So everything.
Let's let's go back to that oct so var log.
So everything in here under the VAR log directory, as we have instructed the universal forwarder to
monitor anything under this which are all of these.
We are actually receiving those.
So let's do a refresh one more time and see.
And as you can see, var log alternatives of cups d message.
Where's the RD message?
RD message?
We are pretty much.
Ingesting actually forwarding everything under the VAR log directory.
