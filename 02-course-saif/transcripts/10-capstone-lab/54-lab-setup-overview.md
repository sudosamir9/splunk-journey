---
course: saif-admin
theme: 10-capstone-lab
lecture: 54
lecture-title: "Lab setup Overview"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/10-capstone-lab, transcript, kind/video]
---

# Lecture 54 — Lab setup Overview

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

In this section, we will be implementing our last and final lab, which is part of the Splunk Enterprise
Certified Admin course.
Now, before we deep dive into our Splunk lab set up, let me give you an idea and an overview about
the different Splunk components, as well as the different data collection methods that we're going
to be implementing throughout this lab.
Also in this lab, we will be simulating different use cases taken from the real world.
So if you remember from the previous slides, we've already shown you how to configure an edge ship
event collector and forward those requests to the indexing tier.
On the other hand, as part of the network input, I have shown you how to configure a FortiGate firewall
to forward the logs via syslog to the indexing tier.
Furthermore, we have shown you how to deploy and configure a universal folder on a Windows machine
and then deployed the windows to that.
We have downloaded from Splunk Base to monitor certain files and directories and forward the logs to
the indexing tier.
Similarly speaking, we have shown you as well how to deploy and configure a universal folder on Linux
based machines and then leveraging the Linux to that.
We've downloaded as well from Splunk based to assist us into monitoring certain files and directories
on this Linux machine and forward the logs to the indexing tier.
Lastly, as part of the scripted inputs, we have shown you how to create a custom app leveraging some
preexisting scripted inputs that would run on a scheduled interval to pretty much collect diagnostic
data from voice commands and forward the output to the indexing tier.
So all what we have learned in the previous slides, we will actually implement these different collection
methods throughout this lab.
Now, while it is okay to forward the logs from the universal folders to the indexing tier directly,
however, in the real world it's almost always advised to have intermediate folders in between.
Now, the reason why a lot of customers would have these end machines, whether they are Windows machines,
servers or Linux machines, was going to be deployed in different geographical locations.
So there could be a problem that the network bandwidth is limited.
So these intermediate folders could act as a relay.
Also, maybe there are certain use cases where you're going to be forwarding data which contain sensitive
information.
Take the example of credit card information.
So you don't want to store such sensitive information directly on the indexer.
So what you want to do is you want to manipulate the data.
So basically, as it transits and flows through the intermediate forwarders, maybe you would like to
apply some certain data masking as it flows throughout the intermediate forwarders.
So the end result is that the data while is going to be written into disk, it's going to be manipulated
or masked.
Now remember that we will configure these universal forwarders to actually perform automatic load balancing
of the data.
So in essence we will instruct this universal forwarder first to forward the logs to the first automated
forwarder and then to the second intermediate forwarder.
This is very much important for data consolidation as well as for full tolerance.
Now once we are done with this.
What we're going to be doing is instead of applying and deploying the configurations and what I mean
by that, the custom apps and add ons directly on these universal folders.
Instead, we will be relying on the deployment server that we're going to be using it as a tool to manage
all these deployments from a centralized location.
This is very much true in very large environments where it's going to become really difficult to keep
track of every single universal folder.
So instead we will be using the deployment server to facilitate this job for us.
