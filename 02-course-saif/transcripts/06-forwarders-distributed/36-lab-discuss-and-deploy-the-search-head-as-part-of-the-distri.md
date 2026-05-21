---
course: saif-admin
theme: 06-forwarders-distributed
lecture: 36
lecture-title: "LAB: Discuss and deploy the Search Head as part of the distributed Architecture"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/06-forwarders-distributed, transcript, kind/video]
---

# Lecture 36 — LAB: Discuss and deploy the Search Head as part of the distributed Architecture

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

In the previous section, I've shown you how to deploy the universal folder on my Windows Machine laptop.
And then we have downloaded the windows, add on and deployed it to this universal folder to monitor
certain log files from generated from my Windows machine.
And we have shown you that by activating some stanzas of interest and the inputs dot com of that app
and then forward the logs to the indexer.
We have also added the index equal windows on these activated stanzas.
And also we have created the index equal to windows on our indexer.
So in this last part, we will be talking now about the search head.
So before we start with the search head, let me jump ahead and go to the next slide.
So let me delete that.
So distribute a search.
We already talked that the search had dispatches the queries to the indexer, as I've shown you before.
Now, if we want a search head to be part of an indexer.
What we need to do is we need to add the indexer.
A.K.A search peers.
To the search had by going to settings distributed search search peers.
And then we need to add this indexer.
Which is.
Let me show you.
This one.
To the search head.
So let me just delete that and come back to the next slide.
So the disk search icon is the file where these changes are going to happen by adding the new search
peer, which is the indexer, and they are living under ETSI System local.
This is a slash sorry.
And then opt splunk.
ETSI sys local, which is the same pretty much.
And this is the configuration that you would expect.
Now the search distributes what is called the knowledge bundles to the search peers which contain knowledge
objects, and they are located under the var run or the search head and under var run search peers under
the search peer, which is the indexer knowledge objects are shared in a clustered environment.
So when you have a cluster environment of search heads, then knowledge objects will be replicated across
all the search heads which are part of that cluster, whereas dedicated search heads in this case they
don't.
In a distributed architecture where the search period is having performance issue, the search period
can be put into quarantine mode.
So if you have multiple indexes, search peers and let's suppose this is the search head and one of
those is having performance issue, you can just pretty much put this indexer into a quarantine.
So it's not going to participate into the different searches returned back to the search head from the
indexers.
So why multiple search heads mainly for access control and performance.
So to increase the performance of these searches, fast retrieval and of course to let a specific user
within a search head to access specific indexes and so on and so forth.
So.
Let's go back to our demo and actually add our search head.
So I have provisioned this search head.
Which is.
This one.
I'm going to log in and then we're going to add this indexer to the search head as part of the search
distributed search architecture.
So let's log in.
What I will do.
I will go to settings.
Under distributed search.
And I'm going to go to search, Piers.
And I'm going to add a new search peer, which is the indexer.
Normally you need to do it this way.
Please include the other IP address of that indexer, which is ours in this case.
And then on Port 8089, which is the management port.
Splunk username and the password for that indexer.
Save it.
And now we have added that successfully.
So let me just.
Replication status is still initial.
Let me just do a refresh in here.
It's going to take a few seconds.
Then it's going to have this going to change, of course, as I've shown you.
If, by any chance this indexer in a distributed environment where you have multiple indexers, it's
performing badly, you can put it in quarantine.
So whenever are you going to go ahead and search from this search head?
This one is not going to participate and return back the results.
So all the other indexes in the part of that distributed architecture is going to respond, but this
one is going to be in quarantine mode.
So let me just do a refresh one more time.
Successful.
So let me show you that in clay.
So I'm actually saying to the search head.
Let's zoom in.
And log in.
So let's clear.
So we would go to opt Splunk at C.
System Local.
And then take a look at here.
Distribute a search.
So let's do pseudo nano.
Just search.
And as you can see, this is the configuration that we've just done.
So now.
The exit from here.
And go back to our search head.
So let's go to the searching are reporting.
And.
Do a query.
To our Windows server.
Within the last maybe 15 minutes.
60 Minutes.
And there you go.
So you can see.
The host, the source, the source type.
By the way, how do you know?
How can you tell if this is pretty much coming from the indexer?
So you need to find.
So let me do a control F server.
And this is the Splunk server.
And you can see this is actually the indexer.
So I've named my Indexer as Linux demo and we can confirm that.
So to confirm that, I'm going to the Indexer.
I'm going to die.
To system local.
And inputs.
And as you can see by default, this is a global default configuration.
My host name is Linux Dash Demo.
So now we have successfully.
Configure the universal folder on the Linux machine as well as on a Windows machine deployed a Windows
add on and then instructed it to monitor the desired log generated on my Windows machine to send it
forward to the indexer, as well as monitoring the secure log and the secure one.
Log and forward those logs to the indexer.
And then I have created this indexer with listening on to nine seven ports and created the security
index first and then the Windows index as a second phase.
And then finally, I have deployed the search head and then add it to this indexer aka search prior
to this search head.
So within all under the concept of distributed architecture design.
