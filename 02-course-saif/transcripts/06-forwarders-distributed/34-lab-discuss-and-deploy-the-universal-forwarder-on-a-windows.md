---
course: saif-admin
theme: 06-forwarders-distributed
lecture: 34
lecture-title: "LAB: Discuss and deploy the Universal Forwarder on a windows machine"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/06-forwarders-distributed, transcript, kind/video]
---

# Lecture 34 — LAB: Discuss and deploy the Universal Forwarder on a windows machine

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

In the previous section, I have shown you how to install a universal folder and deploy it to the Linux
machine.
Then I have instructed this universal folder.
Through this configuration.
To monitor certain files, which are the secure one log and the secure log under the VAR log directory
and assign it to the index.
Equal security.
And then we have configured the universal forwarder to forward these logs.
Through Channel nine seven as a destination port to this Indexer IP address, which is this one.
Lastly.
We have configured this indexer to listen on this port 9997 for incoming traffic from the universal
forwarder.
And also we have configured the indexer and we have created the security index with these parameters.
Now we will go ahead and deploy the universal folder on my Windows machine and we're going to install
first, we're going to download from Splunk Base, the Windows App or ADD on, and we're going to deploy
it to this universal forwarder.
Then we will also deploy the add on windows on this indexer.
So we will take care of the parsing, field extraction, etc., as I will show you in a moment.
As a final step once we are done with this.
I will be configuring a search head and we will add this indexer.
Let me show you.
I will be adding this indexer.
As a search peer to the search hood.
So this the dedicated search head will enable us to search whatever logs that we have monitored from
the universal folder on the Linux machine and the universal folder deployed on the Windows machine to
retrieve those logs.
So let's jump ahead to the demo.
So let's click on Freezer Free Spunk.
I'm not logged in yet, so let's log in.
Yeah, I'm logged in already.
So let's go to resources.
Products.
So free trials and downloads.
Download a free trial 60 days for Splunk Enterprise.
Actually it is in the previous.
Web page.
Let's go to the end of the scroll down.
And this is the Splunk Universal Forwarder.
Let's download that.
So let's go to the window section.
I'm going to download the 64 bit.
So it enter.
Command line.
I'm going to take only the HTTP part.
Copy.
Paste it.
And I'm going to download it here.
So once the download is done.
I'm going to click on it.
I will run it.
This is going to show me this wizard.
So accept the license agreement.
They'll hit next.
Sign a user.
I'm going to create my own.
Go next.
Leave this for the moment.
We will talk about this in subsequent slides next.
This is the receiving indexer.
So we have to provide.
The IP address.
And also the listening port where this indexer is listening for incoming traffic.
So let's go back.
And.
Provide a dose of 10.10.
10.10.
9997.
Of course, you can change this whatever you want, depending on your infrastructure.
Next install.
Now, remember.
In real world scenario you'll need to take care of.
There aren't any firewalls in between, so you need to open the outbound port for 9997.
The other thing is we will need to create.
A Windows index as the next step.
So.
Let's wait for this to finish.
And then we can jump to the indexer and create a Windows index.
Why?
Because we want to collect.
The logs from this Windows machine where this universal forwarder and for these logs to the indexer
and of course we need to assign an index for the incoming traffic.
So let's wait for this to finish.
So we're almost done.
Almost through with the installation of the universal folder on my Windows machine.
So we're done with that.
Finish.
Let's jump in here and go to the local sea to show you where it has been installed under program files.
Then we go to Splunk.
Universal Forwarder lets it continue.
You see the directory structure of the Splunk software under the Windows machine, same as you know,
the one in Linux.
So we go under Etsy, under APS, and here we will deploy the.
A Windows add on in preparation to configure it so we can monitor the logs which are generated on my
Windows machine to forward those logs to the indexer.
First things first.
Now we have that installed.
What we can do.
We can go to services.
And then let me show you that from here you can see that the service or the process for Splunk Universal
Forwarder is running, which should be under.
So let's go further.
Splunk.
Universal forwarder.
There you go.
It's running.
Okay.
So let's jump back to here now.
Let's first examine if we're actually receiving anything from this universal forwarder.
And I'm talking about the internal logs from the universal forwarder to the indexer to examine that.
Let's jump ahead.
So let's go.
First, let me delete that.
Let's go to the indexer.
And let's go to search.
That's.
Check the internal locks.
And I'm going to put the last.
I would say 5 minutes search.
What I can do.
I'll type it.
Stats.
Count by host.
As you can see, this is the universal folder on my laptop machine, which I have just deployed to.
Of course, this is another universal forwarder.
This is a universal forwarder from the previous section.
Where we have deployed the universal forwarder on the Linux machine.
And this is how you can see that the universal folder on the Windows machine is up and running.
So let me just click that and view the events.
Of course.
I'm always putting no time range picker.
So these are the internal logs from the universal forwarder running on my Windows machine.
