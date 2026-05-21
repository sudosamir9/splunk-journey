---
course: saif-admin
theme: 04-indexes-buckets
lecture: 26
lecture-title: "Splunk Indexes: Backup and deletion"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/04-indexes-buckets, transcript, kind/video]
---

# Lecture 26 — Splunk Indexes: Backup and deletion

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

Now to recap.
Let's discuss these points, which are very important to us now.
Splunk back up deletion.
Now if you want to back up whole Splunk instance, first thing you need to take care of is to back up
the var lib splunk directory y because under the lib they will live your indexes.
Also, if you want, you can back back up everything under at C and to be more specific.
System local.
Because these are at the customize settings at the system level.
Like server name etc..
Users directory and apps directory.
Remember, hot buckets cannot be backed up unless you stop Splunk.
So when you restart Splunk, if you remember, that will trigger the hot buckets to actually roll to
warm buckets.
So remember.
This is very important to move an index stop Splunk process, then copy the index directory of your
choice, then start Splunk process again.
So stop Splunk process, copy the index, then start Splunk again, removing unwanted events already
ingested into the index by using the command delete.
So let me show you that.
So if you don't want if you want to delete certain.
Or everything under a specific index, what you can do.
So let's go to Splunk search.
There you go.
I'm going to delete a few things under the underscore internal, which are the internal logs of Splunk.
So sorry in.
Let me just zoom in.
What I'm going to do.
I'm going to first search for the last 24 hours.
There's going to be a lot of logs.
Take a look actually, for the last one hour.
Let's go do it for the last one hour.
So it's going to be a lot easier.
Now, if you see we have different source types, of course.
So what I'm going to do, I'm going to put a pipe.
Then delete.
Ed.
Uh huh.
So.
I think.
What is the error?
You don't have the capability to delete from the index, underscore internal.
I remember that's not possible.
So let's go then to a different index, maybe security.
I think I don't have anything as well under here.
Yeah.
So I don't have anything under the security.
Well, let's go ahead then and do a one shot upload of data.
So let's go ahead and show you how it's done.
So we go under settings data on the fly.
And let's upload some data to the security index.
So select file.
Let's go with secure.
We've just uploaded.
Now, remember, drop your data file here.
Maximum size is 500 and be.
So let's go next.
Now this is the data.
The raw data.
You see, it's already, you know, parsing the timestamp, which is good.
Of course, these are different things that we will be talking about at a later stage throughout the
course.
So let's go ahead and do next.
I'm going to put it under the admin course level.
This is a sauce type.
Well, actually, I can use the default or Linux.
Let me search if they have some pre configured out of the box.
Yeah.
We have Linux audit Linux secure.
Yeah, we have secure.
There you go.
No regular file existed.
This one.
That's fine.
So let's next.
There you go.
And then this is the host.
Let's put it under security index in here.
Let's review.
Now we have uploaded we've done the initial settings in terms of to which index this data is going to
go to and also define the source type, which is a preconfigured one of our terms bunk.
So let's start search the data.
Now, let me just.
Delete everything here.
Let's go to the index security, which is the one and we are searching old data.
So there you go.
We have the data.
Now, what I'm going to do.
Actually.
I have different sources, so I'm going to only delete this one so I could filter only on this one.
And then I will pipe it to the delete process.
So I'm not going to delete actually the entire index.
I'm only going to delete whatever I have filtered, which is the 9000 something.
So let's delete.
Voila.
So we have deleted those logs.
Note in here that this is not going to show when you search it, but they're going to be still there
into the index.
And they will actually be marked for deletion or they're going to go through the bucket life cycle until
it's age expired based on the retention policy that you've you've configured.
So let me just delete that part and just search this data.
Yeah, we don't have anything.
So let's delete this and go back to the security index.
And as you can notice.
Now we have only two sources instead of three previously that we had.
This is how to use the delete command.
So let's let's go back to the slides.
Of course, this is the part where we have discussed.
Also, you can run Splunk Clean Command.
This will delete the entire index, not recommend it.
Note If you don't specify index, all indexes will be deleted.
So let's go ahead.
And to Splunk Seelye.
And let's do.
I've been.
Splunk.
And then clean.
I think it was clean or something like that.
It was clean?
Yeah, it's lung clean.
And then if you don't if you're not sure about the command, let's hit help.
Splunk is not running.
That was not possible.
Status.
Yes.
Monk is running.
Let me just do help.
This is going to spit out all the different commands that we have.
So type help command.
So help clean.
So clean event data, and then we're going to use this one.
Of course.
We're going to delete index.
Security.
Minus F.
That's it.
No such file or directory.
How is that possible?
So.
Ah.
We need to put bin.
There you go.
We've got.
So in order to clean Splunk, they must not be running.
So.
Let's stop Splunk.
Failed.
Why is that?
Let's try again.
Authentication Complete.
Let's wait for Splunk to stop.
So it has stopped.
So now let's go and delete.
Yes.
Cleaning database security.
So let's start Splunk again.
Okay, So let's go back to Splunk.
Let's wait for the process to come up.
So now came up.
So let me search.
Nothing is there.
Why?
Because we have actually deleted the data.
