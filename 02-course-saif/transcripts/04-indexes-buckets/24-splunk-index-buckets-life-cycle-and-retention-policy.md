---
course: saif-admin
theme: 04-indexes-buckets
lecture: 24
lecture-title: "Splunk Index - Buckets Life Cycle and Retention Policy"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/04-indexes-buckets, transcript, kind/video]
---

# Lecture 24 — Splunk Index - Buckets Life Cycle and Retention Policy

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So let's jump ahead to the next slide and discuss briefly all the factors that they're going to contribute
into the bucket life cycle.
So you remember when we talked about the data as it comes in?
It's going to be ingested, you know, and go through the license meter into the hot bucket.
Read, write, vote.
Remember, it's going to roll to warm.
When hot buckets reach maximum size or time or maximum hot buckets number.
So take a look at here.
These are the stanzas.
That you're going to be configuring under the indexes dot conf file.
So max buckets is equal to three.
So as data comes in, they're going to be written into hot buckets.
Now, if the data keeps on coming.
The oldest bucket, which is going to be marked.
So one, two and three buckets.
Now, the old as new bucket comes in.
Then the oldest one will move.
Roll to war.
Max hotspot in seconds.
This is pretty much the retention or the life for the hot bucket.
This is pretty much in seconds.
So once this is reached, Hot Pockets will also roll toward.
Now max data size.
So this is pretty much.
The the bucket size OC.
So once it's reached.
Like, for instance, this is A, 10,000 and B, it's a ten gigabytes.
So if data exceeds to this hot bucket, it's going to reach like 10,001.
Then this data will be rolled to warm again.
Now.
HomePod.
Max data size.
What is this?
This is the whole DB.
Directory, which is comprised of hot and warm.
So if this is exceeded.
Data will move directly to cold.
And if you remember from the previous slide.
If either of those are reached, then data is going to be marked for deletion or actually frozen unless
you have specified a thought path.
So the data will go into archive mode now.
Max Total data size and B, this is the size of the entire index.
The frozen time periods in seconds.
This is the the the time retention period of the whole index.
Hot, warm, cold combined of the whole index.
If it's going to be reached, like, for instance, think of the data that we talked about, which is
for the firewall logs.
So we wanted to keep them for 12 months.
So oldest as this data comes in, the older data, which is going to exceed 12 months, they're going
to be going ahead into frozen deletion.
Now, when you have the data under the warm.
Okay.
Let me just delete this and start again.
Warm will be moved to a different directory.
Maintaining the exact name as well.
Once you reach the maximum number of worm buckets by default, it's 300 here.
Once the data go into cold.
In a different directory.
And I will tell you why.
We want to keep the code into different directory.
A why this one into a separate directory in a moment.
So once we reach the CO, the data is stored into the cold buckets.
They're going to roll to frozen.
When cold TV directory size is reached.
This one.
Okay.
So why would we want to separate the code directory in one directory and those two into different directories
in one directory?
Now, the cold.
Maybe you want to keep this data to be searchable on a fast SSD disks.
While keeping all the data which is under the cold but no directory for slower or maybe network attached
disks like in a different place where they're going to be slower when you want to search older data.
This is very important because then this is part of the management of the disk and the indexes.
