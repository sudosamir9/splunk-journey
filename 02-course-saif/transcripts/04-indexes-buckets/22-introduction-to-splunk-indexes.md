---
course: saif-admin
theme: 04-indexes-buckets
lecture: 22
lecture-title: "Introduction to Splunk Indexes"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/04-indexes-buckets, transcript, kind/video]
---

# Lecture 22 — Introduction to Splunk Indexes

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

In this section, we will be discussing Splunk indexes.
So what is an index?
It is simply a repository for data which is going to be stored in an indexer.
The Splunk instance is configured to index local and remote data.
Then the index data can be then searched through a search app.
Now, if you remember from the previous slides, I've already mentioned that the indexes would be living
under the var lib Splunk directory.
Splunk typically comes with preconfigured indexes.
So let's jump ahead and show you that.
So let's go to Splunk.
Settings.
Indexes.
Now let's discuss the ones of interest to us.
Let's start with the underscore internal Splunk indexes its own logs.
This is our result of the internal processing of the Splunk instance.
Everything will be stored underscore internal.
For example, Splunk data log logs, which are the daemon for Splunk process.
It's going to be stored under underscore internal.
Underscore audit.
This is where Splunk is going to store the audit trail logs, as well as any other optional auditing
information.
Moving ahead to the underscore introspection.
This is typically for system performance tracking like Splunk resource usage, how the data parsing
is performing.
Think of the CPU memory.
Everything that is related to the Splunk performance is going to be indexed under underscore introspection.
Now let's move to the underscore the fish bucket.
This contains checkpoint information for all the files that they're going to be monitored for data input.
Of course, this is pretty much going to be of relevance only for the forwarder, because if you remember,
the forwarders are going to be deployed on the end machines and you're going to instruct those forwarders
to monitor specific files under that instance and then they're going to be forwarding those logs to
the indexer.
But also don't forget that indexes also could be configured on a listening mode or to monitor specific
files.
So this is related to either the forwarder or the indexer.
Finally, let's talk about the main index.
The main index is the default index for data input.
And this is located under the default DB directory.
So some of you guys would ask, why would we want to create many indexes and not only one index?
And what I mean by that, when you want to ingest all kind of data into one index.
Well, fast search retrieval, what I mean by that.
So you will use Splunk typically to ingest all kinds of data from different sources like firewall proxy
logs, database logs, internal logs, windows logs, etc..
And imagine for a moment that you have all of these kind of logs into one index.
So when you want to search only for specific data type, let's think of like firewall logs.
So that means you actually putting some burden into Splunk to search all over all the data.
But if you would actually segregate your data types into different indexes, then you're not going to
put extra load on that Splunk instance to search through all the other indexes.
This means fast search retrieval.
This is pretty much imported when it comes also to retention.
So normally when you are upfront with the customer based on the customer's requirement and the data
importance, then you may want to ask them.
For how long you want to keep that data.
So let's go back.
And let me show you exactly what I mean.
So.
Typically you want to segregate your data based on on their type into different indexes.
So, for instance, we have the security index and here you will go for like authentication logs, security
level logs, pretty much processes, etc..
This is going to live under the security index now because of the, you know, the importance of these
kinds of logs.
For example, customer would want to keep this data for 12 months, whereas for transaction logs like
weblogs, normally customers would keep them for, you know, lower time range.
So pretty much maybe a three month retention period.
So that means you are better kind of managing your data size or the disk size.
And of course, this is going to rotate.
Now, imagine the firewall logs.
You want to keep them normally for six months.
So this is pretty much very important.
Why would you want to segregate your indexes based on the serving purpose?
So whether they are security logs, transaction logs, firewall logs, they can be employed with different
retention period based on the importance relevance of these logs in the eyes of the customer.
So let's go back to the slide and let me delete that one and then.
Access control.
Who?
Access what?
This is pretty much very important.
Because, for instance, you have the security group, you would want them to have access and to take
a look at the security logs under the security index.
But you don't want the other departments to take a look at this.
So this is part of the access control.
So then you as an administrator, based on the customer's policy, internal policy, you will want to
know which group is allowed to access and view what kind of data.
