---
course: saif-admin
theme: 07-data-flow-concepts
lecture: 37
lecture-title: "discussion on Data Collection Methods in a distributed environment"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/07-data-flow-concepts, transcript, kind/video]
---

# Lecture 37 — discussion on Data Collection Methods in a distributed environment

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

Splunk supports many types of data input so it can collect the data as an input in so many different
ways.
And this gives us a lot of flexibility and different options where we can explore based on our infrastructure
and how it's set up.
And we can choose the best methodology for data collection.
So let's first discuss monitoring files and directories.
This option, we can deploy the universal forwarders, whether they are on Windows machines or Linux
based machines, and then we can instruct these universal forwarders basically to monitor certain files
that we want and then forwarding them to the indexing tier.
So let me show you that.
So these are, for example, the universal forwarders.
Oops.
So these are the universal forwarders.
Deploy it on a Linux or a Windows machine.
And then they're going to monitor certain files that we want, and then we're going to send that to
the indexing tier.
This is one way to do it.
Of course, as a best practice we normally send those logs from these universal four is deployed in
here to another universal forwarder acting as an intermediate forwarder.
Or what you can do as well.
You can send the traffic directly which is monitored on these end machines to the indexing tier directly.
So let's go back.
Now the second option is to receive syslog logs on a port.
So pretty much you can configure the firewall, a proxy or any server to send syslog messages to the
either universal forwarder, which is going to be acting as a centralized syslog server.
And then the universal forwarder will relay those logs to the index linked here.
So let's go back in here.
So here you have a bunch of firewalls servers where you can instruct those firewalls, servers, proxies
to send syslog messages to an intermediate universal forwarder acting as a syslog server.
And this universal forwarder is going to forward it to the indexing tier.
Also, you can also send that directly.
To the indexing tier without having a universal forwarder acting as a centralized syslog server.
But this is as a best practice.
So the other way is script execution model input or what I would call scripted inputs.
So you can leverage on the voice command levels to actually use those to gather diagnostic data and
then send the output to the indexing tier.
So what you can do, you can also create your own Python script because Splunk will also support that
as well as PowerShell for Windows.
And you can actually run those scripts on a cron job schedule, time interval, and then forward those
generated outputs to the indexing tier.
We will go one by one and I'll create a demo for all of these Windows logs as well.
When you deploy the universal folder on a Windows machine, you can of course enable it to monitor when
event logs, security registry logs.
If there are any changes to the registry DNS, Active Directory performance to name a few.
Lastly, it's the HP event collector.
So basically what you can do.
So let's go to the graph in here.
So this is pretty much an agent list kind of way of data collection.
So you don't need to have a universal folder.
What you can rely is on an HTTP event data.
So you instruct this machine to send those HTTP event logs to a heavy forwarder where you're going to
have the heck or there should be event collector enabled, and then you can forward those logs to the
indexing tier.
By the way, just to let you know this one here, you don't need an agent.
You just need a way to forward those logs.
Think of the heavy forwarder with the heck on top as kind of an API, and we will discuss this further
in subsequent slides and we will also create a demo about this.
So let's go back to the slide.
Of course, you can configure most of these via the web, but the preferred method to configure the
above is by directly editing the inputs.
So this is how I do it.
And of course I'll be showing you this in the subsequent slides.
So let's move on to the next slide and let's discuss.
So basically, this is the way to collect the logs by configuring the inputs here and the inputs dot
com, you will configure using the different stanzas.
I would encourage you to go to inputs dot com Splunk website where it's going to give you a lot of info
about the different stanzas in the inputs dot com and how you can change and configure those based on
the different data collection methodology and the way you can set it up.
Of course there's a very much important thing.
Of course the inputs, you know, it's the way to configure how you would get the data as an input and
the outputs is the way on how to forward the data which is collected at the input and forwarded to the
next tier, whether it's another universal forwarder acting as intermediate forwarder or directly to
the indexing tier.
So think of it like so like a pipeline.
Of course the props dot com is for data parsing or data manipulation, so pretty much in the data.
So this is the data input which is going to be collecting the data.
And in the output scope, it's going to be sending or forwarding the data and the props dot com is a
way on how you can apply the line breaks to create those events and segment the data.
Of course, you can apply some transforms and can manipulate as well the data for data masking.
And of course then at the end, once the data parsing is done, of course then you're going to go and
write that disk.
So for data manipulation and data parsing, you're going to be working mainly with props, takeoff and
transforms dot com.
So that's that.
We have covered the inputs dot com and the outputs dot com.
I'll be of course demoing about those too and and as we progress throughout the course.
