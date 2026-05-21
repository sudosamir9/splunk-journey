---
course: saif-admin
theme: 11-data-onboarding
lecture: 65
lecture-title: "LAB: Use Data Preview to validate event creation during the parsing phase"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/11-data-onboarding, transcript, kind/video]
---

# Lecture 65 — LAB: Use Data Preview to validate event creation during the parsing phase

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So one of the most important steps of data onboarding is to get your data parse correctly.
And to do that, we can use the data viewer and Splunk web.
But before we do that, let me show you a sample of the data that we would like to parse.
So you can see here, this is the data.
And from the first glance, I can see that maybe we can use this part to get our timestamp extracted
correctly, or we can also use this part.
Also, if I take a deeper look into the data, I can see that this is a source IP.
This is the source MAC address.
This is the destination IP destination MAC address.
And I can see a lot of fields which could be of interest.
So I will show you how we can extract all these interesting fields.
So before we go and upload our sample data, what I tend to do normally is to create a new app context
where I can keep track of all the configurations that I'm going to be implementing.
So let's go ahead and create an app.
And then I'm going to call it Demo Dash Lab.
I'm going to name it as well.
Demo dash lab in here.
I never could have, and I'm going to put the version 1.0.0 visible.
Yes.
The author is me.
Let's save it.
So now that I have created it, it's showing in here.
So let's go ahead to our Splunk Web.
So let's go to Settings.
Add data.
Upload the data from here.
Let's select the file.
Lets upload our sample data.
So now we have uploaded the data and you can see it in here.
So let's break down for you the different controls that is going to help us into parsing this data correctly.
So let's start with the character set.
You can leave that to UTF eight by default.
Leave this one as it is, or we can just delete it.
Now, as previously mentioned, for the should line merge, it's always advised to set it to false.
Now we can rely on the line breaker in here, which is going to tell Splunk software where to break
the data into events.
So this is going to help us to define the event boundaries.
So if you go to this page under advanced, you can see here that this regex pattern help break the data
into an event for each line.
So let's copy some of this data.
Let's put it into our Rejects 101.
Now, let's go back in here and copy this Reg spatter.
And let's paste it in here.
Now, what we want to achieve in here is to break the data exactly at the end so we can start with a
new event.
So to do that, I would highly recommend to watch some videos out there for regular expression.
So what I'm going to do, I'm going to escape and I'm going to put square brackets and then another
escape, which is a backslash and then a double quote.
So you can see now that we are breaking exactly at the point where we want.
So this regex is going to help Splunk identifying the event boundaries.
So let's copy this one.
Let's go back in here.
Let's face it.
Now let's apply.
Raw and you can see it's raking down correctly.
Now, if I'm going to add just another double quote and applying here, you see now the data is not
parsed correctly.
So if I delete that and apply it again, you can see that Splunk is identifying where are the event
boundaries of the data.
So.
Let's go back and create a new control.
So if we go back to our slides in here, we can actually copy the time prefix.
So let's copy that.
Let's go back here and paste this control.
Now, the time prefix here, I want to actually tell Splunk where to start to look for the timestamp.
I'm not going to rely on this one.
I'm going to actually rely on this one.
So what we need to do, let's go back to our write checks in here.
Let's delete this part.
And I actually want to start to look for the timestamp starting from.
Here.
So I'm going to put.
A backslash.
That double quote.
Then time stamp, which is an exact match, a backslash and then a double quote, a backslash, and
then a colon.
Double colon.
And then another backslash.
And then double quotes.
So I'm just going to copy this one.
So now I'm telling Splunk to start looking for the time exactly at this point.
So let's go back to our data viewer.
Let me paste that.
So if I'm going to do apply settings.
You see.
So now we're telling Splunk to start looking for the timestamp starting from here.
Now let's create a new setting.
And let's go back to our slides.
And let's copy this one.
So let's face it in here.
Now, this works in conjunction with the time prefix.
So with this control, I want to tell Splunk on how long I want to look into the timestamp.
So these are four characters.
Five, six, seven, eight, nine, ten, 11, 12, 13, 14, 15, 16, 17, 18 and 19.
So let's put 20.
Now let's go back to our slide.
And I'm going to copy the time format.
So let's add a new control and paste it in here.
Now, the time format.
This is on how to format our timestamp.
So if we go back to this one, this is our.
These are the time variables that we can use to format our time stamp.
So to do that, let's check our timestamp here.
So this is a 2018.
That means we need to choose the year.
Format which should be something like.
Let's take a look.
Which is this one.
So let's copy this one.
So let's paste it in here.
Then I have a minus.
So let's put the minus.
And then the month is zero eight, which is August.
So let's go back in here.
So let's go under specifying the months which should be of this format.
So let's copy this one.
Let's go back to our data viewer.
Now, the day is 20, which should be of this format.
So let's first put the minus.
And let's go back to our.
Variables in here, so specifying days and weeks.
So for the day.
Is of this format, which is correct.
So let's copy this one.
Let's go back in here.
Let's paste it.
Let's take a look.
There is a T, capital T.
So let's copy that exactly as it is.
And in here you can see this piece or this portion.
It is the it's the hour, minute and second.
And this is the format.
So let's go back to our documentation here and let's take a look at the variables of the hour, minute
and second.
So if you see here, this is the hour, the 24 hour clock, which is from zero 0 to 23, which is exactly
what we want.
This is the 15.
So that means I'm going to copy this one.
Let's go back to our data viewer.
Let me just paste it.
There is a colon in here.
And then for the minute as well.
And for the second.
So let's copy the one for the minute, which is the decimal number from zero 0 to 59 format.
Let me copy that.
Let's go back to our data viewer.
There is another column.
So let's go back and check the seconds, which is also a decimal number.
Spent some time in here and identify all the different variables which are crucial to the time format.
So let's go back in here.
Let's paste it.
Let's apply the settings.
And as you can see, we are actually telling Splunk to look only for the first 20 characters or positions
starting from this point where we have used the time prefix.
So now that we have the data correctly set up.
Let's go ahead and save this source tape.
So I'm going to name this source type as demo dash lab.
Let's leave the description and then I'm going to change the app to the one that I've created earlier
throughout this lab, which is Demo Dash lab.
So let's save it.
So now that we have parsed this data correctly right now, let's go ahead and click on next.
Now I'm going to place it under the main index.
Let's preview.
Let's submit.
