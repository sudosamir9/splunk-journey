---
course: saif-admin
theme: 04-indexes-buckets
lecture: 23
lecture-title: "Demo: Splunk Index's Structure"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/04-indexes-buckets, transcript, kind/video]
---

# Lecture 23 — Demo: Splunk Index's Structure

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So let's talk about the index structure.
Now, an index is comprised of buckets.
So typically when the data comes in, you know, into the indexer, it's going to go through the parsing
pipeline.
Once it's done, then this data is going to be marked to be written into disk.
So once the data comes in, you know, to be ingested, all the data is going to land into the hot buckets.
So what is the hot bucket?
The hot bucket from this name?
It's an read write mode.
So all the data, all the new data will come in and they will be marked, you know, for ingestion and
they're going to land into the hot bucket.
Now, the hot bucket.
We'll have the format hot underscore v one until like 2010 sorry underscore zero underscore one underscore
two to the RN.
Like that.
So let's talk briefly about the index structure.
In Splunk.
The index is comprised of buckets.
So think of it this way.
When the data comes in.
And it goes into the indexer.
So first it's going to go through the parsing pipeline.
And what I mean by that, you can pretty much parse the data, you can extract fields, etc. You're
going to create events.
So when this data is marked to be ingested or written to disk.
So they're going to go first, you know, into the bucket.
But of course, when they're going to go into the hot bucket, they're going to go through the license
meter.
Once they land into the hot bucket.
The hot bucket is kind of from its name.
It's a bucket where it is going to be in read and write mode.
This bucket is always listening, you know, and storing incoming data.
Data.
Would roll to warm.
Under certain conditions when some thresholds that you will be configuring under the Dexcom configuration
file, these certain thresholds, once they are reached, then the hot pockets or the data which is
in the hot Pockets, will roll to the warm.
The Hot pockets are of this format so hot underscore v one underscore zero one up to the end.
So when the data rolls to the warm.
The warm buckets are in read only mode and the name will change respectively for these buckets to this.
Now.
These data, which is going to be or this data when it's going to be into the warm buckets, they're
going to have this format name.
Take a special look.
Attention to these.
This is the epoch time for the earliest and the latest time for the data.
So as the data comes in from the heart to warm, they can roll.
This bucket will contain the earliest events.
With respect to this epoch time and the latest within this epoch time.
Remember when we talked about the search?
So let me show you.
So if we go in here.
Let me just delete this.
So when you search for a data, of course as a best practice, it's very important that you will include
a time range.
Now, this is will help this will help Splunk to actually go ahead and search into the right buckets
for fast retrieval process.
And what I mean by that?
Here.
By taking a look at all the timestamps within each bucket name within the worm.
Of course, warm buckets will roll to cold under certain, of course, satisfying certain thresholds
when they are reached.
We will talk about those in the next slides.
Remember?
The logs or the data when they are stored under the hot or the warm buckets.
All of this data going to be living under the DB directory, which is under the index name.
We will talk about this in a moment.
When the data rolls from warm to cold.
They get to maintain the same name.
Bucket name, but they will be stored into a separate directory called DB.
So let's take a see that into action.
So let's move ahead into here.
So this is the underscore internal DB directory where all the logs, internal processing logs are going
to live into this index name.
Now take a look.
Code.
Well, actually, let me just zoom in.
So we will see.
And this is the DB directory and the DB directory.
All the hot and warm buckets will live in.
Once they roll from hot, warm to cold, the data will be moved or the buckets they will be moved to
the cold DV.
Now let's go back.
To the previous slide.
And let's talk about once the data is in the cold directory or the cold buckets, you know, under that
cold DB directory.
Under certain thresholds.
The data will be moved to the frozen either to be marked for deletion or to be archived by default.
If you don't specify a thought path to archive the data, the data will go into the bin.
Now, when the data goes from cold or rolls from cold to frozen for deletion.
Under two conditions.
If the maximum size.
Of the index is reached.
Or if the retention policy has been reached.
And we will talk about this in a moment.
A slunk index.
Contains the raw data.
The exact raw data.
Which is compressed in that extension.
The test idea X Files.
Think of this as an index of the raw data, which is going to enable fast retrieval search.
And of course, the buckets and these are the buckets that we are talking about.
So.
Let's jump ahead.
To the next slide.
And talk about that.
So let me zoom out.
So.
Now going into the DB directory.
Here.
You can see that the TV directory will hold the warm and the hot pockets.
This is the hot bucket.
It's going to be in read.
And right mode, waiting for incoming data to come in.
And as the data ages or certain thresholds going to be met, the data will roll into warm buckets.
And these are the warm buckets.
Of course, when we when we go into each of these here, you will see that the hot bucket will contain
the side file.
Think of it.
This is like the index.
Of the actual raw data, which is also an index.
So this will help you.
To enable you to search the data.
So this will help Splunk to determine what fields or events you want to search.
Now, of course.
Once the data is ingested, you will have the meta fields, so host data sources and source type.
These are the meta fields which are very important to us.
Under the warm.
Bucket, it's pretty much the same.
You will have the side X, you will have the blue filter.
This is out of the scope of this admin course to a more advanced topic.
You have the houses, you have the sources and the source types and of course you have the raw data.
So I'll show you that in subsequent slides.
