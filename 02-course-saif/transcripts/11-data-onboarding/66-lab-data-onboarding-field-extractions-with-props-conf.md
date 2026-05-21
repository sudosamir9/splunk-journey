---
course: saif-admin
theme: 11-data-onboarding
lecture: 66
lecture-title: "LAB: Data onboarding - field extractions with props.conf"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/11-data-onboarding, transcript, kind/video]
---

# Lecture 66 — LAB: Data onboarding - field extractions with props.conf

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

Let's wait for the data to be uploaded.
So now that I have identified the timestamp as well as the event boundary of this data and I have broken
it down into events.
Let's go ahead and click on Settings Fields so we can extract some fields of interest for us.
So let's click on field extraction.
And now I'm going to click on Open Field Extractor.
And I'm going to select the source type, which was Demo Lab.
If you remember.
Now I'm going to choose all time in here.
And I'm going to select a sample event, which is this one.
So let's go and click on next.
And I'm going to use the regular expression.
Let's click on next.
And now, if you remember previously, we have identified some fields which could be of interest to
us.
So let's examine this.
Now, this is the first field, which is source IP.
This is the IP address.
So let's highlight that.
Let's give it a field name, maybe source, underscore, IP, underscore, address.
Let's add that as an extraction.
So let's highlight this one, which is the source Mac address.
So I'm going to give it a name source underscore Mac address.
Let's add it as an extraction.
Now I'm going to choose as well this IP address with which is destination IP.
So let me see.
Let me just give it a name.
Destination underscore IP address.
Let's add it and then you can do the same for this one, which is Destination Mac address.
And let's add that as an extraction.
And maybe let's add another field, which could be.
Maybe the protocol type.
So let's add that.
As well.
So I'm going to call it protocol underscore.
Type underscore.
Maybe.
Maybe I'm going to call it proto underscore type because we have already here a protocol type.
So let's add it to the extraction process.
So now I have identified those five fields, What we can do.
We can also show the regular expression in here.
Now, what I would highly recommend, always double check this work.
Although Splunk is good in identifying and formulating for you the regular expressions in here, though,
it's better that you also do it yourself.
So.
Control C.
Let's paste it in here and you can see that we're actually getting a good match against all this data.
So always verify the work.
So now that we have extracted those fields from our sample data.
Let's go ahead and click next.
Let's now click next again.
And now this is going to live under my demo lap.
So as you can see here, I'm under the demo lap context, so let's finish that.
So now if we go to search and reporting and search our data, which is under the index equal to main.
Let's go under.
All, Let's.
Let's pick the old time time picker.
And you can see here that we are not seeing actually the fields that we have just extracted.
Why is that?
Let's go back to our projects and take a look.
So we have named it Source IP address.
We have name it as source Mac address, destination Mac, address pro two underscore type and the destination
IP address.
But I cannot actually find that.
Now, the reason why because this is under the search context.
And we have configured those field extractions under my demo lab context.
So let's click on the demo lab.
And under the demo lap context and because of these are regarded as search time field extraction.
So we need to make sure we go under the proper app context.
So let's go to our index main again.
Let's search for all time.
And now we can see that the fields are now showing destination IP address Destination Destination Mac
address source IP address Source Mac address and also the prototype.
So this is how it's done.
So now that we have passed our data and we have defined the event boundaries and we have also done the
time extraction and some field extractions as well.
Let's take a look at the props dot com and how it would look like.
So let's go ahead to our CLI and let's take a look at the props dot com.
Now you can see this is the source type.
Under the prop stock conf and this is the line breaker that we have defined the shoot line marriage
set to falls and this is the time format that we have configured and the time prefix.
And you can take a look as well at the extract, which is another control that's going to help us to
do some search time field extraction.
And you can see these are the different fields.
And if we go further, you can see as well all of the regex pattern and the capturing group for these
fields that we have defined in the web.
I will provide basically all of these configurations under the resources.
