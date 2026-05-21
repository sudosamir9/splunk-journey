---
course: saif-admin
theme: 03-apps-configs-layering
lecture: 20
lecture-title: "Understand Splunk configuration Layering ( Global Context vs App/User Context )"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/03-apps-configs-layering, transcript, kind/video]
---

# Lecture 20 — Understand Splunk configuration Layering ( Global Context vs App/User Context )

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So you remember when we talked about the index context, which is anything that has to do, you know,
with background tasks like inputs, you know, parsing output, which is forwarding or just indexing.
This is regarded as the global context.
Now imagine you have multiple copies of the inputs dot com across different
directories.
Now for you folks.
If you don't know what is the inputs dot com file.
So let me just give you a brief about that.
So let me just go ahead.
And actually inputs dot com stock.
So let's go to the first one.
Now the inputs contains possible settings that you can use to configure inputs.
And what it means by that is the data input.
So when data is going to be sent, you know, the Splunk instance will receive it.
So this is regarded as the data input as the data comes in.
So let's move along and talk about it.
So normally under global context.
The final precedence or the highest priority is always.
Anything under the local directory, under the system directory.
So local.
Directory under the system directory.
Anything in here will be of highest precedence, number one.
Now.
As a number two.
The list is going to be at the app level.
So remember, always local beats default.
If you see here, this is one takes precedence.
And then when we go to the app level here, we are talking about this.
You see, always local takes precedence.
Now why Cisco Beats Firewall.
Why this is number two and this is three why this is not two over this one.
The reason why?
Because at the app level.
ASCII takes precedence.
And what I mean by that, the letter C takes precedence over the F.
So if you have multiple copies of inputs dot com across the different apps, you know, within the apps
directory, then the one which is going to take precedence.
Think of it like it's an ASCII, you know, order so A, B, C, D numbers take precedence over letters
and of course capital letters takes precedence over small letters.
So imagine if this was a capital F, So the precedence is going to be this one as a two instead of a
three.
So let's delete that.
So under local, we don't have anything.
So in here the host is taking is going to take precedence index as well.
Now let's go under.
Do we have any other local, any other inputs dot com, any other local directory.
Yes we have under the firewall.
So this is number three.
Now in here, of course, we have host But again, this one takes precedence over this one.
This one beats this one.
So it's going to take this one index as a.
Of course it does exist and it does conflict with this one.
But again, this one takes precedence.
But look, source type, we don't have it.
So that's going to be the union.
So this one is going to be added at merge time.
Disabled here doesn't exist.
Also, this one is going to be added.
Now, those two will be added here.
And then number three.
Now let's go through all the default if there are not going to be any other input conf files across
other apps, then we're going to go and circle through the default directories.
Now this is number four.
Under here.
We have hosts.
But of course, this one takes precedence over this one.
And although this one takes precedence over this one, but this one beats both of those index as well.
No, no, because we have a conflict.
This one takes precedence.
And this one as well.
They are already here because this one takes precedence over this one.
Now move on.
Number five.
We don't have anything but number six.
We have so.
This one actually does exist, but it never exists across all the other three, although this is the
last resort.
But there are no conflicts.
So this one is going to be also the union.
So remember, those two are going to be added.
And this one as well.
So at runtime.
We're going to have this, which is those two from here and those two from here.
And the last one, which is this one, because we don't have any conflict in other higher with a higher
priority.
Inputs dot com files.
So configuration files are always merged at runtime if there are any duplicates instances and I mean
by those.
Across different existent inputs.
Dotcom files, the highest precedence takes place.
One, two, three, always local by default.
And then if there are no conflicts, then it will be added as a union.
So this one.
And let's move on to the search type.
You remember we talked about we have so two contexts.
We have global contexts that we have explained and we have user contexts.
So let's go ahead and talk about the search time.
This is at the app user level.
For example, if you want to create a macros, you know IT field extraction field or what I would call
event that's going to reside under the fields dot com.
So or a search pretty much search time field extraction.
They're going to reside under the search time level in here same concept as within the index time level
or global level.
This time, this is not going to be the highest priority.
It's going to be the user where he's going to be residing under which app.
So let's suppose this is the user Tesla.
He's actually viewing the Cisco.
He's under the Cisco app.
So he's under the Cisco app, so he's under the app level, Cisco, so whatever is under local.
For example, it's going to take it's going to take precedence.
And then.
We moved to the app.
And the second highest priority is going to be Cisco.
Why Cisco?
Because the user Tesla, is under the Cisco app.
Then the third is not going to be like within the concept of local Beat's default.
No, this time it's at the app level.
So this is going to take precedence.
Then three defaults and then whatever app.
It's going to take also precedence number four, number five.
And this is going to be the last one.
But of course, within the system level, you know, local beats default.
Of course, also here within the same app level, of course, local will be the default.
But for example, the local from here is not going to beat default.
So think of it as.
If the user is going to be under the search instead of the Cisco.
So let me just do that this way.
Under the search, then this time this one is not going to be the second highest precedence.
Actually, this one is going to be the second highest.
This is going to be two and three.
And then for.
Two and three and then four and five.
And then, of course, always this is going to be the last.
