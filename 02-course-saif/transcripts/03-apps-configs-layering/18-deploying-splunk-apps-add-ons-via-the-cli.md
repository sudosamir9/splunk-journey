---
course: saif-admin
theme: 03-apps-configs-layering
lecture: 18
lecture-title: "Deploying Splunk Apps / Add-ons via the CLI"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/03-apps-configs-layering, transcript, kind/video]
---

# Lecture 18 — Deploying Splunk Apps / Add-ons via the CLI

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

I've shown you the first way to upload an app via the web.
Now let's see how we can do that via the CLI.
So I've already have those apps under.
So let's copy.
So let's copy the Cisco app and the Cisco add on which I've already uploaded them to the desktop so
it should be under home.
My username desktop.
And then it's Splunk.
Add on for Unix to opt.
Splunk.
At sea.
Apps.
Ask permission tonight.
I need to do it with pseudo.
This is the first one.
And this is should be the second one, which is called Cisco Networks.
Which is this one?
Where is it?
This one.
So let me just tap, tap and hit enter again.
So now.
We can see that these are both here.
So, but they are under route.
So what we do first.
Actually, let me do it differently.
So let's do sudo tar minus exit VRF.
Let's enter those two.
Add on.
I've untied the first one.
And this is the second one.
In fact.
The Cisco now is there as well as the where is it?
So this is the first one.
It should be called something with a.
Actually, I entered this one.
And I entered also this one.
So let's go ahead and change the ownership of those.
So sudo chon splunk.
User and then group Splunk minus R which is a recursive.
And then go for Cisco underscore.
iOS.
This is the first which is this one here, and then the second is the Splunk.
Actually, I'm just thinking of it.
I think I didn't antar it.
Actually, no, I did it.
I did it.
My bad.
So let's go ahead and do this one as well.
So Splunk then underscore to.
So now.
We can see that the Splunk tie for Linux Unix is under Splunk and Splunk, and the Cisco one is as well
as Splunk and Splunk.
So although we did enter both of them now, by the way, we can remove those two.
We don't need those two anymore.
So.
Sudo remove cisco dash networks and pseudo remove.
Splunk.
Dash.
Add on.
Now let's view it again.
Pretty much all night.
Now, although we have entered both, you know, app and add on one for Linux and one for the Cisco.
Still if we do refresh.
This is still at runtime.
I cannot find the one for Cisco.
So what we need to do, we either restart Splunk or we do debug refresh.
So if I do debug refresh now, let's refresh it.
Let's wait until this is done.
Reloading again, everything that we have here.
Now, if I do it, refresh one more time.
So control F Cisco.
There you go.
We have it again.
Let's move on to the next section.
