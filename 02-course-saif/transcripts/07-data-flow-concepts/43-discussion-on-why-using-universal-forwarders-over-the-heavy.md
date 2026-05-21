---
course: saif-admin
theme: 07-data-flow-concepts
lecture: 43
lecture-title: "Discussion on Why using Universal Forwarders over the Heavy Forwarders?"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/07-data-flow-concepts, transcript, kind/video]
---

# Lecture 43 — Discussion on Why using Universal Forwarders over the Heavy Forwarders?

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

In this section, we will be discussing the preference to use universal folders over a heavy folder,
acting as an intermediate folder in a multi stage data routing design.
So let's assume that we have this environment.
So typically we will have universal folders deployed to the end machines and then we will instruct those
to forward the logs to the intermediate folder and then the intimate folder will forward the logs to
the indexing tier.
Now we would recommend normally to use and deploy the intermediate folder here as a universal folder.
The reason why, because the universal folder has lower resource impact scales better and has less overhead
on the wire over the the heavy folder.
If you deploy a heavy folder in here, of course it's going to require a license and it's going to send
the data as cooked, parsed.
And this is going to introduce much more overhead on the wire or on the network while using or deploying
the universal folder here as an intermediate folder is going to introduce, you're going to be using
less resources.
And I'm talking about how it expects scales better.
And you're going to be forwarding the logs as uncooked and parsed.
Of course, there are scenarios where you would also want to deploy the intermediate forwarder from
a heavy forwarder, and that is normally when you want to introduce, for example, advanced routing
capabilities.
And of course, if you want, for example, you have a use case where you are sending some sensitive
data from these universal folders and you don't want to have that data exposed on the indexer.
So what you can do, you can actually use a heavy forwarder as well to manipulate the data, mask,
some sensitive data, like, for example, credit cards, information prior to writing that to disk
on the indexer.
Or if you want to activate the heck the A.P. event collector, then you will need definitely a heavy
forwarder or DB connect.
So these are pretty much the use cases that you would need when you need to use the heavy forwarder
over the universal forwarder.
But in the end, it all comes down to the architecture, design and serving the purpose of how you would
like to collect the data versus how much hardware, specs or resources you have to allocate to these
universal folders or these instances versus how much going to be able to scale your design at a later
stage.
