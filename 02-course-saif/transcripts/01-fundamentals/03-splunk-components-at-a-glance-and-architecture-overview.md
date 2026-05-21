---
course: saif-admin
theme: 01-fundamentals
lecture: 3
lecture-title: "Splunk  Components at a glance and Architecture Overview"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/01-fundamentals, transcript, kind/video]
---

# Lecture 3 — Splunk  Components at a glance and Architecture Overview

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So you remember from a previous slide where I was showing to you about the data flow ingestion flow
from the data input process through the different pipelines up to the search part and the standalone
fashion.
But now we will be going to the second part or the second architecture where I would say, where are
we going to be offloading the job of data input to dedicated machines a.k.a the forwarders.
Now let me show you that exactly what I mean.
So as a best practice, we would deploy the forwarders which are responsible for the data collection
part to the desired end machines to collect the logs from universal forwarders, typically the raw data
and the forwarded without any prior treatment.
Now let me give you an example.
So typically we will deploy.
Those forwarders.
As a pre-installed package to these end machines, which is this this pretty much this Linux server.
What we will be doing is we will instruct those forwarders to actually monitor the internal logs of
or the system level logs of this machine.
Ultimately, all of these logs will be forwarded by the forwarder package which is installed on this
machine.
To the Splunk instance for further data parsing and data indexing.
So.
Pretty much, you know, the forwarders is being offloaded from the Splunk instance.
Similarly is with the search head.
So the search heads.
As a best practice.
And in a real world scenario, we would deploy those instances or this role on a dedicated component
or machine to perform high intensity, dedicated search queries.
And this is typically done this way.
So let me show you exactly what I mean.
So we just talked about the forwarders, which we're going to be deployed on these servers and they're
going to be responsible to monitor the logs of your choice.
And then those will be forwarded to the indexer.
Now, the indexers are also dedicated machines, which they will do only this part.
And data parsing part so they can to parse those logs which are being received from the forwarders.
And they're going to pretty much break these data logs into events and parse those data and provide,
you know, all the key value pairs.
And then you as a user sitting in here.
Through dashboards, search and monitor, report and analyze.
You will go ahead and create queries to actually search the data which has been just indexed.
So.
Instead of having a one standalone architecture, which is pretty much useful when it comes to self
learning.
Testing, you know, posses proof of concept.
We will be using pretty much the standalone Splunk, but for more advanced and more high intensity searches
and real world scenarios will be more into this architecture flavor.
We will be dedicating the search hat's part, you know, to dedicated machines and the indexers as well
as well as the forwarders.
Now you see this deployment server.
We will be talking about that in subsequent slides.
One last thing that I would like to talk about is.
All components get installed from the same Splunk package.
It is just the configuration which changes the Splunk behavior.
So what I mean by that now, when you install Splunk.
And we will be showing that in the next slides.
It all has all of these components.
It just you as a user, you will go ahead and configure the Splunk instance to act only as a search
head or only as an indexer or only as a forwarder.
So for here, for example.
It's still a standalone, but we're offloading the forwarders and here we have configured this instance
to act only as a search head.
Similarly, here to act as an indexer and here also as a forwarder.
