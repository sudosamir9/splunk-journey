---
course: saif-admin
theme: 07-data-flow-concepts
lecture: 40
lecture-title: "Data consolidation and Load balancing topology (introduction to Event breaking)"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/07-data-flow-concepts, transcript, kind/video]
---

# Lecture 40 — Data consolidation and Load balancing topology (introduction to Event breaking)

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So let's discuss more in depth about the different controls that would govern how to forward the logs
from the universal folders to the next tier.
Mainly I'll be working on applying and configuring these controls under the inputs dot com and the outputs
dot com.
And I'll be discussing as well the different topologies, the architectures that could serve different
scenarios on how to forward steer the traffic to the next tier.
So let's go ahead and jump to the next slide and discuss this.
So I'll be discussing the data collection deployment topology by editing the inputs dot com outputs,
dot com and the props dot com.
Now I will leave the props dot com for a later discussion throughout this course, but I will be focusing
mainly on the outputs dot com and in the input stock of of course we will be discussing all of these
as well and mainly about when we can be using the heavy folder and the different use cases.
So let's jump ahead to our first topology, which is this one.
Let me just zoom in and discuss this.
So mainly and this is pretty much very straightforward.
So we will be this topology.
I have different universal folders deployed to end machines, whether they are Linux machines, Windows
machines, and I'm going to be instructing those universal folders to forward the logs directly to a
Splunk standalone instance.
So mainly I will be working in here.
On the outputs and on the input.
So, for instance, I would like to maybe instruct these universal folders to monitor certain files.
So I'll be applying the monitor stanza and I will be monitoring whatever we have under the VAR log directory.
So basically monitor all the logs inside this directory, assign it to the index Linux and a source
type of Linux and this is activated, then instructing these universal forwarders to through the outputs
of configuration.
And this is the server IP of this standalone Splunk instance.
And a compress, a compression, the control of false.
So I don't want to compress basically the logs that I'm going to be forwarding from these universal
forwarders.
So let's just go further up.
And of course, this is with regard to the universal forwarders.
Now, in the indexer, of course, I will need also to set and configure the inputs to listen on a specific
port, which is 9997.
And I'm going to configure that under the stanza Splunk TCP.
So the Splunk TCP stanza means the expected forwarded logs are have to be from forwarders.
If it was a TCP colon forward slash forward slash triple 97, That means that the logs which I'm going
to be receiving could be basically any other instance other than Universal folder.
So let's actually show you that.
So let's go to the inputs and I'm going to control F, So control F, RT, Splunk, TCP Colon.
Now this is.
The same as the TCP stanza, except that the remote server is assumed to be a Splunk instance and most
likely a universal forwarder.
So when we configure this, that means that the expected remote hosts sending those logs are is going
to be a forwarder.
While.
TCP IP.
This one.
Would be.
Let's take a look.
So this one, the following configurations are a support for our data.
And the data could come from any remote server other than a Splunk instance.
So let's go back to our configuration in here.
And of course, you need to make sure that you have configured the index, which is Linux, because
obviously, whatever you're going to be monitoring here and forwarding it through the output dot from
this universal folder, the target index would be a Linux.
So you need to make sure that under this indexer.
For instance, you have also configured the Linux index.
So this is pretty much the first topology, the data collection methodology.
So pretty much straightforward.
Configure the inputs to monitor the logs and of course the output Stockholm to forward those logs to
the next tier, which is the index indexer.
In here.
Of course, on the indexer you need to make sure that you need to set up this indexer to listen on a
specific port for the incoming traffic from here to this way.
So this is the first typology on how we can collect the data.
Let's move on to the next one.
And this one.
We have a bunch of universal folders in here.
But.
We are instructing these universal forwarders to actually send the data load, balance the data to two
different indexers.
So the forwarder in here and the forwarder in here and this one as well is sending those whatever we're
going to be monitoring.
Under the Volokh.
Sending those logs.
In a kind of a round robin fashion.
So sending the blogs here and then send this logs in here and we have a couple of controls that we need
to take a look at closely.
And these are the auto LWB frequency and the auto LWB volume.
Of course, these ones, we will we will take a look at those closely.
But.
Take a look at this control here or this parameter.
So server under the server were actually configuring the host and the port, the host and the destination
port.
So we're instructing this universal forwarder to forward the logs to both ends.
So the index r one and then the x indexer to.
So let's now talk about the auto LWB frequency and auto LWB volume.
So the Outer LWB frequency, if it's not set by default, the universal forwarder will alternate the
logs.
So monitored every 30 seconds.
So first, it's going to send the logs to the indexer one, and then after 30 seconds, it's going to
switch and send the logs to the second indexer and then it's going to alternate to the first one and
then it's going to alternate between both.
Now we can overwrite that settings by applying, for example, this control auto LWB frequency equal
to 40.
So that means we're going to alternate.
We're going to switch from the first indexer to the second Indexer after 40 seconds.
Similarly speaking, the auto LWB volume.
It's at 10,000 bytes or kilobytes.
I think actually we can take a look at this and the output scoff.
So let's go ahead and check out all LP frequency.
The amount of time in seconds.
That's exactly what I've discussed.
And send the data to an indexer before redirecting the outputs to another indexer.
So that's an alternate while out to LP.
Volume.
This is the volume of data in bytes.
Yeah, exactly.
To send to another indexer before and you Indexer is randomly selected from the list of indexers.
So let's go back to our diagram.
What that means is that this universal folder is going to forward the first.
10,000 bytes.
Then once this has been reached, switch and send the next to this indexer.
Once the threshold has been reached, then alternate and switch back to the first index.
So the forwarder your controlling the follower in a way using this control to alternate the logs between
the index one and index two.
So these are the two controls that you need to take care of when you want to forward the logs and load
balance it between those two indexers.
Automatic load balancing is very important because it's going to distribute the events across these
indexer and why it is important because in a distributed environment we tend to distribute the processing
and of course distribute the workload across different indexers as well as parallel processing.
Now.
Let me emphasize one important thing.
Switch happens.
Only when the forwarder detects an end of file.
So as this universal forwarder is reading the logs from this, monitoring those logs and it's going
to alternate in here between index or one index or two.
This one.
The universal photo is not going to alternate the logs.
Or the switch is not going to happen unless there is an end of file has been reached or there is an.
Decrease activity in input output.
So then the switch is going to happen.
So this is very important.
But even if we have set of controls to load balance, the traffic between index or one index or two,
this could break and this could break potentially when we have set the universal forwarder to monitor
a big large file or a continuous data stream is coming to this universal forwarder.
And then that means that this universal folder is going to get stuck on one indexer and it's not going
to switch.
So how to fix this issue.
So to fix this issue, we need to introduce what we call the event breaker.
Now we need to instruct this universal forwarder.
To make it aware of the event boundaries of the data being sent to the indexing tier, and only then
the switch is going to happen.
So that's going to help make the load balancing go smooth.
So how we can do that?
We do that by enabling the event breaker, enable equal to true under the scope and it's going to these
controls needs to be set.
For our source type of interest, which is the source type of the data being sent to the indexing tier.
And of course, we need to let the universal forwarder through the event breaker, controlling here
and using a proper regex so we can let it know where to break the events properly.
This is pretty much very, very important when it comes to multi-line events.
So let me show you an example.
So.
Take a look at this data.
So this is data from Windows.
And as you can see, it's a multi line events.
So switching or load balancing is not going to happen unless we instruct the universal forwarder to
know the event boundaries of this data.
So this is October 21st and as we go through the data, actually it ends in here.
So we need to find a regex to actually set it and break it.
So let's, let's do that.
So let's start with a new line.
Now, as we see in here, what I can do, I can put.
A backslash w for characters.
And I'm going to do, for instance, a plus.
So the plus means between one and unlimited times and then there's a space in here.
So what I'm going to do backslash space.
So it's an S and then backslash DX backslash D, So as we go through the data now, we can use this
regex.
Actually, and that control.
So we can instruct that universal forwarder to actually brake at the end of the event.
And this going to help with the switch and facilitate it during the load balancing.
And as you can see in here, it all is going to break up to this point.
So we can take this back the rejects and go back to our.
Props.
And then I'm going to just going to paste it in here.
And then we take this for that specific sauce type.
And then we have to configure it in the prep stock.
And inside this universal food order.
Now there is another control, which is very much important.
And let me just type that which is the max.
Q size equal, maybe we can put it to ten.
NB So what does that mean?
This is, you know, this control.
So let's suppose.
This universal folder cannot reach this indexer and cannot reach this indexer for whatever reason.
Maybe they are down or there is a congestion on the network, etc..
So this is this is the maximum amount of data that the forwarder.
Could buffer into the output queue.
Before it's going to send it to the indexes.
This is typically happening whenever they're in scenarios where the universal forwarder cannot reach
any indexer or there is again, an issue with the network congestion in the network.
And this could help not to lose the data.
And as soon as the indexes are reachable again from the forwarder, then buffer whatever data I have
in the outputs dot com and then send it to the indexing tier.
Now, there is one important thing to to note here.
The in a distributed environment where you have the universal folder configured to forward the data
to different indexers this max queue size.
So for instance, the if let's suppose this universal folder is on this indexer and for whatever reason
this indexer is not reachable anymore.
This one is not going to happen or we're not going to buffer that data because the forwarder will switch
to Indexer two and it's going to switch maybe to index or three.
And if all of those are not reachable, then and only then the universal forwarder will stop forwarding
the data and it's going to buffer it up to the amount that we configured it, which is ten and B, and
then as soon as any indexer is up or reachable, then forward whatever we have buffered into the output
queue back to the indexing tier.
