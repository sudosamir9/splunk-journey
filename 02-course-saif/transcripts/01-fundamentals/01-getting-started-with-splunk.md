---
course: saif-admin
theme: 01-fundamentals
lecture: 1
lecture-title: "Getting started with Splunk"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/01-fundamentals, transcript, kind/video]
---

# Lecture 1 — Getting started with Splunk

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So in this section we will be talking about what does Splunk do?
But before we even try to answer that question, let me give you an idea and an overview about machine
generated data.
So what is that?
It's pretty much logs which are generated as a result of running processes and applications.
So let's take an example phone.
So when you switch on your phone and you switch it off, a log is generated giving information about
that action which has triggered that log.
Let's think about servers, desktop applications.
Any kind of electronic machine would generate such data.
Of course, when we take a look at this data, pretty much from the first glance, you would see that
it's pretty much unstructured, hard to understand and complex in nature.
And of course, remember, this kind of data would contain valuable information.
And it's generated in huge quantities.
Now, how does Splunk come into play?
Well, before we answer that question, let me give you an example.
So imagine you as a system administrator.
Normally your daily tasks would be to, you know, go through data.
The logs to try to find the root cause of the issue.
But if you see in here these kind of data, it's pretty much hard to understand.
And it might take you hours to pretty much find the root cause of the issue.
Now, how Splunk would come into play.
Well, Splunk will ingest any kind of data as an input.
You could think of JSON format logs, unstructured logs, pretty much traffic logs, anything that you
could think of.
It will parse those logs and to make something meaningful out of this data.
And then it will be stored into kind of an index or a database table.
And then you as a user will try to go ahead and through the queries to find your results.
Now, I'll give you another example from Take It from the Real World.
So there's a huge software company which has been using Splunk to ingest health care data taken from
their remotely located devices with sensors.
And then Splunk will try and go ahead and find any abnormal activity in this kind of data and then will
generate alerts based on these abnormalities.
Ultimately, these alerts will be sent to the user in a form of kind of a dashboard and KPIs giving
an idea or showing the performance of these pretty much devices.
So imagine how Splunk could be so powerful as a tool to help you analyze these huge quantities of data
from all of these devices and give you real time about what's happening behind the scene.
