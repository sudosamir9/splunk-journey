---
course: saif-admin
theme: 07-data-flow-concepts
lecture: 41
lecture-title: "Discuss forwarding the data based on Routing and filtering"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/07-data-flow-concepts, transcript, kind/video]
---

# Lecture 41 — Discuss forwarding the data based on Routing and filtering

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

Another use case in here is to selectively forward logs to different indexers based on the monitored
files.
So let me show you that.
So we have index of one index or two and we have one universal forwarder.
So what we can do is.
We can selectively.
Whatever we get to monitor for the block, secure only destine this data.
To Indexer one.
Similarly, whatever logs which are under the log messages only send it to indexer to.
And we use what we call the underscore TCP underscore routing control.
So through this control.
We can selectively set or forward the data to the desired indexer.
He is to be configured in the input scope and then we need to reference that.
In here.
So as you as you see TCP out index R one, what does that mean?
Is that.
This is Indexer one.
This is the output group, which is Indexer one.
And this is the output group, Indexer one.
So whatever I'm going to monitor under the log secure, send it only to the output group index or one
whatever I'm monitoring under the log messages.
Send it to the output group indexer to so I'm selectively routing different files to two different indexes.
