---
course: saif-admin
theme: 10-capstone-lab
lecture: 61
lecture-title: "LAB: Deploy the heavy forwarder via the DS and forward Fortigate Firewall Logs"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/10-capstone-lab, transcript, kind/video]
---

# Lecture 61 — LAB: Deploy the heavy forwarder via the DS and forward Fortigate Firewall Logs

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So in this section, I will go ahead and configure the heavy forwarder.
Now, first things first, what we need to do, we need first to actually deploy the deployment client
on this heavy forwarder so it can phone home back to the deployment server and we can use the deployment
server as a centralized tool to deploy whatever apps and add ons back to the heavy forwarder.
So let's log in to this heavy forwarder.
Bye, Sage.
And let's do that.
So, KD.
Opt splunk at C apps.
And now and here we need to copy the this app here so it can talk back or phone home back to the deployment
server I can use when ACP to copy this file.
So let's go ahead and log in via winzip to the heavy forwarder.
So to do that, what I'm going to do just going to open and use session basically, and I'm just going
to go to my heavy forwarder and take the public IP address.
So let's go back in here.
So paste it.
And I'm going to provide the username and password.
So now I'm on the heavy forwarder.
So let's go to the temp directory in here.
And let's copy.
And let's copy the deployment client app.
So let's face it in here.
So now it's here.
So let's go back to the CLI and let's see D to temp.
And I have it in here.
So let's do pseudo copy minus our demo to opt Splunk at C apps.
Let's switch to the apps directory.
So opt to Splunk at C apps.
Now let's check that app, which is this one.
Now what I'm going to do.
Just going to cede to the demo.
Then local.
Then I will do a sudo nano deployment clients dot com.
I need to change.
Of course the ip address in here to reflect the correct IP address of my deployment server.
So let's go to the deployment server and copy the private IP address.
So let's go back in here, paste it, control X, save the settings.
So now let's go ahead and change the ownership of the file to Splunk.
Splunk.
So opt Splunk at C apps.
Now let's trigger a restart.
So pseudo minus you Splunk.
Then.
So then Splunk.
Restart.
So let's wait for this to finish.
So now, once we are done restarting our heavy forwarder, then we should go back to our deployment
server in here.
So we're going to be able to actually see it.
So let's log in to our deployment server.
Let's go back to the Florida management.
Let's go to clients.
Let's wait for a minute.
So now we're actually able to see also the heavy forwarder.
But of course, under the heavy forwarder, we don't have any apps deployed to it.
So what we need to do let's go back to our diagram in here.
I will need to deploy the FortiGate to.
So it's going to help us to to parse the logs which are incoming from this FortiGate firewall to here.
Also, what we need to do and we need to create another app on this heavy forwarder so we can instruct
it to listen on port five, five, five, five or 514.
We will see.
In addition to that, we need to create another app so the heavy forwarder can forward the logs to index
or two.
So let's do that together.
But all of this will be done solely from the deployment server.
So let's do that.
Now let's log in to our deployment server via SSH.
So let me just copy the public IP address of the deployment server.
Let's go back to our heavy forwarder.
Let's exit.
That's based the IP address.
And let's log in to our deployment server.
So let's go to opt Splunk at C deployment apps.
Now in here.
I will need to copy the same app, which is.
This one to instruct the heavy forwarder to listen on port five, five, five, five.
However, this app is configured to listen on Port 9997.
What I'm going to do, I'm going to duplicate this app and then make the changes.
So let's do copy minus our demo lab.
Inputs.
Bass and I'm going to rename it to demo, underscore, lab underscore, inputs underscore.
Heavy forwarder underscore FortiGate.
So let's do that.
I forgot to include the sudo sudo.
Now let's go to our demo lab inputs.
Then heavy forwarder.
Now let's do sudo nano local then inputs dot com.
Now let's change that port to 555 as well as instead of splunk TCP.
I'm just going to put UDP.
And also we need to include the index, which is going to be the destination for all this traffic on
Fortinet.
So Fortinet index because if you remember we've already created the Fortinet index on our index or two.
So we need to make sure that this has to be tagged into the inputs dot com inside the heavy forwarder.
So index equal to Fortinet.
Now let's save that.
And now.
Let's do sudo chan minus our splunk splunk opt splunk at C deployment apps.
So now.
Let's go to deployment apps.
I have just created now the inputs to prepare this heavy forwarder to listen on port.
Five, five, five, five, five.
So now let's duplicate another app.
Which is the demo lab underscore i f underscore outputs underscore base which is instructing basically.
Those intermediate folders to forward the logs to the index are one.
However, we're just going to make some changes so that instead of going to index one, it's going to
go to index or two, but we will deploy it to the heavy folder.
So let's do that together.
So let's go back to our CLI.
Let's do sudo copy minus r.
Demo lab i f output base.
And I'm going to rename it to demo underscore lab underscore heavy.
Forwarder.
Underscore outputs.
So let's go to that app.
So Seed demo lab.
Heavy forwarder and I'm going to do a pseudo nano.
Local then outputs.
And now I'm going to change it to index or to.
And I'm going to put the IP address of the indexer, too.
So what I'm doing here, I'm just going to reuse the same app that I have deployed for the intermediate
folders and just change some configuration so I can deploy it to the heavy forwarder.
So let's go back to our instances and let's go to Indexer two.
I'm just going to copy the internal IP address of the Indexer two.
I'm going to paste it in here.
I'm going to save it.
Just going to move some directories above.
So sudo chon minus r.
Splunk splunk then opt splunk.
It's c deployment apps.
So let's go to the deployment apps.
So now I have prepared the outputs.
So the heavy forwarder outputs where I'm going to instruct basically this heavy forwarder to forward
the logs to index or to I'm going to deploy as well.
The.
Demo lab inputs, heavy forwarder FortiGate, where I'm going to instruct this heavy forwarder to listen
on port five, five, five, five, as well as I'm going to deploy the four decade to that we have done
earlier throughout this lab.
So let's do that together.
So what I'm going to do, I'm going to go to the folder management now, I'm going to create a new server
class and I'm going to call it heavy.
For order.
Base.
I'm going to save it.
And I'm going to add all three apps together.
So that would be the slunk to because we will need that there as well as the.
As well as the demo lab inputs, heavy forwarder, where I'm going to activate the heavy forwarder to
listen on port five, five, five, five for incoming traffic from the FortiGate firewall, as well
as I'm going to instruct the heavy forwarder to forward the logs to index too, which is this one.
So I'm going to save it.
And I'm going to add the client, which is the heavy forwarder where I intend to deploy these apps to.
So let's copy, for example, this one.
Let's face it in here and put a wild card.
Let's preview that.
So I already have a check mark, so let's save it.
So now let's do an edit on.
Maybe this one should be OC.
I'm going to trigger a restart of the Splunk daemon on the heavy forwarder.
So now that we have deployed all those three apps to the heavy forwarder.
That means we can verify this by going to the CLI of the heavy forwarder.
So let's go to our heavy forwarder.
So exit.
And let's copy the IP address of our heavy forwarder so we can ssh to it.
So this is the IP address 100.
So this is the one slog in.
So CD opt splunk at C apps.
So let's do la la.
And now, as you can see, we have all those three apps that we've just deployed from the deployment
server, and they have landed under Splunk at C Apps.
So now that we have configured our heavy folder in here.
So let's go ahead and actually configure the FortiGate firewall to forward the logs to the heavy forwarder.
But before we do that, we need to make sure that the port five, five, five, five is opened on the
inbound.
So for whatever logs they're going to be sending from the FortiGate, we need to make sure that that
port is opened.
Now, to do that, let's go to our instance under our heavy forwarder.
And let's check if we have a security rule in place.
Now, in here, I don't see any security rules.
So what we need to do, we need to go ahead under security groups and create a new security group for
this.
So I'm going to call it 40 gate, 40 gate, incoming traffic.
I'm just going to copy this and just going to baste it in here.
I'm going to add a rule on the inbound.
So TCP IP 555.
I could also actually include TCP and UDP just in case, but let's include the TCP and then from everywhere.
And then I'm going to add another rule for actually.
For you.
DB.
So let's also include the five, five, five.
So now let's just add anywhere.
So now let's create the security group.
Now let's go back to our EC.
Two instances.
And now let's go to our heavy folder in here and add that security group.
So under Security Change Security group.
And I'm going to add that group, which is the 48 incoming traffic.
So let's add that.
Let's save it.
So now let's go ahead to our FortiGate firewall and configure it to forward the logs to our heavy forwarder.
So let's log in.
So config.
Log sis log settings.
Now let's do set.
Fort.
Five, five, five, five set mode.
UDP.
So let's do a show.
Now we need to set the port.
Five, five, five, five.
Let's do a show again and we can see that it's enabled and this is the destination IP address of our
heavy forwarder.
So let's do an end.
So now let's go back to our diagram and discuss this.
So I have already configured the FortiGate firewall to forward the logs to the heavy forwarder.
Now, to verify this, we need to go ahead to our search head and check if we are receiving any logs
from the FortiGate.
So now I'm actually able to see the logs coming from my FortiGate.
