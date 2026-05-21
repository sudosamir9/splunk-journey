---
course: saif-admin
theme: 10-capstone-lab
lecture: 59
lecture-title: "LAB: Deploy Base Apps to the UFs, IFs & UF on Windows via the Deployment Server"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/10-capstone-lab, transcript, kind/video]
---

# Lecture 59 — LAB: Deploy Base Apps to the UFs, IFs & UF on Windows via the Deployment Server

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So now we are able to see the intermediate forwarders, the universal forwarders, as well as the universal
forwarder which is deployed on my Windows machine under the forwarder management inside my deployment
server.
So now what I'm going to do, I'm going to use C.P to actually copy these apps that I've already prepared,
which I'm going to be sharing as well with you using CP.
And I'm going to copy those from my local machine to this deployment server.
So let's go ahead and do that.
So I'm just going to go to my CP and this is my public IP address of my deployment server, which is
deployed on the AWS.
Just going to log in.
It's going to take a moment.
So I've logged in.
So what I'm going to do, I'm going to go under Ops Splunk at C deployment apps.
This is where the apps should live, so they should show up here.
Let me just show you that here.
So let's go ahead and do that.
I'm going to go to my directory.
I'm just going to copy.
Those apps that I've created to here.
So it's going to take a while.
And now let's go ahead to my deployment server.
And actually log in via SSH.
So let's do that.
Clear.
Then I'm just going to paste the IP address of my deployment server.
Let's log in.
Here we go.
So we logged in.
Let's go to CD opt.
Splunk at C.
Deployment apps.
Let's do LA minus LA.
And as you can see now, I have all my apps that I've copied using the CP in here so I can see them
in here.
So basically, make sure that the ownership of those apps are Splunk Splunk.
So let's go to the folder management by the web and let's do a refresh.
So now I'm able actually to see the apps that I've deployed.
Now you need to use a naming convention or a way that you can recognize the apps that you're going to
be deploying.
This is very much true and very large environments where this list could grow rapidly as well as the
clients.
So what are we going to do is we're going to link an app to a deployment client.
And the way to do that is through the server class.
So now we have the apps listed in here.
We have our clients, the deployment clients in here, which are a bunch of universal folders, intermediate
folders.
So we're going to create a server class, as previously mentioned in my slides to link an app to a deployment
client.
So let's go to our diagram.
So let's discuss that briefly.
What I'm going to do first, I'm going to deploy an app to these intermediate folders so they can forward
the logs to index one.
So let's do that together.
So first, let's go and examine this.
Now for index one, the internal IP address.
And with one, two, six actually with 1 to 5, this is the private IP address.
So let's go to our CLI.
And check that.
So the app that I'm going to be using is demo Lab.
I f outputs base.
So let's see D to demo.
I.
F.
And then let's go to local and let's do sudo nano outputs dot com.
And as you can see, this is the destination IP address of our indexer, one which we verified.
So now actually, we need to change this.
To Indexer one.
So it's always good to verify if you've configured your configuration correctly, your parameters.
So now I've saved it.
And let's make sure that it is Splunk.
Splunk.
Good.
So now I'm going to go back to my forwarder management.
And I'm going to go ahead and create a server class.
So let's go ahead and create one.
So I'm going to name it.
Intermediate forwarder base.
Outputs.
To.
Indexer one.
Now we're going to add the app, so I'm going to be using the demo lab.
If outputs base, let's save that.
So now I'm going to add the clients to this server class.
So let's add the clients from here.
So I'm going to include intermediate forwarder one and intermediate forwarder two.
So let's do that.
So this is intermediate folder one and this is Internet forwarder too.
So what I'm going to do I f and then a star which is going to match against this one and this one.
So let's do a preview.
And in fact, we've chose both.
And then what I'm going to do, I'm just going to save that.
Now we can see that this app, which is the demo lab, if output space have been deployed, has been
deployed to F one and if two.
Now, to confirm that we are actually now receiving the logs from intermediate forwarder one and intermediate
for two on the index or one here.
So this way let me show you.
So let's go to our search head and actually formulate a query for that.
So let's go to our search head here and let's go for.
Index internal Stats account by host tool for the last maybe 15 minutes.
Let's search.
And as you can see now, we are receiving also the logs from I.F. one and I.F. to.
So now that we have configured those two intermediate forwarders to forward the logs to index one from
here.
So now what we need to do, we need also to create another server class to instruct those two intermediate
forwarders to listen for incoming traffic from these universal forwarders.
So first let's go ahead and actually create another server class.
So let's go in here and let's create a new server class and I'm going to call it I f underscore.
Base.
Underscore inputs.
That's it?
Pretty much.
So let's save it.
And now let's add the app.
Which should be demo lab input space.
So basically in this app we have the configuration to enable the lesson on 9997, So let's save that.
Let's add the clients.
Which would be if one and if two.
So.
Based it put a star, which is a wild card preview.
So I have one and I have two.
Let's save that.
Let's edit.
And let's do also trigger a restart on these two intermediate forwarders.
So now what I'm going to do.
Let's go back to our lab diagram.
I'm going to instruct the universal folders which are deployed on my Linux machines in here to forward
the logs, to load balance the data to intermediate for the one, an intermediate forward or two.
And the same for this one to intermediate 4 to 1, intermediate forward or two.
So what we need to do, we need to create another server class.
Now the reason why I'm excluding the universal folder, which is deployed on my Windows machine, because
for this one, which is installed on my local machine, I need to provide the destination IP, which
is the public IP address of the intermediate folder one and intermediate folder two.
So we will need to create another app for that.
So first let's focus on the those universal folders which are deployed on my Linux machine.
So let's go back to the folder management.
Let's create another server class and I'm going to call this server class UDF underscore base, underscore
outputs to I.F..
So let's save that.
Let's add the app, which is Demo Lab.
UDF output space.
Let's save that.
Let's add the clients.
And this is a wild card, so I'm going to put a UDF star.
Let's preview.
So I'm selecting you f two and you have three.
But I didn't assign the proper host name to this one, so I'm just going to copy it.
And I put a comma.
I'm going to paste it in here.
Let's do a preview.
So I'm selecting also this one.
So let's save that.
So basically now I'm going to do an edit to trigger also a restart on these three universal folders.
So now I have deployed an app to configure those three universal folders to forward the logs to the
intermediate folders.
So basically those to load balance the data to the intermediate folders like this.
So let's go back to our search head and make sure that this is working.
So this is the search head.
So let's go back and verify that our new universal forwarders are actually forwarding the logs as well
through the intermediate folders to our indexers.
Which is Indexer one in this case.
So as you can see now, we're actually receiving logs from UDF three.
And from you f one.
And we should see as well maybe you f too soon.
So let me just do the last 15 minutes.
So now we're actually able to see as well.
You have two.
You have three as well as our universal folder one.
So let's go back to our diagram in here.
So we have configured as well the universal forwarders to forward the logs load balance that logs to
intermediate 4 to 1 and intermediate forwarder to.
And these two as well to forward the logs to index or one.
And all what we have done is through the deployment server from a centralized location.
And now what are we going to do?
We're going to go ahead and create a new app solely for the universal forward deployed on my Windows
machine.
So to do that, what I'm going to do, I'm going to go to my deployment server and connect via SSH.
So let's do that together.
So let me just copy the IP address of my deployment server.
And let's go back to my cell.
I got a paste, the IP address.
So what I'm going to do, I'm just going to create a new app and I'm going to rename it.
So I'm going to copy the content of this one to a new directory.
So let's just copy that.
I'm going to do sudo minus.
So sudo copy minus r.
Demo lab UFS Output space.
And I'm going to rename the new one as underscore Windows.
So this is only for the Windows machine, so let's save that.
Now I have created a new app in here.
So what I'm going to do.
I'm going to cede to that one.
Um, you f underscore windows.
I'm going to do sudo nano.
Local and then outputs dot com.
And in here, instead of my private IP addresses of these two intermediate forwarders, I'm going to
provide the public IP addresses because remember, my Windows machine is locally where I have deployed
the universal fluid.
So let's go to the instances and I'm going to copy the public IP address of my intermediate folder one
and two.
So this is the first one.
I'm going to paste it in here.
Let's go to the second one, which is this one.
Copy it.
Then going back in here and I'm going to remove the private IP of the same intermediate folder.
Just going to face it like this.
So I'm going to save my configuration CD.
Then I'm going to do lz ll h making sure that it has the Splunk ownership.
It does not.
So we need to do that and change it.
Sudo tron minus r for recursive splunk.
Splunk, then demo udf underscore windows.
So now I have my.
Windows app up and ready.
So let's go back to our.
To the deployment server.
So let's go to the forwarder management.
Let's go to the apps and the app.
Here we have it.
So let's go ahead and create a new server class solely for my universal folder, which is deployed to
my local machine.
So let's name our new server class as UDF, underscore base outputs out puts, underscore to.
And I'm going to call it Windows so I know what is this server class used for or the purpose of it.
So let's add an app.
Which is going to be this one.
Let's save it.
Now let's add only my windows.
Universal food.
Which is this.
Control.
C Control V Preview.
Let's save it.
Now let's edit and also enable the restart of the Splunk daemon on my universal folder.
Deploy to my Windows machine.
Let's wait and then we can verify.
If we're actually receiving as well the logs from my Windows machine where my universal folder is deployed
too.
So I think I'm not going to receive any logs from my universal folder deployed on my local machine because
I need to check whether I have allowed the inbound traffic to this intermediate folder from the outside
on 9997.
So let's go ahead and click on the first intermediate forwarder.
Let's go under security and let's check if I allowed this.
In fact, I don't see anything which is allowed, basically.
So what I need to do, I need to go ahead to security groups and create a new security group.
So I'm going to call it outside.
9997 windows.
So control C.
Control V.
I'm going to add an inbound rule where I'm allowing 9997.
Let's do it from end everywhere.
It's fine.
But now.
So let's create the security group.
Now let's go to my instances.
Instances in here.
Then I need to go to my intermediate folder one.
Under actions security.
And I'm going to add the new security group.
So this is the one outside 9997 windows.
Add it, save it.
Let's go to my second intermediate forwarder.
Which is this one.
And I'm also going to add the new security group.
So let's add that one.
Here at the security group.
Save it.
So now.
Let's go back to the forwarder management.
And for that server class, specifically for the windows, I need to trigger another restart.
So let's save that.
So let's verify this now.
So now we're actually able to see the logs coming from our universal folder deployed on my Windows machine
locally.
So let's go to our lab diagram.
Now, we have successfully configured this this as well.
So now we have successfully deployed our custom apps from the deployment server to our intermediate
forwarders, as well as our universal folders on our Linux machines as well as on my Windows machine.
So now what we need to do, we need to go ahead and start with the different use cases as well as building
our indexes under Indexer one and Indexer to.
