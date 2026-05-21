---
course: saif-admin
theme: 06-forwarders-distributed
lecture: 31
lecture-title: "LAB: Discuss and deploy the Universal Forwarder on Linux"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/06-forwarders-distributed, transcript, kind/video]
---

# Lecture 31 — LAB: Discuss and deploy the Universal Forwarder on Linux

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So let's go ahead and install this universal forwarder.
But before that, let me show you.
I have provisioned this Windows machine.
Now, normally what I've done, I went into the wired settings from here and then.
On my Ethernet.
I have configured.
To manual and then entered the IP address that's mask and the gateway.
Now, this is one way to do it.
The other way where you can do.
So let's go ahead to the CLI.
What you can do.
Ludo.
I know.
See?
Net plan.
And then from here as well, you can configure the network settings.
Now for this purpose.
What you can use.
You can use it this way.
So let me show you.
I'll be providing that as well.
So you can configure it also via the CLI.
And then once you're done with this settings, then you can do sudo net plan apply.
So let's go ahead.
And first download the universal folder.
So in case you don't have an account, just go ahead and create and let's hit on free.
So from here.
Lets me log in for a moment.
Yeah.
Splunk Platform products.
Let's hit on free 60 days trial and know this is a Splunk Enterprise.
So let's go one step back and to the end of the pace call down.
Then you can see the Splunk universe of four.
Download it.
It's going to take you to the page where there are different flavors with all the supported OS platforms.
So let's go for Linux.
I'll be choosing the 64 bit.
This one.
And the RPA, the target set, file it on download now.
Copy the command.
And then let's go to the CLI of the provision Linux system.
So before we start, we need to make sure that you have a user.
In my case, I've already created that user, but let me show you.
So sudo ad user splunk.
It already does exist to make sure.
So pseudo cat see.
And then you can see that this is the user.
That I've just created.
Then.
Spunk recommends to download and install the universal folder under the opt.
Let's go ahead.
Copy that again.
Copy.
Based.
Pseudo.
So we are downloading now the file the package for one universal folder.
Once we are done.
It's root.
Root.
We need to make sure that we need to change this.
So zero.
John Slunk.
Splunk.
Then.
We thought you said file.
Think we we change that already.
So Splunk Splunk, now, the owner of this package is the user Splunk and the group Splunk.
Ooh, sudo tar minus x f.
Splunk.
So I think it has been installed.
All right.
And I'm tired.
So let's change.
File.
Ownership again, and this time with minus R.
So it's going to do a recursive.
Over all the files are directories inside the Splunk forwarder.
Hit enter.
Splunk.
Now let's switch to a Splunk user again.
So now what we do is see the to the Splunk Universal forwarder.
And do bin.
Splunk.
Start.
Hit queue.
Accept the license.
Create a user.
Then set a password.
Confirm the password by entering it.
Enter the password again.
Authentication complete.
So let's do Splunk.
Status it is running now, unlike the Splunk Enterprise, which is a full blown Splunk instance.
The universal folder does not have a UI, so pretty much you need to deal with it via the CLI.
So it is running up and running, but.
We have installed it.
Successfully on a Linux machine.
This is I'm using an open two machine in this case.
Now, bear in mind we've just installed it, but we didn't instruct the universal forwarder to monitor
no data and no forwarding to the indexer so far.
