---
course: saif-admin
theme: 10-capstone-lab
lecture: 56
lecture-title: "Splunk Deployment Walkthrough in a distributed Environment"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/10-capstone-lab, transcript, kind/video]
---

# Lecture 56 — Splunk Deployment Walkthrough in a distributed Environment

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

In this section, I will walk you through how to deploy the different Splunk components in a distributed
architecture design.
So let me bring my notes to the front and then let's discuss that briefly.
So as previously mentioned, throughout my last two sessions, I have given an overview about our lab
setup.
So basically this one.
And we have identified a different components as well, the different methods in terms of data collection
and what we're going to be implementing.
Then in the second section, I have shown you that the best way to actually deploy this lab is to create
an account.
And then I have shown you as well how to launch a server instance and then taking care of all the basic
configuration and accessing and connecting to that instance.
Now, for the folks out there, again, if you feel that AWS is not the choice or the right choice for
you, you can always also rely on VMware Workstation, where you're going to be deploying it on your
local machine.
And of course, you can deploy all the different components of Splunk.
Obviously, if you're going to have enough hardware specs, then you could go with this method of deployment.
So the choice is yours.
So let's go back to our notes.
Now, in this section, however, what are we going to be doing is.
So let's go through these steps, deploy the indexes and configure the monitoring console.
So first things first.
In such an environment, what we need to first focus on is to actually deploy the two indexers.
So what I'm going to do, I'm going to first deploy Indexer one and Indexer to.
And then.
I will set up the monitoring console.
I will deploy it on a separate instance.
And then once we are done, I will then deploy the search head and adding it to the distributed environment.
So we would want that all our Splunk nodes, except for the indexers, to have all of them forwarding
their internal logs to the indexers instead of indexing them locally.
So this reduces disk space usage and it makes as well the internal logs for all the Splunk nodes searchable
without having to necessarily logging in on every single Splunk component.
So basically, we would want to insert the heavy forwarder, the intermediate forwarder, the intermediate
for the one and two, as well as the different Splunk auxiliary components.
And by that deployment server monitoring console as well as the search head to forward their internal
logs to either one of these.
So for the sake of this lab, I'm going to be choosing index or two to parse and index all the different
internal logs.
Now, once we are done with this, I'm going to be configuring the monitoring console in a distributed
mode.
So let's go back to our notes in here.
Now, follow my best practices where I walk you through configuring the you limit and disabling the
PHP in previous sections.
So for the sake of this lab, I'm not going to configure the ultimate or disabling the transparent huge
pages because I've already provided a demo on how to do this.
So I would encourage you to go ahead and follow the previous sections where I have explained that and
also provided a demo on how to do it.
Now, once we are done with this, I'm going to do post installation checklist.
And then we will deploy the intermediate forwarders and deploy the universal forwarders.
But we're not going to do any configuration, just deployment.
And then we will go ahead with the deployment server and we will configure it and then we will configure
those intermediate forwarders as well as the universal forwarders to be acting as deployment clients
to our deployment server here.
Once we make sure that those universal forwarders and intermediate forwarders and the heavy forwarder
is showing actually under the deployment server, then it becomes the interesting part where we're going
to go ahead and configure our custom apps and add ons that we will actually deploy through the server
class to all of these different universal forwarders as well as the intermediate forwarders.
Lastly, we will configure the hack on this heavy forwarder as well as we will configure a firewall
to forward the logs via syslog.
In this case is going to be a FortiGate firewall to the heavy forwarder.
So once we are done with this, we can end our lab with data onboarding.
So basically we will prepare a test environment to test our sample data and of course we'll make sure
to get the meta data fields correctly from the beginning.
And obviously we will actually use the data viewer and use the props dot com to get this data pass correctly.
So basically we will make sure to get the timestamp correctly, identifying the event boundaries, field
extractions and obviously we will walk you through all of these different controls that's going to help
us into parsing our data.
So let's go ahead and jump to our lab set up.
