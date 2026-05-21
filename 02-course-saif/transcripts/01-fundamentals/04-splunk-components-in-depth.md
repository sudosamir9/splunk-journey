---
course: saif-admin
theme: 01-fundamentals
lecture: 4
lecture-title: "Splunk Components in Depth"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/01-fundamentals, transcript, kind/video]
---

# Lecture 4 — Splunk Components in Depth

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

In this section, we will be talking about strong components, but more in depth.
So let's start with the Splunk forwarder.
So the forwarder is an agent that you deploy on IT systems.
It collects logs and sends them to another Splunk Enterprise instance, as I've shown you in the previous
slides.
It is very fast, requires less resources on the host with minimal footprint.
So what I mean by that?
So if we go to the Splunk website where we want to download the universal forwarder.
So as of this recording, it's 9.0.1, the Splunk version.
Now, as you can see, it's a 28 megabytes of data, so it's not really big.
The package now, mainly because it does not support Python.
No, I mean user interface.
It's just used to collect the logs and the data which is going to be forwarded from the universal forwarder
is uncooked.
So pretty much it's passed now.
It's regarded as the best data collection method and the most common way to get data in.
So pretty much in large scale environments, the universal folder is the way to go and there's no license
needed.
It's pretty much free.
Now let's move on to the Splunk indexer.
The index search transforms the data into events unless it was received pre processed from a heavy forwarder.
Now, I never mentioned the heavy forwarder in the previous slides, but in the next slide I will be
talking about the heavy forwarder and the difference between this one and the universal forwarder.
So Splunk Indexer stores it to disk and adds to an index, as I've shown you before, and enabling search
ability, the indexer creates the following files separating them into directories called buckets.
So.
When data is stored into the indexer, it's pretty much gets separated into buckets and it will contain
the compressed raw data as it receives it, and then indexes pointing to the raw data.
And this pretty much will enable fast search ability.
So to see the X Files, it's going to kind of like a pointer to the raw data.
Think of it as an index of an index.
By the way, this subject is going to be part of my next course, which is going to be a very advanced
topic about Splunk Enterprise deployment, which is part of the architect certification.
Now, metadata files how source and source types are pretty much annotated to the logs.
The indexer performs generic event processing on the log data.
So this is the Splunk Indexer.
Now, let's get to the interesting part, which is Splunk.
Heavy forwarder.
Now.
It is a full Splunk Enterprise.
That can index search and change data as well as forward.
So think of the Splunk heavy forwarder, just like a normal full blown Splunk instance.
The only difference is that between the Splunk heavy forwarder and the universal forwarder is that they
Splunk heavy forwarder will parse and index the data.
Note that the universal folder has no python packages, as I've just mentioned that in the previous
slides, while the Splunk heavy forwarder is a full blown Splunk instance.
You can actually enable the option to index the data in here, but normally you will just avoid that
now.
Note that when data comes from the heavy forwarder indexers, do not parse the data again when you receive
the logs and send them to Splunk.
Heavy forwarder.
It has the capability to actually search, pass the data, and it's going to be part of the license
meter.
So the data will be sent actually from the Splunk IP forwarder to the indexer cooked.
That means when the indexer will see this data cooked, it's not going to parse the data again, it's
just going to skip the parsing pipeline into the indexer.
Now, this is going to be a very important question.
It might come up into the exam.
Now how you forwarders are also used to run Splunk add ons that receive data from external resources
data forward.
Our past, as I've mentioned, that larger footprint with respect to UPS, which are the universal forwarders
and of course it require a license.
Now why would we need Splunk heavy forwarder?
Ultimately the heavy forwarder.
It's used to forward the data.
Now, I've mentioned earlier that the big difference between stomach heavy forwarder and the universal
forwarder, that it's purchased the data and it is a full blown Splunk instance that means it supports
Python.
So the happy forwarder actually has a UI interface where you can pretty much deploy the Splunk DB connect,
where you're going to send logs, structure data from databases through the Splunk DB connect plug in,
and the heavy forwarder will parse this data.
Also, the Splunk heavy forwarder could receive HTTP event collectors.
So what I mean by that?
So imagine logs that you want to send from a source, but you don't want to install the universal forwarder
there.
So you can actually enable this feature where the Splunk heavy forwarder will receive this data based
on an HTTP token which will be generated in here and pretty much will pass this data and will accept
it without the need of any universal forwarder on the end machine sending those logs.
Now Splunk searched The search had provides the UI for users to submit searches via the spill query.
It allows users to search and query Splunk data, and also it provides a distributed search architecture,
which allows you to scale up to handle large data volumes.
Exactly as I've shown you in the previous slides, where we have dedicated search head, where it's
going to go ahead and submit a search request query to the indexer to retrieve the desired data.
Splunk Deployment Server.
I have mentioned that before.
So what is a Splunk deployment server?
It's regarded as a centralized configuration manager.
So in large scale deployments, where you're going to have and deploy thousands of universal forwarders
to the end machines where you want to collect the logs from these end machines, it becomes really tedious
and really hard to actually manage the universal forwarders.
So the deployment server is nothing but a centralized manager where you can actually manage those universal
forwarders.
So users interface with the forwarder management deployment clients a.k.a. Universal Forwarders, and
heavy forwarders, for example, are remotely managed by this instance exactly as I've mentioned that.
You can use the deployment server to actually deploy apps and configuration files.
To the universal forwarders in large scale deployments under the deployment apps, deployment clients,
which are the universal forwarders and the heavy forwarders phone home at intervals.
Back to the deployment server.
So if we go back, I will exactly show you what I mean by that.
So in here.
Let me take pencil.
So this is the deployment server.
Now imagine you have hundreds, thousands of forwarders, universal forwarders.
So how you would go and manage all of these when you want to deploy, for example, applications or
configurations that you would like to monitor certain files and law files basically in those end machines.
What would you do?
You will use the deployment server in here to actually deploy all of these applications, apps and configuration
files to those forwarders at a large scale.
So it becomes very much easy for you to manage all of these forwarders.
Now let's, of course, the four orders I almost forgot.
They will phone home back to the deployment server, asking if there are any updates to these configuration
files through checking the hashes of these applications and if there's any difference.
Now, the forwarders will actually pull in a pull mode, will get those apps and updates.
Now let's start with a license master.
It acts as a centralized license repository for Splunk Enterprise licenses.
You can define license pools and stacks.
Monitoring console.
The monitoring console is a tool for viewing detailed topology and performance information for your
Splunk Enterprise deployment.
So pretty much it's kind of a dashboard so you can see and hear.
It actually provides an overview about your whole Splunk infrastructure.
So you can see here the performance, the health check of the search heads, the cluster master, the
deployment server, and the license master.
And of course, you can see the CPU performance, the memory usage, you know, if it's reached at a
certain threshold.
This is kind of like a dashboard, if you will.
You can actually deploy it separately in large scale environments or you can combine it with the cluster
master node with enough sufficient resources so it can handle the cluster master as well as the monitoring
console.
Now.
Let's jump ahead.
To the next, which is the Splunk Deployer.
So the deployer is a Splunk Enterprise instance that you use to distribute apps and certain other configuration
updates to the search at cluster members.
So think of it.
The Slug deployer is kind of the same as the Splunk deployment server, but the Splunk Deployer handles
search heads in a search hat cluster environment.
So this is pretty much the only difference that you need to know.
Now, of course, the deployer distributes what is so called configuration bundle.
Which is contains applications and configuration files to all of the different search head nodes which
are part of the search head cluster.
Now let's delete that and move to the next slide.
Splunk Cluster Master.
Now.
The cluster master is this one.
Now, this is a very interesting topic.
And it manages and regulates the functioning of indexers so that replicate external data so that they
maintain multiple copies of the data.
The Splunk Cluster master, it's pretty much helps to regulate the data, you know, which is going
to be flowing replication of the data between one indexer to the other.
So let's suppose one indexer goes down.
Now, it really promotes higher ability and disaster recovery.
So one if one goes down, the master cluster node will kind of do some processes in the background where
it's going to make that data available at all time, even if one of the indexes goes down.
So it pretty much avoids this.
What I would what I would call the single point of failure.
Now, if you remember in the last in the previous slide in our topology there we were having only one
indexer.
And one search head and different forwarders.
So if the indexer goes down, that's a single point of failure.
So pretty much the search head won't be able to send search requests to the indexer because this is
gone.
But with the master cluster node, it promotes higher ability and pretty much it replicates the data
which is here to here to here.
Now, if one goes down still, you have to that they're going to go through kind of a process which
is a replication process, and then the data would be searchable at all times.
