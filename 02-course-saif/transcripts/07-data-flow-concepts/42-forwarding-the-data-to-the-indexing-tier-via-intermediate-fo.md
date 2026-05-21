---
course: saif-admin
theme: 07-data-flow-concepts
lecture: 42
lecture-title: "Forwarding the data  to the Indexing tier via Intermediate Forwarders"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/07-data-flow-concepts, transcript, kind/video]
---

# Lecture 42 — Forwarding the data  to the Indexing tier via Intermediate Forwarders

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So in this diagram, we have a bunch of universal folders in here.
Load balancing the logs to intermediate folders.
These intermediate folders are nothing but universal folders.
And of course these intermediate folders are forwarding the logs to the indexer.
This is typically recommended by best practices to have this way as set up.
Now suppose we have another indexer in here.
So index to index or one.
Similarly speaking, these intermediate folders could also load balance the data to the index sink tier.
Now, this is very much important when it comes to distributing the events across different indexers,
of course, as well, distributing or load balancing the data from the forwarders to the intermediate
forwarders for better data distribution and workload.
Now, if one of those intermediate forwarders goes down, this is not going to introduce a single point
of failure as we have another intermediate forwarders where this universal forwarder could get stuck
on this one and then forward the data to the indexing tier.
Let's discuss something which is the index acknowledgement.
Now by default the indexer acknowledgement is set to false unless you enable it and what it does.
Let's assume that the data is being sent to the indexer.
Now for whatever reason, there is a congestion into the network.
So there is no way to tell that the forwarder that the indexer is receiving the data from the forwarder.
So in this way, what we can do, we can enable this use knowledge to true under the output conf.
And what this is going to do is basically if the data get lost along the path, that means that the
indexer is not going to send any acknowledgement to the forwarder, which implies that the universal
folder needs to send the data back again to the indexer.
So this is important because it's going to protect against any loss of data as it goes or gets forwarded
from the universal folder to the indexing tier.
This also could be set up at the intermediate forwarder.
So whatever the data is going to be sent in here, the intermediate forwarder is going to send an acknowledgement
back that the data has been received.
And similarly speaking also from the automated forwarder to the indexer as well.
So this creates kind of a better way for data resilience.
