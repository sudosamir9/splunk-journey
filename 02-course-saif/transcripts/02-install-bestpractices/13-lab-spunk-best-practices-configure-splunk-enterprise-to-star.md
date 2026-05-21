---
course: saif-admin
theme: 02-install-bestpractices
lecture: 13
lecture-title: "LAB:  Spunk Best Practices - Configure Splunk Enterprise to start at boot time"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/02-install-bestpractices, transcript, kind/video]
---

# Lecture 13 — LAB:  Spunk Best Practices - Configure Splunk Enterprise to start at boot time

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

Before we even reboot the machine, we need to enable the boot start.
So to enable the boat start, let's go to the website.
This is the website from Splunk Run Splunk Enterprise as a system D service.
So let's go further down and then search for That's the one.
So let me just copy all of this.
Copy.
And let's go back.
So I need to be rude.
So, KD.
Under opt so the user.
That I have configured is Splunk.
So.
Like this.
So opt Actually, I need to put Splunk as well in here.
So dot forward slash Splunk, then Splunk and Able Boot Start system D managed one, then the user Splunk.
Let's hit enter.
Please stop.
I need actually to stop Splunk first.
So let's first stop Splunk.
My bad.
So stop.
Now we're stopping Splunk.
It has been stopped.
So now let's run the command again.
So system D unit file installed and configured as system D managed service.
Now we can go ahead actually reboot the system.
So let's wait for the system to come up again and then we can take it from there.
Now that we have run a reboot into the system, let's log in again.
And see.
So let's now switch to.
So, Sue Splunk.
Let's provide the password.
Okay, so let's go to OPPT and now let's run.
Splunk.
Then Splunk status.
So let's see, did our configuration you know that enabled boot start will, you know take effect.
So we have actually restarted Splunk.
So when we hit this, that means that it should actually start Splunk as well upon rebooting the system.
Voila.
So Splunk is actually running.
