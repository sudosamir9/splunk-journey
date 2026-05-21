---
course: saif-admin
theme: 07-data-flow-concepts
lecture: 38
lecture-title: "Discussion on Metadata Fields and data flow (continuation )"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/07-data-flow-concepts, transcript, kind/video]
---

# Lecture 38 — Discussion on Metadata Fields and data flow (continuation )

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

As previously mentioned, slang can support different ways on how to collect the data.
And depending on the data collection methodology that you're going to be using in your infrastructure,
you need to configure the input file with the proper settings.
So each stanza controls a certain behavior that could be applied on the Splunk instance.
So I would encourage you guys to actually go ahead and explore the input stock conf As it says here,
the file contains possible settings that you can use to configure inputs.
So there are global settings which are applied globally and there are settings which are applied per
stanza.
So I would encourage you to go through these and of course I will mention most of the different stanzas
and controls that you're going to be using throughout this course.
So this is regarding the inputs and this is for data collection.
And for instance, you want to configure your universal folder to monitor certain files.
Of course, then you will need to use the monitor stanza or you need to configure, for instance, the
universal forwarder here to listen for specific port.
So you will need to use the TCP stanza and so on and so forth as well.
As for scripted input, you will need to use the stanza script for the heck.
For instance, you will need to use the http stanza.
So there are different controls stanzas that you need to use for serving that specific data collection
methodology.
Now this is for the inputs.
Now, when it comes to forwarding this data from here to the next year, then you will need to use the
outputs dot com.
Of course, I will also encourage you guys to go ahead and explore a bit about the output stock of.
Of course, throughout this course, again, I will be demoing and using one of the most important controls
within the outputs dot com that governs the way that you can forward the data to the next tier.
Now the props dot com could be useful as well into the data input and this is pretty much important
when it comes to line breaking timestamps.
RegEx transforms manipulation of the data.
So let me show you that exactly what I mean.
So let me just delete this and go back to here.
And as you can see, this file possible settings, key value pairs for configuring Splunk.
And this is commonly used for configuring line breaking.
So for instance, as you are receiving the data, you want to break the data into events.
Of course, especially this is useful for multi-line events, so you need to know the boundaries of
the event, that beginning of the event and the end of the event.
Sometimes you will need to configure that manually.
Of course you can rely on the default settings that Splunk offer, but in the end, depending on your
data, sometimes you will also need to do that manually as the data comes in.
Now some metadata fields are added and these are the hosts, source and source type and as well as timestamp
and index.
So let's go to the next slide and discuss the metadata fields.
So a Splunk index is the data.
It adds to its subfields automatically and becomes part of the data.
And we call these fields as default fields.
Now, think of these major data fields kind of like a way that's so Splunk can categorize them properly
as part of the data ingestion and then search it at a later stage.
So some of the most important default fields are the host source source type index timestamp.
Now let's discuss those briefly.
So let's discuss the host.
So the host is like the host name of the machine, sending this data as part of the data input.
So let's go back in here.
So what I mean by that, usually when you have a universal folder and here deploy it to a machine,
that's exactly going to be the host name.
So it's going to be present as the host name of the machine sending the data.
Or it could be actually as well, the firewall.
So if, for example, you have a FortiGate firewall, in my case, it's a 10.10, 10.1 90, for instance,
or an actual domain name that's going to be the host name of the firewall.
So this is equal to the host name.
So let's go back and discuss the source.
So the source is the genetic file name where this data is present when being monitored or the full path
to this file or for data sent via syslog.
So imagine.
So let's go back.
So, for instance, I'm monitoring certain files in here, like under var log syslog or var log messages,
for instance.
So the source is going to be assigned to the var longer messages.
So it's the originating file where you are actually monitoring that file or on a firewall.
It could be the hostname plus the port number.
Now let's go back.
To our slide in here.
And let's talk about the source type.
So the source type is the way to categorize the data so Splunk can know how to format it.
It's like a reference.
So it's it's very important to assign the correct source type.
So let's go back in here.
So.
When the data comes in.
And go to the indexer.
You need to find a way to reference this data to kind of like a point of reference where the indexer
is going to assign it a source type so you can actually categorize it inside the indexer, so you can
assign the source type either at the indexer, but also you can assign it at the forwarder.
So you can assign a source type.
And based on that, it's going to tell Splunk on how to categorize this data so you can search it at
a later stage.
So now one of you guys is going to ask what is the difference between source and source type?
So source and source type.
So again, the source type is one of the most important fields and the default feel that the Splunk
platform assigns to all the incoming data so that it can format the data during the indexing.
Now, the difference is that the source is the name of the file, which is the originating file or stream,
while the source type determines how Splunk software processes the incoming data and then categorize
it.
So this is pretty much the originating path or the file being monitored, while the source type is the
point of reference that is going to help Splunk to categorize this type of data into the index.
And you can, of course, manipulate this data during the indexing to mask some data or to manipulate
the data, doing some extraction.
And how you will do that, you will need a reference which is the source type.
So and the prob stock of when you want to do apply some settings to manipulate this data are doing some
field extraction, then you will need to reference the source type.
Of course you can do that also in the source, but the source type is always a good reference.
The index is where this data is destined for it.
So as you ingest or as you monitor this data and it's coming into the universal forwarder or you're
just monitoring the data or simply you're sending this data from a firewall to the universal forwarder.
Of course, you need to tell the universal forwarder where is going to be destined for so what index?
So it's an index is very important.
And lastly, the timestamp.
So you need to assign a timestamp to the data being ingested.
So now that we've covered this part, let's move on to the next section.
