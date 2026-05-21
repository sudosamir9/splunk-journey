---
course: saif-admin
theme: 09-data-inputs
lecture: 50
lecture-title: "LAB: Introduction to using whitelist to include files ( monitor inputs )"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/09-data-inputs, transcript, kind/video]
---

# Lecture 50 — LAB: Introduction to using whitelist to include files ( monitor inputs )

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So let's take another example.
So first, let me just.
Here's that.
And delete everything.
From my index.
So it's not searchable.
By the way, even if I use the delete command in here, that doesn't mean it's it's gone from the from
the index.
You need to go physically and delete the data as well.
So you can do the clear data, the clear index command.
So let's take another example.
So what if I would like.
To monitor.
Or whites list only the axis dot log in here.
So server three and server two.
Not this or the secure dot log.
Let's go with the secure dot log.
What can I do?
So.
That's first stop slunk.
And then.
Let's wait for a minute.
Then let's go and clear the fish bucket.
And let's go back to our.
Input stock of so.
I would like to monitor.
Only the secure log waitlist.
Only the secure log from server to and server three.
So what I can do.
So let me remove.
This.
Apache Web server.
Let's keep the star.
Well, actually, what I can do.
I can do it this way.
And then I want to remove the host's rejects.
And I want to put something different, which is white list.
And I want to white list only.
This secure log.
Or actually, I could take another example.
So do we have another example where we can use in this case?
Actually, I found something.
So I want to whitelist.
Only those.
Those.
How would I do that?
So first, let's go to the right directory.
So far log.
In this case, because we are under the var log.
As you can see, tree var log.
And then I want to list white list.
Only those.
So how I would do that.
So first let's copy those and let's go to our Rejects 101.
The space that.
So let's try to work that out.
So I will start with underscore.
Server.
Backslash D four digit.
And then.
Backslash at DOT because I'm escaping the dot.
And then a log.
And then I'll put a dollar sign, which is end of the file.
So what I can do here now?
I will just copy this.
So I'll just copy this.
And I will paste it.
And here.
But this is going to be only for monitoring purposes.
What if I want also to name the host according to the logs?
So if you remember what we can do, we can still use the host underscore regex.
So let's check that one more time.
So what we can do lets me remove everything from here and type Apache underscore.
Prot underscore.
And then I'm going to put capturing group.
Server.
Backslash.
I'll put a DD.
Or maybe a dot and a star.
But then I'll put a backslash dot.
And then log and then the dollar sign, which is end of the file.
So I'm capturing I'm just matching everything.
But as between these two, I'm just capturing the exact.
So I'm using a capturing group.
To only take the server one server to server three.
So this is a match.
And this is the exact group.
So let me just copy this.
I'm going to copy it.
I'm going to paste it in here.
Now.
I'm going to save that.
And let's start Splunk.
So let's wait for this to finish.
So to recap, I had to restart Splunk twice for this to take effect.
So let me recap with you guys what I've done.
So let's bring back that.
So under the var log monitor, var log, but only whitelist.
And this is a regex match.
Just go through the var log and find anything that matches this regex.
So in this case, it's going to match this one and then assign those with the host underscore regex
equal to this.
And the capturing group should be server one, server two server, whatever server number a digit.
So I'm taking this portion, you know, using the capturing group.
Again, I encourage you to go through the regex tutorials.
So let's go into the index.
And examine that.
So let's see.
So.
If we go to the source.
Exactly what we have done.
We have only.
White listed whatever is matching here.
So if we go back into the regex.
I'm matching those.
So monitor these files.
So this is what we are doing in here.
Whitelisting based on a regex match, which are those?
And then using the host regex.
And then extract server one.
Server two.
Server three.
Server four.
And this is exactly what we have done in here.
So you can see several one server two.
Server three.
Server four.
