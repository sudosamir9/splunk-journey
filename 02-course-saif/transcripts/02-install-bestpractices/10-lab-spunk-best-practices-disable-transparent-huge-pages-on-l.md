---
course: saif-admin
theme: 02-install-bestpractices
lecture: 10
lecture-title: "LAB:  Spunk Best Practices - Disable Transparent Huge Pages on Linux"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/02-install-bestpractices, transcript, kind/video]
---

# Lecture 10 — LAB:  Spunk Best Practices - Disable Transparent Huge Pages on Linux

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So we have successfully installed Splunk and now we need to jump ahead and do some post checklist.
So we've done some web navigation, post installation, server settings, server control.
We talked about those and now we will be talking about the best practices for configuring Linux.
And that means we will need to increase the limit settings and turn off transparent huge pages.
We already did the check Splunk status via CLI and also as a post installation Health check.
We will need to enable boot start.
So whenever we boot the Linux machine, Splunk will start automatically.
So guys, let's start now with the Linux server recommendations, which is to turn off transparent huge
pages and increase you limit settings.
So first things first, let me just show you what I mean by that.
So of course, I'm going to be providing all of these settings for you guys.
So this is pretty much what you need to do.
I've already prepared that.
Now.
It's a file which is disabled php.
Now if we can't that.
Disable THP You can see this is the same file.
So what are we going to be doing is.
We're going to go ahead to seed.
Actually, we are Splunk user, so let's exit and go to the root.
Now let's move to Etsy.
And then in it.
Dot d.
Under here.
Now, let me talk to you briefly about this.
So normally we can disable transparent huge pages, but they are not going to be persistent.
What I mean by that, if we go and cat.
Six.
Colonel.
I think it should be.
Mhm.
And then transparent pages.
And then we have enabled and you see, it's under my advice, it should be always under never that one.
And the defrag it should be.
Yeah.
So we need to change.
We need to write a script so we can change this by creating very small command, which is echo never,
you know.
And then.
It's going to be this.
So if we do it that way.
Actually like this.
So if we cat it again.
It's going to show as never, but this is not going to be persistent.
So if you do a reboot, it's going to come back to my device.
So how we do that now, we will need to create.
So via let's do it with nano.
So nano disable underscore thp.
So let's create that file.
Now what I'm going to do, I'm going to copy.
All of this.
And based it.
Let's make sure that the whole file is there.
Then control X and then Y.
Now I have a saved that.
So let's check again.
Disable.
Yeah, it's there.
What I'm going to do now?
Let's check.
The ownership.
And is it?
It's not executable yet.
So what we're going to do is.
Change.
Mode.
755.
Disabled thp.
Let's check again.
Because the file is executable now.
Actually, I cannot see that.
So let's do disable.
In fact, it is executable now.
Now.
This is for disabling the transparent huge pages.
I'm going to be providing you guys with this one.
Now, this is very important.
You need to take care of it.
Try to do it.
So it's very important.
