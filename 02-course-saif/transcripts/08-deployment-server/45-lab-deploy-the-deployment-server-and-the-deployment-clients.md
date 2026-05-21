---
course: saif-admin
theme: 08-deployment-server
lecture: 45
lecture-title: "LAB: Deploy the Deployment Server and the Deployment Clients"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/08-deployment-server, transcript, kind/video]
---

# Lecture 45 — LAB: Deploy the Deployment Server and the Deployment Clients

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So for the sake of this lab, I have already configured and deploy two universal forwarders on my two
Linux instances.
And then I will be configuring and enabling my deployment server on my indexer.
Typically, in a real world scenario, when you're facing the customer and depending on how many universal
forwarders that you're going to be managing from the deployment server, it's always advised to have
the deployment server deployed on a dedicated Splunk instance.
As you scale up, that means you need more specs.
So it's better to have the deployment server run on one dedicated Splunk instance.
I do think that for Linux, universal Forwarders, Linux based machines, you can actually deploy and
manage up to 10,000 universal forwarders from one dedicated Splunk instance where you're going to have
a deployment server run on it.
So.
What we're going to be doing as the first step is to configure the deployment client dot com on these
two universal forwarders.
So they're going to be able to talk or phone home back to the deployment server.
So let's go to our slide and check that together.
So configure port management.
So what are we going to be doing is, as a first step, I will be deploying the deployment client dot
coms on these universal forwarders.
And as a second step, I will add the desired apps that I want to deploy to these universal folders
on their Etsy deployment apps.
So I'm going to be placing those here.
So let's go to my Splunk Web.
So here.
We go under settings.
Forward or management, we click there.
So here for door management, the former management UI distributes deployment apps to Splunk clients.
No clients or apps are currently available on this deployment server.
So what we need to do is there are two ways.
Either we deploy the deployment client to these universal folders so they can appear, or we can also
deploy the applications under its C deployment apps.
So let's first I'm just going to copy.
Those go to the indexer under Sealy.
So if I do see the upped Splunk it see deployment apps.
Here.
I don't have anything as apps.
So that's why we don't see anything in here.
So what I'm going to do, I'm going to copy.
My Cisco app.
Which I have it here.
I'm going to paste it under opt Splunk at C deployment apps.
So I need to be.
So put zero.
So I've just copied it.
And the Cisco app is here now, but I need to change the ownership of this app.
So Sudo chan minus R for recursive Splunk.
Splunk.
Cisco.
So now we have that under Spunk and Splunk.
So if I'm going to do a refresh in here, you see now that now the forwarder management has been activated.
Repository location is Splunk home at C Deployment Apps, which is exactly what we have done.
So I have copied the Cisco iOS app.
I first downloaded it from Splunk Base and then I've put it in here under Splunk at C deployment Apps.
So this one, this path, which is this path.
So.
Slunk home.
It's basically the global variable for Splunk.
So now if we go under APS, we see that the Cisco app is there and it's enabled, but it's deployed
to zero clients.
So this is the first step.
We don't have any server class and we don't see any clients in here.
So what I mean by that, we don't see any universal forwarders.
So what I'm going to do now, I'm going to go to my two universal folders.
So this is the first universal folder.
And this is the second universal photo.
So what I'm going to do, I'm going to copy.
So pseudo copy minus R.
Opt Splunk forwarder.
I have already an app which I've created, which I'm going to go through it.
This is the app.
I'm going to paste it under opt Splunk folder at C apps directory.
So now we have in here this app that I've just created.
So let's examine that.
Of course, under this app we have the local and the metadata under local.
I have the deployment client dot coms.
So let's examine that deployment client and what I've done.
So do I know.
It's going to be all local.
Deployment client dot com.
Let's examine that.
So this is pretty much the stanza that I need to create under the deployment client.
And I will be providing this in the in the course.
So this is the stanza.
And I'm just referencing here the target URI, which is the IP address and the management port of my
deployment server, which is this one.
Which is acting.
So this is the index cert, which is acting actually as a deployment server as well.
So let's go back.
All I'm doing, I'm referencing and putting the IP address and 8089 so I'm going to save that.
And then what I'm going to do.
I'm just going to change the ownership of the app that I'm doing.
So let's do sudo chong minus R splunk.
Splunk.
And then all deployment clients.
One minute and I will show you exactly what I mean by one minute.
So let's go to deployment.
Clients scoff.
And let's examine.
What kind of parameters that I need to provide.
So if we go to this is the deployment client.
This is disabled equal to boolean.
We need to actually reference that.
So.
What we need to do is we need to actually copy this one.
Now by default.
The universal forwarders.
Let's go in here.
Phoned home back to the deployment server every 60 seconds by default.
So we can overwrite that.
By setting this maybe to 2 minutes, 120 seconds.
So what I'm going to do, I'm going to go back to the.
Deployment.
Client dot file, which is here.
And I'm going to change that.
As you can see in here, phone home and travel in 60 seconds.
I can do that maybe 120.
But it's really up to you how often you want your universal forwarders to go and talk to your deployment
server.
Normally for customers with large environments and you have they have probably thousands of universal
folders and you don't want to put a lot of burden on your deployment server.
So you can maybe put that up to every 5 minutes or every 10 minutes.
So let's keep that to 60 seconds.
So let's save that and go back.
And again, this is the target, Uri.
So if we copy that, we go in here so we can have a better idea about what does it mean?
So this is the target, you or I?
The target, you or I of the deployment server.
So.
For for a better understanding of the deployment clients dot com.
Always you can go back to the Splunk documentation because it provides really a good and thorough information
about the different options that you can set and configure.
So that's now that we have configured our deployment client dot com under this Splunk Universal folder.
I've already saved it, so I'm just going to restart my.
Universal forwarder.
So pseudo.
Then.
Splunk.
Restart.
Once we restart it, then we should wait for 60 seconds.
And then.
The universal folder here should appear.
The first universal folder should appear.
So I'm just going to refresh.
Just going to wait for a few seconds.
So it's already up and running.
So our first universal folder just appeared, which is here, and this is the universal folder.
As you expanded here, you see that no apps has been deployed and there are no server classes associated
with this universal folder.
So let's go ahead and do the same for the second one.
So what we need to do is I copy the same.
So copy sudo.
Copy minus r opt Splunk forwarder.
All to opt splunk forwarder at C apps directory.
And under here.
We have.
All deployment clients.
And then.
I'm just going to go.
There.
Local.
And I'm going to show you the.
Deployment clients dot com.
So in here is exactly the same.
The target tree is my deployment server IP address and the management port and then terrible phone home
back to the deployment server is every 60 seconds.
So what I'm going to do is just change the ownership of that application.
So opt splunk forwarder C apps that all.
And I'm going to restart Splunk.
Universal Forwarder.
So Zullo then Splunk forwarder.
Splunk.
And then restart.
So the the the settings or this new configuration will take effect.
By the way, we can always use B tool as a good command to to see if the changes took effect.
So what we can do is.
We can do B tool.
And then deployment client, which is the name of the the configuration.
And then list.
And let's do debug.
And as you can see in here.
These changes took effect.
So we need to wait for 60 seconds or more, depending on how fast the individual Ford is going to talk
to the deployment server.
Let's do a refresh and then it should appear here in a few seconds.
So now we see that the second universal photo also appeared, and this is the IP address and this is
the IP address of both universal folders respectively.
And you can see this is the host name.
This is the client name.
And also under here, we don't have any apps associated and deployed because you see here there is zero
deployed, zero deployed.
So now that we have the two universal forwarders for the purpose of this lab and I have my app in here,
what I'm going to do, I'm going to actually deploy another app under the deployment apps directory.
So it's going to show in here.
So let's go back to our deployment server.
And this is here.
So I'm just going to copy another file or another app, a custom app home.
I've copied there.
So desktop UDF.
F Where did I save that?
It's under here.
There you go.
Then I'm going to place it under Ops Splunk at sea.
Deployment apps.
So let's check that one more time.
And here you go.
You have the UDF based inputs.
So in this app, the custom app, what I have.
So let's examine that.
So seed UDF.
Local.
And this is one I have input and output scores.
So it's pretty much configurations that I have configured to instruct the universal forwarders to do
certain behavior.
So if you examine the inputs, nano inputs dot com running the scripts.
So I'm just instructing the universal photos to run the top the process and the net stat through the
script.
This is a scripted input.
Of course.
Definitely.
I need to have also the bin directory where I'm going to be referencing and calling those scripts from
the input scope.
Also, what we have under the local, we have the output dot com.
So let's examine that.
Out to scoff.
Pretty much what I'm doing is just forwarding logs to my indexer on Portable nine seven.
So what I'm going to do, I'm just going to deploy this.
You have based inputs also to to those to universal folders, and I'm going to do that using the forwarder
management.
So now that we have placed.
My app under the deployment apps.
Which is the repository for all the apps that I want to deploy.
Just going to change that, the ownership.
Zero churn minus are Splunk.
Splunk.
U.S..
So I have both now.
So if I do a refresh.
There you go.
Now I have my UDF based inputs as well and the Cisco iOS app.
As a final step.
Since we have the clients ready and we have the apps, I'm going to associate and map whatever I have
here.
And the apps to my clients by using the server class.
So let's delete that and let's go to server classes.
So what I'm going to do basically.
So let's do a refresh.
So let's create one.
So I'm going to name this server class.
Just follow some naming convention that it's going to be easier for you to interpret and make sense
out of the server class.
So I'm going to call it.
Base.
So u f underscore base.
Underscore inputs.
Simple.
So let's save that.
I'm going to be associating the app that I want, so I'm going to put this as a UDF.
I'm going to save it.
And then I'm going to add also the clients.
So how can I add the clients?
This is a wild card.
So if I put a star and I do a preview, it's going to take both.
So if I do only you f one and I do a preview, I will be selecting only one UDF.
So based on this, you can whitelist the ones that you want.
So what I'm going to do, I'm just going to also you can do UDF and a star.
So it's going to take UDF one and UDF two.
So there are different ways where you can actually using this wild card to select and match the ones
that you want to associate with.
In this case, I'm just going to put a star.
Just going to do a preview.
It's already selected.
Of course, you can exclude as well.
So let's save that.
So now.
As you see here, this app is enabled and deployed apps successfully.
To those two universal folders.
So basically I have deployed this.
Inputs dot the inputs dot com that I've just shown in the outputs dot com, which is this app under
here.
This you have base inputs.
To those two universal forwarders.
And if we expand it here, you can see the app that I've deployed and the app that I have deployed.
So let's go back to the folder management.
And you can see now.
Deployed one app deployed, one app deployed for those two universal folders.
So this is one server class that I've created for that purpose.
I'm going to create another server class.
I'm going to call it Cisco because we want to deploy the Cisco app.
And I'm going to call it maybe Cisco app underscore usf's just, you know, choose an appropriate naming
convention that's going to suit you.
So save that.
I'm going to add the desired app, which is the Cisco iOS.
I'm going to save it and I'm going to associate.
Whatever universal folders that I want.
For the sake of this demo, I'm going to put on the U.
F one.
For instance, I'm going to do a preview.
And I'm selecting only you f one.
I'm not deploying this Cisco app to UF two on the UFT one.
So let's save that.
So now we have deployed the Cisco iOS app using the server class mapping to only the UDF one.
So let's go back to our forwarder management.
Now you can see that for the Cisco app UDF.
Actually, if we go to clients, you can see that for the UDF one, I have two apps deployed.
We expand in here, we have the UDF base inputs and the Cisco app.
While for UDF two, I only have the UDF base inputs.
So as a final step, just for verification, let's go to uf1.
And us to.
So if we go under seed, if you remember that all the apps that are going to be deployed from so all
the apps that are going to be deployed from the deployment server to the universal forwarders, they
are all going to land under Etsy apps.
So let's do that.
Let's go back to the Universal folder one and two.
So CD.
Etsy apps.
As you can see here, for the universal folder too, we only deployed u f base inputs.
While here it's clear and do c d at c apps.
We actually deploy two apps, Cisco, iOS as well as you have base inputs.
So this is the way on how to manage your APS and deploy them to your universal folders from the deployment
server.
