---
course: saif-admin
theme: 10-capstone-lab
lecture: 57
lecture-title: "LAB: Deploy Splunk Components and forward the logs to the indexing Tier"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/10-capstone-lab, transcript, kind/video]
---

# Lecture 57 — LAB: Deploy Splunk Components and forward the logs to the indexing Tier

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So in this section, we will go ahead and deploy the different Splunk instances.
So I've already configured Indexer to index or one as well as the monitoring console and the deployment
server.
And I left the search head intentionally for you so we can actually go ahead and do that together.
Now, feel free to follow the same steps that we're going to be doing in deploying the search head and
apply the same steps to deploy index or to index or one and the monitoring console deployment server
as well as the heavy forwarder, because in essence, we're going to be using the same Splunk package
across all of these different components.
While for the universal folders and the intermediate forwarders acting as a universal forwarder, then
we will use a different Splunk package, which is only for the universal forwarder.
So let's go ahead and actually do that.
So what I'm going to do, I'm just going to launch instances.
I'm going to create the search head.
And I'm going to use the urban to flavor.
Now, previously we mentioned that for the universe of orders, one new virtual CPU and one gigabyte
of memory would be enough for the slab.
However, if we go for the system requirements for the search head or for the indexers, they would
require 16 physical CPU cores or 32 virtual CPUs and 12 gigabytes of RAM.
And you see, this is the minimum specs.
Of course, for our lab, I've already tested that it would be more than enough to go maybe with, I
would say the medium instance.
So two virtual CPUs and four gigabytes of memory would be enough.
Now, to compare the instance types in terms of pricing.
You can see that the medium would cost you 0.046 US dollar per hour.
So what you can do again, as previously mentioned, you can just create and deploy the slab for a couple
of days and once you're done, you can just terminate that.
So let's go back and select the instance type.
And now we have assigned the two virtual CPUs and four gigabyte of memory to our search head.
Now I'm going to be selecting my key, which is going to be the this one.
So network settings, I'm going to leave it as it is actually in my lab environment, I will be choosing
the default.
So this is the one.
And now eight gigabytes of storage would not be enough.
I might increase that to 15.
So let's keep it that way.
Now let's go ahead and actually launch the instance.
So now that our search head is up and running, what we need to do is we need to make sure that we are
able to actually access the search head from our end.
So to do that, we need to assign the proper security group.
So let's go ahead to this instance.
So let's click on this one and let's go to action.
And under Security Change Security Group.
Now, I'm going to provide the security group that we have created earlier.
So that would be the Splunk Demo instance group.
So I'm going to add this security group and I'm going to save it.
Now, once we're done, let's go back to the search head.
And under security tab, we can see what what ports are allowed to this new search head instance.
So I've allowed 8000, which is the default web port for Splunk, Web four for 320 to say, and I'm
only allowing it from my IP, which is the IP address of the ISP provider.
So now that we're done.
So let's go ahead and connect to this instance.
So let's click on Connect.
I'm just going to copy this one.
By the way, feel free to change this one to the actual public IP address of this instance.
So you can still do that.
So I'm just going to paste it in here.
And I'm going to include pseudo.
And the proper private key.
The private.
DUP pm.
Yes.
And you can see now that we have successfully logged in, says H to this server.
So let's go back to the server.
Now, this is the public IP address that I was mentioning.
Now, what we need to do is let's go ahead and change the name of this instance.
So sudo by or actually nano.
Etsy host name.
I'm just going to maybe put.
Search head.
Just like that.
And then.
We need actually to do a reboot for this to take effect, but you can leave it as it is, but we can
still do that.
So now I've changed the host name and now what we need to do, let's create the splunk user.
So sudo add user Splunk.
Provide a password.
Retype the password.
Except.
Yes.
Now that we have the Splunk user, we need to go ahead and go under opt.
Now let's go to.
Splunk.
Let's log in.
Just going to log in.
Then I'm just going to copy the W get command so we can install.
And download actually the Splunk Enterprise.
So let's go to free trials and downloads.
So stuck enterprise.
And then I will choose Linux.
I'm going to choose the target set file.
So I'm going to click on this one.
And under download via the w get.
I don't need this one.
I'm just going to copy that.
You get command.
Copy.
Let's go back in here.
Paste it.
Don't forget to add the pseudo.
Zero.
So now I'm downloading the Splunk Enterprise package.
I have it in here.
So sudo let's enter this file due to tar minus x z vrf.
Splunk.
So I'm tarring it.
So once we are done, we need to change the ownership of the Splunk directory.
So you see, we need to change those.
So what we need to do is sudo tron minus R for recursive splunk.
Splunk.
And then Splunk.
Now, if we see now we have changed the ownership.
Now, bear in mind that as previously mentioned, you need to go ahead and enable the and configure
basically the you limit as well as disabling the transparent huge pages.
These are best practices provided by Splunk.
Now, for the sake of this lab, I'm not going to do those, but please feel free to go ahead and do
that.
And you can follow my previous sections where I have provided a thorough demo on how to configure the
ultimate as well as disabling transparent, huge pages.
So now that we are done with Splunk, feel free to remove this one.
So sudo remove Splunk dash nine.
So now we are left only with the splunk directory.
So CD upped splunk.
Now what I'm going to do?
Zu.
Do zu.
Splunk.
So let's go ahead and actually start Splunk.
So, Ben, Splunk start.
Hate.
Q And then why accept the license agreement?
And then I'm going to create a Splunk user.
And a password, and I'm going to confirm the password.
So once we are done and the Splunk instance is up and running, then we can confirm that.
So let's wait.
So now Splunk is up and running.
What we can do status.
And you can see Splunk Daemon is running.
So now that we have successfully connected via Sage and we have also deployed the Splunk on this search
head instance.
So let's go ahead and connect via the web.
So let me just copy this IP address.
So this is the public IP address.
I'm just going to base it in here and I'm going to include the port 8000.
So I'm just going to include Splunk, the username.
So now let's go to settings and actually validate few settings under the server side.
So if we go to general settings, this is the management port.
This is a Splunk server name.
You can actually also change it in here so we can do search head.
Like this run.
Splunk wipes enable us to slash tips on Splunk Web.
Yes, let's do that.
Web port is 8000.
So that should be OC.
I'm going to also include here search head.
So let's save that.
And what we can do now.
It requires a restart.
So let's just go ahead and restart Splunk.
Let's wait for a minute.
Of course.
Now what we need to do, we need to include the HTTPS and here.
And your connection is not private because we are using a self signed certificate.
On the Splunk side.
So now just include the username and the password again.
And now we're able to log in to the Splunk Web again.
So basically, let's go back to our lab.
So basically, we have deployed the server on AWS as well as we have successfully deployed the search
head on this server.
So now we have the Splunk search head up and running.
What I would encourage you guys from now on is to go ahead and repeat the same steps to configure the
indexer to index or one the deployment server in here as well as the monitoring console.
So now once you have provisioned all the servers in here and I'm talking about the search head index
or two indexer one the monitoring console, the deployment server and the heavy forwarder as well as
deployed the Splunk on these different hoses as I've done in here.
Now what you need to do is you need to configure all of these instances to forward the logs, the internal
logs to index or to so basically from the heavy forwarder from the search head.
From the monitoring console as well as from the deployment server.
Forward all their internal logs to indexer too.
So let's do that together now.
What I would suggest is to have the public IP column here and the private IP addresses here, and we're
going to be using actually the private IP addresses.
So what I've done, I have just wrote down so I've written down all of the public IP addresses and the
internal IP addresses of their corresponding instances.
So what we want to do now, we need to go ahead and log in to every single Splunk instance here and
configure it to forward the logs, I mean the internal logs to Indexer to which is this one.
So let's go ahead and start with the search head.
So I'm going to go ahead and copy the IP address, the public IP address of my search head.
So this is the one.
Then I'm going to go to my cell.
I.
And then I'm going to delete everything in here.
I'm just going to paste it.
Hit enter.
So I have locked to my search head seed to opt seed to Splunk at C apps.
So under the apps directory, I'm going to create a new app.
So let's go ahead and actually create this directory.
So sudo vector.
And then.
For warding.
To index or to you can name it the way you like it and then under that, so seed to forwarding.
I'm going to create another directory which is called local.
And then I'm going to also create the metadata.
So meta data.
So first I'm going to start with the local so seed to local.
And here I'm going to create the outputs dot com.
So sudo nano outputs, dot conf.
And in here.
I'm going to copy the configuration.
Which is this one.
So copy.
Paste So I'm going to put the server.
IP for my indexer too.
So if I go back to my.
Notes.
I'm going to copy the internal IP address, so let me paste it.
Save it.
And then.
Go to.
Matter.
And then in here, I'm going to copy.
Basically the configuration.
So bear with me a moment.
So I'm just going to copy this one.
Copy.
And then I'm going to create sudo nano local dot meter.
Hit enter.
Based it.
Trial x Y.
So now let's go out from here for a second.
So if you notice, I've created this app now for forwarding.
So what I'm going to do, I'm going to change the ownership.
So sudo chon minus R splunk.
Splunk.
Then I'm going to give that app name.
The path.
So now.
I have that.
Under Splunk.
Splunk.
So what I'm going to do.
Seed.
Then I'm going to do Zoo Doe Zoo Splunk.
And I'm going to restart my Splunk instance here.
So then.
Splunk.
Restart.
So let's wait for the search had to restart and the meantime, what we're going to go I'm going to go
to index cert two, which is this one.
Let me just copy this IP.
And go http.
And access that indexer to.
So let's wait.
For a second.
So it seems like it's not running.
So what I want to do, I'm going to log in to the Indexer two, which is here, and I've done Splunk
status and I can see Splunk DX is not running.
So what are we going to do on this Indexer too?
I'm going to start.
So let's start it.
Let's wait.
And once the index or two is up and running, then hopefully we will be able to get to the Splunk web.
So let's do a reload.
And here you go.
So now.
Let's log in to the indexer.
So I've already restarted the search head.
So for the configuration to take effect now, I'm going to go to the search and reporting.
Just to make sure that the configuration that we have done is correctly, that we have actually created
the app, which is this app.
Let me show you.
So we have created basically this app.
And the outputs dot com to forward the internal logs from the search head to the indexer, too.
So let's go to the indexer.
So we're going to do index equal to underscore internal.
And let's do pipe stats count by host.
So still we don't see anything last 15 minutes.
Of course.
Why we're not seeing anything.
So, folks.
That is because we've only configured.
The search had to forward the logs to the indexer too.
But remember, we never configured the indexer to on listening mode.
So what we need to do actually, we need to go to the indexer to.
Which is this one here?
And what we need to do is we need to configure this indexer to for listening mode.
So let's go see the opt splunk at C apps.
And then here I'm going to do the same.
So make directory.
I'm going to call it.
Listen up.
Underscore.
Listen.
Inputs.
And then I'm going to do local.
I'm going to do meta data.
So let's go to the app underscore lesson local.
And in here I'm going to create nano inputs.
Dot coff.
So here, I'm just going to paste.
This configuration.
So I'm instructing this indexer to listen on incoming traffic on Portugal nine seven.
So let me just save that.
And then.
I'm going to go and create the meta data local meta.
So seed to metadata and then nano local dot meta.
I'm going to paste the same configuration in here as well.
So I'm going to do is to.
This one.
So copy this one.
The pasted in here.
Control X.
So.
Let's make sure that.
The ownership of this app is Splunk.
Splunk?
Yes, it is.
And you can see this is the one.
Now, once we are done with this one, we need to restart the Splunk instance in here.
So I'm going to do.
Ben Splunk.
Restart.
So let's wait for a while until this instance is restarting and then we will verify if this indexer
is actually listening on 9997.
So let's wait.
So to verify this was to assess minus a N and we want to grep for 9997.
And you can see that this indexer now is this on 9997.
Now let's log back again to our indexer.
Which is index number two.
And now let's search for the last 15 minutes again.
So now, as you can see now, we are actually receiving the internal logs from the search head on this
indexer.
So.
This is what we have done.
So basically we have instructed the search head through the outputs to conf to forward the internal
logs to the index or to.
Also, we have seen that first we forgot to enable the 9997 on listening mode.
So this is what we have done.
So now what I would encourage you to do is.
Copy the same configuration that we have done in here to index one and also the same for the search
head to copy the output conf to the monitoring console, to the deployment server and also to the heavy
forwarder.
So what I'm going to do basically.
Um, let's go and do that.
So from the search head, I'm going to skip that app.
To basically monitoring console to the deployment server, to the heavy forwarder so we can receive
all the logs, all the internal logs on index searcher.
So let's do that together.
So let's go ahead and copy the app that we have just created under the search head, which is this one.
Let me show you.
The forwarding to index or to.
So the internal logs, we need to copy this app to all the other Splunk instances.
And what I mean by that, the heavy forwarder, the monitoring console, the deployment server and to
do that all what we need to do.
So what we need to do is we need to go ahead and use this step command.
So let's first paste the IP address of our deployment server.
So I'm going to copy this IP first.
So we're going to copy it to the deployment server.
Based it.
Under the temp directory.
Now we are facing this issue.
Permission denied.
So how to fix this issue?
So what we need to do is we need to go back to our instance.
So let's go to the instances.
So let's go to the deployment server in here.
Let's click on Connect.
Let's copy this one.
And let's go back to our terminal.
Paste it.
I'm going to change.
The private key private PM include pseudo.
So in the deployment server now.
So what we need to do basically.
We need to copy basically this one.
So let me copy it.
Base it in here.
Then we need to find the value.
Which is.
Password, authorization, authentication.
And we need to change this to.
Yes.
So let's save that and then let's do a system.
CTL restart of the S.H. server.
Copy paste.
All is good.
So now let's go back to.
Our.
Search head.
So KD upped Splunk at C Apps.
And now.
I'm going to just copy the IP address of this instance, which is the private one which ends with 218.
There you go.
And I'm going to just hit enter.
And I've copied that app to do the deployment server.
So let's go back to the deployment server now.
Seed upped or actually seed temp.
And this is actually the directory.
So let's do pseudo copy or word.
To opt Splunk at C apps.
So we need to do an include A minus R for recursive.
So now KD upped Splunk at C Apps.
Let's do la la.
And this is the one.
Let's change the ownership.
So sudo tron minus are Splunk, Splunk.
And then forward.
Now that we are done, what we need to do, we need to do a restart.
So.
Zoo Splunk.
Then De Ben.
Splunk.
Restart.
So now we are starting restarting the deployment server.
Let's wait for it to finish.
And then we will go back to our indexer.
To see if now the deployment server is sending the internal logs to the indexer, too.
So let's wait for a moment.
So let's go back to our indexer.
Let's do search.
And here you go.
Now we can see the deployment server as well.
So once you have copied the app that we've created on the search, head to forward their internal logs
to the indexer, too.
And I mean by that, to the heavy folder, to the monitoring console, to the deployment server, then
you should see something similar to this.
So I am logged on the Splunk indexer, too, and you can see that now I'm receiving all the logs, the
internal logs from all these Splunk instances.
