---
course: saif-admin
theme: 11-data-onboarding
lecture: 62
lecture-title: "LAB: Data Onboarding Overview and working with props.conf and transforms.conf"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/11-data-onboarding, transcript, kind/video]
---

# Lecture 62 — LAB: Data Onboarding Overview and working with props.conf and transforms.conf

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So now that we have deployed our Splunk environment in this lab successfully.
Now comes the interesting part, which is the data onboarding process.
You see the data onboarding workflow consists of few steps.
So let's jump ahead to our slides and let's discuss that briefly.
In the real world, whenever you're facing the customer, it's always good to ask the customer upfront
and let them prepare kind of a list of all the data sources that the customer wants to ingest.
So you can ask the customer, for instance, what is producing this data?
Is it an application and appliance?
And where is this data residing?
Is it a flat file?
Is it coming from a syslog feed?
Is this data being generated from a rest API?
Is it a database or simply maybe they want to monitor their windows and machines and then you want to
deploy the universal forwarders to these end machines?
So ask for more specific information such as let them prepare kind of like a sheet to put the data source
host names.
The IP addresses the path to this data, the location, the access information, and at a later stage,
maybe you could also ask them about the retention requirements, like how long this data needs to be
kept on the database.
So let's jump to our next slide and discuss that.
So again, gather information about the data sources, where is this data and kind of define the data
collection methodology.
So let's jump back to our lab diagram and discuss that.
So there are a lot of customers where they already have kind of a syslog server and they're actually
forwarding all their logs from their end machines like firewalls, proxies, etc., and they are being
collected in a centralized server.
So what you can do, you can actually deploy the universal forwarder or the heavy forwarder to this
centralized syslog server, and then you can instruct it to forward the logs to the indexing tier.
And this is exactly what we are simulating in here.
So now let's jump back to our slides and let's discuss the next point.
Now, once you have gathered information about the data to be ingested, it's always advised that you
go ahead on Splunk Base and check if there is a preexisting app or add on for that data.
This is going to make your life a lot easier.
And this is exactly what we're going to do throughout this lab.
Now, in case that you don't have any add on or an app for a specific data that the customer wants to
ingest, you can always revert back to the data pre viewer and use the props and transforms to get this
data parsed correctly.
And this is exactly what we're going to be doing.
So let's go to the next slide.
Things to remember.
Try to set the source type at the beginning.
It's always advised that in the input phase, try to configure the source type in case that you are
not able to define the source type, in case that you cannot define the source type, then you can always
use the props to do that job for you.
So basically you can put this control and the props dot com and you can define the path to the source
and then you can set a value for the source type, same as well for the host.
Now if the source type is set at the input phase, you cannot overwrite it in props.
So make sure you satisfy this requirement.
Now you can configure the source type with additional controls to get this data right at parsing phase,
like setting up the line, breaking the timestamp extraction, raw data manipulation and field extractions
and many more.
So let's identify the different controls in props dot com.
So here you have the should line merge.
So by default the should line merge is always set to true.
Now this should line merge when is set to true.
Splunk will combine several lines of data into one single event.
Now, in the real world and as a best practice, always set the should line.
Urge to false and let the line breaker do the job for you.
So you should actually rely on the line breaker in here to break your data into events because there's
a significant speed boost by using this line breaker instead of relying on the should line merge.
So turn this off.
Always advised.
Now we will use the time prefix.
So the time prefix is just the regular expression that is going to serve as a starting point to help
the Splunk software to extract the timestamp in that data.
Of course, the max timestamp look ahead is just to tell how much to look into the data for the timestamp extraction.
Now we will actually implement all of these controls in the prop stock conf in our next demo lab.
