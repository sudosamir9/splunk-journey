---
course: saif-admin
theme: 02-install-bestpractices
lecture: 15
lecture-title: "LAB:  Spunk Best Practices - Post Installation Health Check"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/02-install-bestpractices, transcript, kind/video]
---

# Lecture 15 — LAB:  Spunk Best Practices - Post Installation Health Check

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So now, since we have rebooted and we have taken care of the PHP, which are the transparent huge pages,
this one, turn it off and then increase the you limit settings.
So let's go to the Splunk website and do actually some post, you know, installation health check through
the monitoring console.
So let's log in.
That's going to take some time.
So now what we're going to do, we go to settings monitoring console.
Now, remember, in the previous slides, we talked a bit about the monitoring console.
Now, this is the dashboard that we were I was mentioning previously.
Now.
Just to to give you a brief about it.
Now, the monitoring console, you can enable it.
You can deploy it as a standalone.
So let's hit on general setup from settings.
Now the mode is standalone, which means I am enabling the monitoring console for this instance only.
Now lets hit enter, edit, edit server log roles and now we are on license manager search head indexer
that should be OC, save it OC apply changes and then.
Let's hit refresh.
And then.
Let's go to the health check part.
So this is pretty much a comprehensive health check to support enterprise instances.
Now, let's start that.
Now, don't take a look at this one.
That should be okay.
It's not relevant.
Let's see if everything checks out.
Really good.
Now, of course, one or more oasis has returns, CPU or memory specific that fall below reference hardware
recommendations.
Now remember when we talked about that.
Now if we click on this results, you see that?
The minimum hardware specs.
You know, recommendation is 12 I'm using for physical memory is 12, and now I have currently eight.
So you really need to take care of this.
It's very important and you need to add her to the hardware specifications from Splunk.
Now I'm showing you this in real time.
Now let's check where are the best practices.
Take a look.
Assessment of server limits.
Successful because we've taken care of the you limit.
So we have increased that actually you can see now.
This is the current, this is the recommended, this is the current, this is the recommended.
So I've taken care of that.
Also, let's take a look at the transparent pages where it is.
There you go.
So transparent.
Each page is enabled is never and this one is also never.
You remember from the command line when we went ahead.
Let me just do cat.
System.
Col.
Mm.
Transparent then enabled.
Which is perfectly good, which means that the script that I've just, you know, created it is correct
and it took effect.
It actually, you know, it it's run basically under the Z in it, which is.
So when you reboot, there are different running levels.
You know there is from 0 to 6.
Also, this one is never so perfect.
Now we have a Splunk, you know, adhering to the Splunk best practices up and running and ready for
further deployment.
