---
course: saif-admin
theme: 06-forwarders-distributed
lecture: 33
lecture-title: "LAB: Discuss and configure the Indexer for log receiving"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/06-forwarders-distributed, transcript, kind/video]
---

# Lecture 33 — LAB: Discuss and configure the Indexer for log receiving

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So in the previous section, we have configured the universal forwarder.
We have instructed the universal forward to monitor certain files, which is the secure log and the
secure one dot log.
And we also configure the output account to forward wherever we're going to be monitoring here to the
indexing tier.
In this section, however, first we will start to configure the indexer by first configuring it on
a listening mode.
So it's going to be listening on 9997 for incoming traffic from the universal forwarder.
But first, we're not going to enable this one.
We're going to keep it disabled so we can see the behavior when we don't have an index for the incoming
traffic from here.
So let's go ahead and first create this part and then we will forward the logs and then you will see
the error that on the indexer that you are receiving the logs for an undefined index.
But then we will, of course, create that index and then we will do that again.
So let's go and log in to the indexer and then configure the inputs dot com.
So we can make this indexer on to listen on 297.
So let me just delete that part.
So now I'm the indexer.
So let's go ahead and change that.
So I already have the admin course app created.
So I'm going to go see the local.
And then I'm going to go sudo nan.
I think I've already created that one.
So let me show you that.
So nano inputs dot com and pretty much what I've done, I just copied this part.
Into here.
Sorry, Not this one.
It should be the other one into here.
So I'm instructing the Splunk.
Indexer to listen for incoming traffic coming from the forwarder.
So this is the stanza which is Splunk TCP.
Now if you guys don't know, what is Splunk TCP.
So let's go ahead and search that.
Splunk.
TCP IP.
Receives receivers use this input stanza.
This is the same as the TCP stanza, except that the remote server is assumed to be a Splunk instance,
mostly like a forward.
You can still use TCP colon 4/4/ to activate the receiving site to listen on that whatever specific
port that you want to configure.
Also you can specify the remote server.
In my case, I'm not doing that.
It's optional.
So I'm using actually the Splunk TCP in this case, which I'm instructing the the indexer here.
That the incoming traffic is going to be expected from a universal forwarder.
So this is what I'm doing in here.
So let's delete that.
And let's go back to the Seelye.
So now.
So now that I've created it.
So let's go.
To Splunk.
Indexer.
It's.
Login.
What I'm going to do.
I'm going to do a debugger refresh.
Just so that we reload the new configuration which we have just created.
So this is done.
So now.
Let's confirm if the indexer is actually on listening on the Portugal nine seven.
So I'm going to do this minus an.
Sorry.
And then I'm going to grab.
Or 9997.
And you can see in here that yeah, it is listening on 9997.
So.
Let's log in to the universal four to the Splunk indexer.
And actually see if we have the index security because I've just disabled it now.
So we actually have it.
We still have it.
Let me check.
Actually, what I'm going to do is since I have already the indexes in here, I'm going to rename that.
So what I'm going to do, I'm going to do so.
Move the index's dot com to indexes dot.
Cons.
Something like that.
So this means that it's not going to be read from the Splunk instance.
So let's do a reload one more time.
Refresh.
Let's wait.
Then once it's done, I should expect that this is no more.
There.
Yeah.
So the security is not there.
Now, what are we going to do?
I'm going to go back to the diagram in here.
So we have already configured the universal forwarder through the inputs dot com to monitor the var
log.
Secure one and secure.
Log.
And we have instructed also the universal forwarder to forward the logs.
To the indexer and we only activate it now.
The Indexer on listening mode on 9997 based on the outputs here.
Now the index security is not enabled yet.
If you've seen, I've changed the configuration.
So I'm going to instruct the universal forwarder to follow the locks now and let's see what's going
to happen.
So that means delete that.
Let's go back to the normal Florida.
So let's do Zu slunk.
And now been Splunk.
Restart.
So authentication is complete.
Let's wait.
Put the password again.
Let's make sure that it has.
It is running.
So now let's go back to the indexer.
Let's do a refresh.
Let's wait.
So since we didn't configure the security index.
As you can see here, we have received an event for configure disabled or deleted index security, which
means if we go back to the.
Slide in here.
And you can see we have configured all of this and we have configured that the monitor logs to be sent
to the indexer and they Indexer is actually listening on this port.
And so we see that event.
However, we didn't configure the index.
That's why it gave us this error.
So to fix this problem.
So let's delete this to fix this problem.
What we need to do is.
We need to actually first enable the security index.
So what I'm going to be doing let's go back in here.
Let's go see.
Opt.
Splunk its C apps.
Admin.
Local.
I will just rename this one so it could be picked up by the slug processor and I will reload this configuration
so the security index will be shown again.
So let's go ahead.
I'm going to do move index to indexes dot com.
Let's view nano indexes.
You just know that.
Yeah.
Pittenger So this is the security index.
That I have created.
And let's cancel that.
Let's reload.
So those go back to here and do a refresh.
And let's make sure that the actually the index is going to be shown in here.
And in fact, it's here, as you can see.
There you go.
So.
Now we're back to the index equals security.
And as you can see, I'm trying to find.
The logs because it was showing this error in here.
So let's go back to our.
Architecture in here.
So you remember we already configured that the logs has been sent to the indexer, but we cannot see
any logs.
So here, what are we going to do?
So because we send the logs and we didn't have the security index in here configured and I mean by this
one.
So the data has been lost.
So here what we're going to do, I'm going to do I'm going to clear the fish bucket on the universal
forwarder to trigger this universal forwarder to ingest the the logs again.
So what I mean by that, let's clear this and let's go to the universal forwarder.
So let's zoom in.
So city.
So let's go and show you actually that.
So I'm going to do ls.
L h.
Bar.
The Splunk.
Fish bucket.
You see, this is the fish bucket that I was mentioning before slides.
And you see, these are actually think of it, it's kind of like a database that's going to maintain
all the classes as well as the data seek and the CRC seek for the monitored files.
And as you know, we have three files.
We're actually two secure, one secure and lock.
And because we've already forwarded these logs and had been already read by the Splunk processor.
But we have lost them because we didn't have a security index.
So when we're going to be deleting.
This data.
Then we will force the Splunk processor to re index whatever we have configured into the inputs dot
com to monitor those specific files.
So let's go back to the slide and let me show you what I mean by that.
So this is the fish fish bucket.
So what I'm going to do.
I'm going to actually take this one.
Let's copy this one.
Let's go back in here.
First, I will need to stop.
So let's stop Splunk.
So, Ben.
Splunk.
Stop.
Let's wait for it to stop the process that I'm going to paste.
I think I didn't paste it right.
So let me try to paste it again.
Copy.
Index.
Clear in the fish bucket.
So let me just hit.
Put a pen bin.
Yes.
Jimena is not supported on this version.
Oh, okay.
So what we need to do is, is to actually just to use the remove.
So what we can do is.
Remove minus R.
And then I'm going to do opt.
Splunk.
Forwarder.
Bar lip.
Splunk.
And then fish bucket to remove everything.
Now let's start Splunk again.
I am on the University of Florida.
So let's see if it is running.
It is.
Now let's examine the fish bucket.
If it has been recreated again.
So this blunt border bar lip.
Splunk.
Yeah.
There you go.
Fish bucket.
It has been recreated.
So now the Splunk processor will go ahead and reread these files.
And because we didn't have when we deleted the the database, which is the fish bucket database, which
is going to be maintaining the CRCs.
And since we have deleted that, so as a first step, it's going to create a CRC for all the monitored
files and is going to compare to an empty database.
So that is what is going to trigger the re of all of the monitored files.
So if we go back to Splunk.
Let's give it a moment.
It's going to take a while.
Like maybe a few seconds.
So notice now we are reading the files again.
So let's go back to our lab.
So we have configured this.
We have configured this with this.
Now, as a final step, we will add the search head.
As part of the distributed architecture.
