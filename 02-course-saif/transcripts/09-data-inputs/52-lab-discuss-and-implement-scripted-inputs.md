---
course: saif-admin
theme: 09-data-inputs
lecture: 52
lecture-title: "LAB:  Discuss and implement Scripted Inputs"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/09-data-inputs, transcript, kind/video]
---

# Lecture 52 — LAB:  Discuss and implement Scripted Inputs

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So in this section I'll be discussing the scripted inputs so Splunk can execute scripts based on a schedule
time, cron job, and of course indexed the output.
So let's go back to the universal folder.
Let me show you what kind of commands that we can actually schedule to be executed.
So first it's like PS minus F, you know, this is just to give you the internal processing, basically
the processes which are running on my Linux machine top, for instance, time uptime, you have different
OS level based commands.
So we can rely on these scripts so they can run on a scheduled interval on our end machines.
So on Splunk Base, there is a very good app where it offers really out of the box scripts that you
can actually rely on for testing purposes.
So just go ahead and install, download the Splunk, add on for Unix and Linux.
And I'll just break it down for you.
The directory structure.
So normally for a directory structure for the scripts, they live under the bin directory.
So all the scripts, they have to live under the bin and they have to be called from within the bin
directory.
So let me show you.
So let's go to this Splunk to for next.
And under the pen you can find all the different scripts, the shell scripts, where we can run these
voice commands for our Linux based distribution.
So for example interfaces, piece top to name, few.
So.
If we go back to our universal forwarder.
The way it has to be done is as follows.
So let's go to.
Let's see.
Apps.
We already have the app set up here, which is the you have base inputs now and here I have created
the bin directory.
And under the bin directory.
I have copied some of these scripts, so I've copied the common.
Of course, this is very important.
And I've copied that piece.
The top and the next stat.
So let me show you.
So.
Ellis H.
Ben.
So I have these three commands.
Of course.
Now for you guys, if you want to wonder what is the common.
This is pretty much to set the the global variable for some of.
So this is going to serve as an input for the net state of SRH and the SRH so they can run smoothly.
So how we would call these scripts.
So of course we will need to define that under the input scope.
So let's go ahead to the local.
Then sudo nano to the inputs dot com.
And as you can see here.
This is the stanza for the script and I'm calling the PS and I'm giving it an interval to run every
30 seconds and I'm assigning a source type of PS and a source of PS, and I am also sending whatever
is the output would be generated from running this script.
To be targeted for the Linux index.
Same with the top.
Same with net stat.
X.
Now to show you.
I have the bin directory and these are all the shell scripts where they have to live.
And under the local directory I have the inputs dot com where I'm going to be instructing to call the
scripts which are under the bin directory, which is exactly here.
So I have the bin and I have the default.
In our case, I have the local and here I have the inputs which it's going to call whatever scripts
that I have under the bin directory.
Now, remember, all the scripts under the bin has to be executable.
So let's show you that CD bit.
Of course they are executable.
So let's go to our search.
And let's find out.
So Linux.
I'm going to call it.
For the last 15 minutes.
And as you can see.
I am pretty much receiving logs from the executed command piece, top and Net stat.
Of course, this runs on a scheduled interval.
This is every 30 seconds.
This is every 60 seconds and this is every 60 seconds.
Now to show you as well, under the indexer, I've already copied as well the whole to.
And let me show you.
This is the to add on for Unix and Linux.
You can also have a representational view of all the commands which are part of this to.
So let's go to data inputs.
For the data inputs.
You scroll down to scripts.
And underneath the script just click on app.
And as you can see, these are all the different commands.
Which are part of the Splunk underscore to underscore NICS, which is this one.
And here shows under this column in terrible column shows you they are running on an interval of 60
seconds 360.
So this is a really good start where you can make use of some scripts which are offered in many tos
from Splunk Base.
And you can customize it to serve your purpose.
