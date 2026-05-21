---
course: saif-admin
theme: 01-fundamentals
lecture: 2
lecture-title: "What does Splunk do?"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/01-fundamentals, transcript, kind/video]
---

# Lecture 2 — What does Splunk do?

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So as I mentioned in the previous slide, Splunk is a distributed system that would ingest process and
index log data.
Now, Splunk will process the data in three stages.
Now let's first talk about the data input.
So Splunk will ingest the raw data taken from any device that you can think of is going to break it
into 60 4k blocks of chunk and is going to add some metadata keys to it like source, source type and
host.
Now, we will be talking about those three in subsequent slides, but for now, take it as it is.
Now, I'm going to be combining the data indexing and data parsing in one process, and that is the
data parsing and storage.
So Splunk will parse the lock data by breaking it into lines.
And then it's going to identify timestamps, creating individual events and annotating them with metadata
keys.
So what I mean by that?
Well, let me show you.
Exactly.
So let's go to Splunk.
So pretty much searching the internal index, which is pretty much showing the internal processes of
Splunk.
Now, if we take a look at this log example in here, by the way, I'm viewing it in raw mode.
So it's pretty much ingesting it as it is now, as you can notice.
This part where it's showing the timestamp.
Now, if I'm just going to break this down, and as you can see here, it's being assigned to the underscore
time field.
So this is pretty much the key that this is still the value and this is the key.
So that's the key value pair.
So Splunk is going to ingest this raw data and is going to be assigning key value pairs to this.
So it's going to be so easy for you to search those events and get the desired results.
So let's go back to the third process, which is the search.
And now the search process will provide the UI to the users so they can use it to interact with Splunk.
So it will allow users to search and query Splunk data interfaces with the indexes to gain access to
the specific data that they have requested.
This is exactly a moment ago, which I've pretty much shown you.
Now, what I'm giving here for the sake of of this architecture presented here, Splunk is acting as
a standalone instance where it's actually performing all the rows together.
And I mean by that the data input which a.k.a Splunk, forwarder data indexing and parsing.
This is the Splunk Indexer and the searching, which is going to be the search head.
Now let's go to the next slide and then I will be showing you exactly what I mean.
So Splunk components now.
Splunk, comprised of three main components, what I would call them the processing components, which
can be handling the data, which is the forwarder, the indexer and the search head.
For the sake of the previous slide, which I've shown you, Splunk as a standalone, again, is acting
as the whole instance where it's performing all of these roles together.
Now, as a second component is the management components.
So these support the activities of the processing components above.
So I would call them these kind of the auxiliary components so they could help manage the inner workings
of Splunk as well as the processing components, which are the deployment server, the license server,
the master cluster, no deployer and monitoring console.
Of course, we will be talking individually about every single one in subsequent slides.
