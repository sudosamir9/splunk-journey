---
course: saif-admin
theme: 09-data-inputs
lecture: 51
lecture-title: "LAB: Configure the Firewall to forward the logs to the UF ( Network Input )"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/09-data-inputs, transcript, kind/video]
---

# Lecture 51 — LAB: Configure the Firewall to forward the logs to the UF ( Network Input )

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

Now that we were done with the monitoring input, which is this part?
I will go ahead and configure a firewall.
To forward the logs to the universal forwarder.
So first there are a few steps that we need to take care of.
I will need first to create an index in here.
Now, for the sake of this lab, I'm going to be configuring a FortiGate firewall.
And send those logs to the universal forwarder.
But first, I need to create the FortiGate index under the indexer and then under the universal forwarder.
Of course, I will need to configure it to listen for incoming traffic or a specific port.
And then lastly, I will create or I will instruct the firewall, which is the FortiGate firewall,
to send those logs on that specific port which the universal forwarder is listening on.
So first things first, let's go ahead and configure that.
So first, let me just delete this.
Let's go to Splunk and let's go to Indexes.
I think I have already created the FortiGate.
So it's here.
What I'm going to do, I'm just going to delete it.
I'm just going to recreate it one more time.
So let's go ahead.
I'm going to put F get FortiGate firewall.
Keep everything as it is.
I'm going to save it.
The FortiGate index is there and ready.
So now we are on the universal forwarder.
What I'm going to do, I'm just going to delete everything.
I'm just going to control X, Save it.
Now I would like to send or to make this universal folder.
To listen on a specific port.
So let's say five, five, five, five, five.
So let's go ahead and configure this universal forwarder to listen on that port.
So what I'm going to do actually, before I'm going to do that, I'm going to check if this universal
forwarder is listening on any port.
So I'm going to do 555.
So for now, I don't have any.
The porch four times five.
The rest of is not listening.
So what I'm going to do, I'm going to go back to the input of.
And I'm just going to copy this configuration.
So basically what I'm doing is.
Using protocol UDP.
I'm instructing the rehearsal forwarder to listen for incoming traffic on this port.
And whatever.
Traffic is going to be picked up from this on this port.
I want to reference it with the index equal to eight.
I want to sign it with a sauce type Feet under the sauce.
FortiGate.
Now connection underscore host.
Now you have different options.
You can do DNS so the Splunk will do a reverse lookup for that IP.
If it's an IP to to actually get the domain name or I will just keep it to IP.
Q sighs more to come about this and then disabled equal to zero.
So I'm just going to do and save that.
And I'm going to restart the universal folder.
So let's do.
So, zoo Splunk.
Seed opt.
Spunk for order.
Then Splunk restart.
So let's start Splunk for a moment.
Okay, so let's run.
That's.
S minus a, and I'm going to grep for that port.
Let's see if it's up.
And in fact, as you see here.
By doing the configuration under the input score of.
Now my machine where the universal folder is deployed to.
I've instructed it to listen on port four, five, five, five, five for incoming traffic.
So let's go back to this.
So what I've done.
I have configured the index of FTT here.
On this universal order.
I have configured it to listen on chip on five, four times five.
So five, five, five, five.
On using UDP protocol.
Of course it's already this universal forwarders already configure with the output scope to to forward
the traffic to the index.
Then Dexter now comes the and we have verified that the port is up and running by checking here.
This one.
Make sure in real world scenario you don't have any firewalls in between, you know, just to make sure
that the traffic is sent.
And then I'm going to go to the last part where I'm going to configure that FortiGate firewall to forward
the locks on that port, which is four times five UDP protocol.
So let's jump ahead and do that together.
So let's jump to the firewall.
I have a FortiGate firewall in here.
And I want to configure this FortiGate firewall to send the traffic to the universal forwarder on port
five five, five five using the UDP protocol.
So let's go to login report.
Lock settings.
And in here.
So remote logging and archiving.
I don't I'm not using any photo analyzer or 40 manager.
I want to send those logs to a syslog server and the syslog server in here in our case is the universal
forwarder.
This one.
So let's go back to our 40 guy.
And there you go.
I'm going to enable that.
So.
I want to send the logs to.
190 or actually 60?
I'm not sure.
Let me just check.
IP address.
So.
So my IP is ten, ten, 1060.
Yeah.
So let's go back.
This is the universal forwarder, by the way.
So let's go back.
This is 60.
Events, logging, local traffic.
Everything is set.
Let's apply.
So settings are done.
So we have configured the firewall.
Let's go ahead and see if we're actually capturing any traffic sent from that firewall.
So what we can do is we can use TCP dump minus I.
Any.
So this is the flag for any interface and I'm going to do, for instance, minus.
So before minus I any minus and and I'm going to do minus double V.
Then I'm going to specify.
Purports to be five, five, five.
We need to do that with pseudo.
So I'm listening now.
So let me just log in at the minute.
Let's see if you are receiving anything.
In fact, we are receiving.
So if you can see here, I'm sending from my firewall, which is this one.
FortiGate.
From this source port to my universal folder on this destination port.
So I'm receiving.
So basically, if we go back to our.
I'm sending it from this firewall to this.
Now, we've already configured the inputs, you know, to listen on five, five, five, five.
And then the universal forwarder here is acting as a syslog server is going to forward the logs to the
indexer and we can see that into action.
So let's go back to the search.
Index equal to f.
G.
T.
Let's search for the last 24 hours or actually the last 15 minutes.
And here we go.
So.
Host It's exactly this one.
But take a look.
The host in here.
Is the firewall, which is this IP.
Index is that we've configured this is the source which is the FortiGate and the source type, which
is FTT.
So this is pretty much how you configure and forward the traffic from a firewall to the to the universal
for the listening on a specific port.
So now that we have configured this firewall, the FortiGate firewall, to send the traffic syslog messages
to the universal forwarder and the universal forwarder through the port, five, five, five, five.
And then it's going to relay whatever being received from here to the indexing tier.
But let's talk about.
This configuration that I've done earlier, which is the queue size.
So what?
How can this help us?
In Splunk, we have what we call flow control.
So these queue settings in here provide kind of a flow control across the entire input stream.
So imagine this firewall is sending too much traffic bursts of traffic to the universal forwarder.
Now, remember, this data in here is in transit.
If it's not going to be processed by the universal forwarder, it's going to be lost.
Now, for whatever reason, maybe the resources, the hardware aspects of this universal forwarder is
not up to the data which is being received from this firewall.
So some of the data will be dropped.
So what you can do is you can configure this universal forwarder through the inputs dot com with the
queue size to actually buffer this data into kind of a queue.
And this is the queue size I've configured to ten mb b.
Now as soon as the universal forwarder is able to process everything.
Then is going to relay the traffic to the indexing tier.
Another scenario, let's suppose the indexer is not there.
It's not reachable by this universal folder for whatever reason, a congestion on this network or just
down whatever.
It could be many reasons.
Now the universal folder is going to see that this indexer is not reachable.
So what is going to do?
So the the universal folder in here is going to buffer this data again into what we call the memory
queue.
Now, if the memory queue is full, then we can fall back to what we call the persistent queue.
Now the persistent queue is going to write the data which is in transit, which is not being able to
process it from the universal folder is going to write it into disk under the var run Splunk directory.
As soon as this indexer is reachable or there is no more congestion into the network in here or here,
then the universal folder will start processes data and it's going to forward it to the indexing tier.
Now let me show you that.
So let me just bring the configuration in here.
So the queue size is the maximum size of the memory input queue.
Default is 500 KB.
Of course you can configure it with KB and B and gigabyte.
Persistent queue is the maximum size of the persistent queue file.
Persistent queues can help prevent loss of transit data.
Now.
This is what we call the input on the input size in here.
Now, this should not be confused what what we call the max queue size.
So this is also the same concept, but this is applied at the output Q.
So the output cue is in here.
So.
Let me bring that one second.
So if the indexer cannot keep up with the data, this is going to be useful on both sides, whether
it's an issue in here or an issue in here where the universal forwarder can not keep up with the burst
of data which is being received at this end.
