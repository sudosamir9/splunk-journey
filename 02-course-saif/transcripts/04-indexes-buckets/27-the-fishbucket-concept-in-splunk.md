---
course: saif-admin
theme: 04-indexes-buckets
lecture: 27
lecture-title: "The Fishbucket Concept in Splunk"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/04-indexes-buckets, transcript, kind/video]
---

# Lecture 27 — The Fishbucket Concept in Splunk

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

In this section, we will be discussing the fish bucket concept.
So the fish bucket does exist with every single sunk instance, whether it's a universal forwarder or
an indexer.
Now think of the fish bucket for now as a pointer, a point of reference as to how far Splunk processor
has read into that file, which is being monitored.
Now, typically this happens in the real world scenario at the universal forwarder site.
So you're going to be deploying a universal forwarder at the end machine and then you're going to instruct
that universal forwarder to actually monitor certain files within that end machine and forward the data
back to the indexer.
So let's put this into action and expand on this concept a bit further.
So let me delete that and bring this to the front.
So imagine you have this file and you have instructed the Splunk Universal Forwarder to monitor this
file.
Now, by default, the Universal or the what I would call the Splunk monitoring processor.
Is going to read for every single file that's going to be instructed to be monitored is going to read
the first 256 bytes of this data, and then it's going to hash this data, the suppose this data.
256 and it's going to hash it what we call a C, r C hash, just a cyclic redundancy check.
Then the processor, the Splunk monitoring processor, is going to take this value and is going to compare
it against.
A database which is maintained by the fish bucket.
And typically this is the database where it's maintaining all the CRCs from all red files.
Now, if this CRC.
It does not exist into the fish bucket database.
That means that this file has never been read.
And then is going to instruct the processor, the monitoring processor, to go ahead and read into the
file.
Now, let's suppose we have read the file up to this point and this data.
Does not exist.
So in addition to the CRC, what is going to be maintained into this database?
It's what we call the Sikh address.
So how far the monitoring processor has read into the file.
And then also in addition to the Sikh called the Sikh address, we will also maintain a Sikh CRC, which
is going to be the fingerprint of the location of this last bite that has been read into the file.
All three values combined.
The CRC, the C address and the CRC is going to be maintained by the fish bucket.
Next time when we incoming data is being generated and read to this file.
So the Splunk monitoring processor is going to check again and see that the C address now or the value
of this is actually smaller than the size of the file being monitored.
That means that new data came in.
So that means that the bucket will instruct the Splunk monitoring processor again to start reading from
here, which is the C CRC.
Onwards.
And then this is the way on how we actually maintain the fish bucket through these values.
And then.
We will avoid, reread the data again and actually send it to the indexer, because this is ultimately
we're going to be avoiding having duplicates into the indexer.
Because that means that universal forwarder will always keep track of how long, how much data has been
read into the file.
Now, if you delete the fish bucket database, that means whatever file is there and you restart the
Splunk Universal folder, it's going to start reading all the files again, meaning having duplicates.
This command is pretty much used.
And we will put that into action.
So we will show you later.
And then we will actually reference the file path, which is being monitored.
And we're going to do a reset.
That means we're instructing the fish bucket to delete whatever values of CRC CRC address and the CRC
to be deleted from the fish bucket database.
So that means that the whole file will be read.
Another way that we can actually delete the whole fish bucket is using this command.
Now, first, before we even run this command, we need to first stop Splunk, run the above commands.
Either this one or this one, and then start Splunk again.
Now, this one will apply on the whole fish bucket while this one is going to be applied only for that
specific exe file, which is going to which is being monitored.
Also on the universal border, what you can do, you can go and delete the vol lips long fish bucket
directory using the R minus R, which is the recursive, and then that means you are just deleting the
whole fish bucket.
So before we move ahead, I will go ahead and create a demo for you guys and then we will apply all
this concept.
