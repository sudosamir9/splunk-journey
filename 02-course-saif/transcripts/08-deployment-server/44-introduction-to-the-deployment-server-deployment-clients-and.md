---
course: saif-admin
theme: 08-deployment-server
lecture: 44
lecture-title: "Introduction to the Deployment Server, Deployment Clients and the Server Class"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/08-deployment-server, transcript, kind/video]
---

# Lecture 44 — Introduction to the Deployment Server, Deployment Clients and the Server Class

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So in this section we will be discussing the deployment server, why we would need it.
So let's jump back to our.
Diagram and explain the reason behind it.
So imagine you have this infrastructure or this diagram where you have a bunch of search heads, you
have some indexers and you have a bunch of universal folders.
Now, as you scale your environment and you introduce more universal folders to be deployed to your
end machines, the more it becomes difficult for you to manage these universal folders which are deployed
on your end machines.
So what we can do is we can rely on what we call the deployment server.
So the deployment server serves to manage large scale deployments with hundreds of others.
We use the deployment server as a central management tool to manage configurations and to be pushed
to either universal folders or heavy folders which act as deployment clients.
So let's go around the naming convention in here.
So.
Let's go to our diagram back again.
Now.
These universal folders, we would call them as we join them to the deployment server, which is here.
We will call those deployment clients, which are either universal forwarders or heavy forwarders.
And the configuration is done on the deployment clients dot com.
We will go ahead and talk about that briefly once we start configuring and deploying a deployment server
and joining the universal folders to the deployment server.
Apps are deployed under Splunk Home at C Apps.
So whatever we want to deploy from this deployment server apps, custom apps add ons we will put.
Those applications apps under Splunk home at C Deployment Apps directory, and then the deployment server
will push those apps to the universal folders.
And they're going to land under Splunk home at C Apps.
So it's recommended to deploy the deployment server as a dedicated Splunk instance.
And this is very much true when as you scale up, because normally the universal forwarders or the deployment
clients in this case will phone home back to the deployment server asking if there are any changes.
And this happens on intervals.
So management port, it's 8089 both directions that means.
So let's go back to our diagram again.
That means that if there is a firewall in between the deployment server and any universal folders,
you will need to open port 8089 by default, which is the management port for both the deployment server
and the universal folder to talk to each other.
So you need to make sure that that port is opened on both directions.
Let's go back to our slides.
So Deployment server again pushes the configuration bundles like apps, add ons, custom configurations,
whatever you want to configure on those universal folders.
For example, you want to push a custom app where you want to instruct these universal folders to,
for instance, monitor certain files and that Windows based machine or that Linux based machine, or
you just want those universal folders to listen on a specific port.
Or even better, you want to configure these universal folders to forward the logs to an integrated
folder or to the index tier.
So how would you go around that?
So the easiest way is to configure custom apps based applications where you can push them from the deployment
server to these deployment clients, which are the universal forwarders and the heavy forwarders.
Now configurations are deployed to deployment clients which are UDF and HDFS under Splunk Home at C
Apps.
So whatever app that you want the deployment server to push to the deployment clients, you need to
put them under deployment apps and those will be pushed.
Two slunk home at C apps directory.
Under those UVs FS deployment, clients pull at time intervals by phoning home back to the deployment
server.
And this is exactly why we would need to open port 8089 so we can enable basically the deployment server
and the universal folders or what we call them in here, the deployment clients to talk to the deployment
server, asking if there has been any changes or into the apps directory inside the deployment server.
So the deployment server will forward those apps or deploy these apps to the deployment clients.
Now, in a moment, we will go ahead, of course, and set up a demo so we can actually configure that
and show you how it's done.
But before we move ahead, I would like to discuss the concept of how we would reference and assign
those applications in here that we want to deploy from the deployment server to the forwarders or the
deployment clients.
We have what we call a server class.
So a server class is kind of a mapping way to to map specific apps to be deployed to deployment clients.
So.
Of course, to make those universal photos, talk to the deployment server.
What we need to do first is to create and push what we call a deployment client file to these forwarders.
And we need to reference the IP address and the management port of this deployment server inside the
deployment client.
So in this way the forwarders will talk to the deployment server and then from now on then the, the
universal forwarders will start talking to the deployment server and then you can place whatever apps
that you want to push, you know, from the deployment server back to the universal forwarders.
This, this is the way to do it of course.
How would you then as a second step, how would you reference or map whatever apps that you have here
to the universal forwarders?
So this is again what we call the server class.
So first we will have a list of our deployment clients, ZFS under the deployment server, then we will
create a server class and in their server class we will reference or we will map whatever desired deployment
apps we want through the server class.
To the desired deployment clients.
So we will create kind of a container, a server class where we will reference the desired universal
folders that we want to push those apps to from a list of our applications which is going to reside
under the deployment apps.
So we will show you that in a moment and we will go ahead and explain all the steps as we progress throughout
the demo.
