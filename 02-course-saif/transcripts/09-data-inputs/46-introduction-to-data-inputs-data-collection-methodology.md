---
course: saif-admin
theme: 09-data-inputs
lecture: 46
lecture-title: "Introduction to data inputs ( data collection methodology )"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/09-data-inputs, transcript, kind/video]
---

# Lecture 46 — Introduction to data inputs ( data collection methodology )

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

In this section, we will be discussing the different data collection methodology and how we can determine
the best option based on our requirements within our infrastructure for data collection.
So let's take a closer look at this diagram.
So first what we can do is to deploy the universal folders on either Linux based distribution machines
or Windows based machines and instruct this universal forwarder through the input stock.
Conf here to monitor certain files and directories in here and forward these logs through the output
dot com configuration to an universal folder which is acting as an intermediate forwarder, kind of
like a central container, and then take these logs and forward them to the indexing tier.
Now this is one way to do it, and this is the preferred method that I have seen so far with customers.
There is also the other way, which is.
To instruct firewalls, proxies, servers to actually send the the event logs as a syslog message.
To a dedicated Splunk machine.
So pretty much think of this as a Linux machine where a universal folder is running on top, and then
this machine is configured to listen on a specific port.
Let's say 514.
Waiting for incoming traffic to be passed and processed.
So the universal order here, which is acting also as a centralized syslog server, is going to forward
the logs to the indexing tier.
This is the second way to do it.
Now, of course, what Splunk can do.
We can also.
Create scripted inputs.
So on these end machines, what we can do.
Splunk offers the possibility that we can pretty much create scripted inputs which run on a scheduled
specific time frame through a cron job and the generated output is collected and then sent to the indexing
tier.
Think of these scripted inputs like or as command level.
So, for instance, if we go to here.
So if if I want top for instance, like this.
So this is the output.
So this script enables us to collect this data.
Okay, let me just delete this to collect this data.
Through the scripted input.
By running our level commands and then forward that to the indexing tier.
And we will see that in the next slides like the top.
PS minus F, for instance, What are the running processes in the background?
So Splunk, you can run with Splunk like Shell script or Batch or PowerShell on Windows as well as Python
scripts, what you can do.
So this is pretty much a lot of possibilities that we can do.
And of course, we will run through a demo and show you that in subsequent slides.
So let's go back to our.
Slight and then discuss the other option.
Now, the third option or the fourth option is what we call the HTP event collector.
So we will configure a heavy forwarder.
As an extra tip event collector.
Think of this that we're exposing kind of an API.
And this event collector through a tokenized API.
It's going to process or listen for incoming HTTP requests.
So this is what I would call an agent list forwarding.
So the only thing that you need to take care of is on these end machines.
You will need to configure it to send those HTTP event data or requests to the heavy forwarder where
we have configured the heck or the HTTP event collector.
Of course, on this one and on this one, we will need to have the same token.
So this to be event collector will accept only incoming traffic or HTTP requests.
Once we have a token which match the token in here.
Of course these are the different ways what we can do.
But also.
Instead of forwarding the logs to an intermediate forwarder, we can also.
Do that directly.
So the universe of orders here installed on Linux and Windows machines and we can forward the logs directly
to the indexing tier without having a centralized a centralized universal forwarder where it's going
to collect all the logs.
The same with HTP event collector.
You can send it directly to the indexing tier and as well as from the firewalls.
You can also send those to the indexer for data ingesting.
So these are the different ways where we can collect the data.
What I'm going to be talking next.
Is how we can configure.
The different options within the inputs dot com as part of monitoring files and directories.
