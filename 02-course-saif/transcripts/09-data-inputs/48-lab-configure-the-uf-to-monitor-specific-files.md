---
course: saif-admin
theme: 09-data-inputs
lecture: 48
lecture-title: "LAB: Configure the UF to monitor specific files"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/09-data-inputs, transcript, kind/video]
---

# Lecture 48 — LAB: Configure the UF to monitor specific files

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

Since we just instructed the universal forwarder to monitor anything.
All the files and directories and subdirectories under the var log.
Well, that's not a good approach normally.
But what if we wanted to actually monitor specific directory?
Under the Apache, we have three more.
So what I'm going to do.
I'm just going to copy.
Var log server.
And I'm going to go to the input stock comp in this case.
So vi or actually sudo nano.
Opt splunk forwarder at c apps UDF local that inputs dot com and I'm going to change this.
Why is that?
It's not really saving that.
It's not wasting it.
So var log.
Let me remember if I'm getting that right.
Apache Dash web.
Server.
Let me just save that for a moment.
Is it Apache web server?
Yeah.
So var log.
By log Apache web server.
Let me make sure via log Apache web server.
Now I want to monitor actually these only whatever files or directories under the Apache.
I want to monitor that.
But since we've already ingested that and we can see it under here.
So what I'm going to do.
First.
I'm going to use the delete command to delete everything in here.
So I've deleted all the logs.
We don't have anything anymore.
But also, I need to remove the fish bucket in here.
So let me just first save that.
Let's go.
And stop the universal folder.
Been.
Splunk.
Stop.
Let's first stop it.
The sweet.
So we have stopped it now.
I'm going to cede to var.
It should be var lib Splunk.
And then there you go, the fish bucket.
So I'm just going to delete everything in the fish bucket.
So I'm just going to do remove minus r recursive fish bucket.
I just removed everything.
Why?
Because I want to re ingest the same data again.
Remember, we, we already monitored anything everything under.
Opt under var.
Log.
So we are not going to be able to ingest that again unless we clear the fish bucket.
And if you don't know, where's the fish bucket, please go through my previous slides so you'll understand
that.
So I want only to have the Apache Web server.
In this case, we've already configured the inputs dot com, you know, to have to monitor only at the
Apache web server.
So now, now that I've deleted pretty much the fish bucket, so I'm resetting everything.
So what I'm going to be doing now.
Let's make sure that we don't have anything.
What is this loss?
Yeah, this is fine.
So we can only also delete this.
That's fine.
And now?
Let's go back.
Index equal to Linux.
We have nothing.
So let's examine one more time.
What I'm going to be doing.
So.
No, no.
Let's see.
Apps u f and then local inputs dot com.
So I'm instructing the universal forwarder to monitor everything and the var log web server.
So.
Now let's start Splunk again.
Actually, it's already stopped.
We have to start it.
That's check status.
To make sure that it started.
Yeah.
And it is running.
OC.
So.
Let's see.
It's going to take a while.
Let's wait for for a few seconds.
So I've restarted the universal folder so that the configurations take effect that we just made.
Let's go to the index.
Linux and let's see what kind of logs now I'm having.
So let's go for all.
And in fact, if we go under the source, you can see that we are only now.
Monitoring, var log, Apache web server and all the subdirectories.
So this is exactly what we have done in this scenario.
