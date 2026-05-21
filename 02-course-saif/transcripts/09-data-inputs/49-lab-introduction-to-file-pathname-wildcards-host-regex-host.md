---
course: saif-admin
theme: 09-data-inputs
lecture: 49
lecture-title: "LAB: Introduction to file pathname wildcards & host_regex & host_segment concept"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/09-data-inputs, transcript, kind/video]
---

# Lecture 49 — LAB: Introduction to file pathname wildcards & host_regex & host_segment concept

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So let's take another use case.
So let me just go back to the Universal Florida and let me show you.
So we are under the log with all the files and the directories where we have the logs.
And let's take this use case, a tree, Apache Web server.
Now, as you can see, we have.
Server one with all the logs which are access and secure.
Log under Apache, which is a subdirectory under Apache web server and we have the server two and the
server three directly under Apache web server.
Now I would like to only monitor server one, server two and server three with all the logs, regardless
of where server one on how many subdirectories it belongs to.
I would still want to monitor anything with server.
So how we can achieve that.
So we have something with Splunk where we can specify input paths based on wild cards.
And we have two basically controls or settings.
The first one is ellipsis.
So let me just show you that.
And this is a nice document.
So we have the ellipsis wildcard and we have the asterisk, you know, wild card.
So the ellipsis wild card searches recursively through directories and any number of levels of subdirectories.
And this is exactly what we want to achieve in here.
So server two us Server three lies beneath Apache web server directly.
But server one there are multi layers, you know, of directories or let's say there is still a sub
directory of Apache.
So how we can do that?
So when we use the three dots, we're actually doing a recursive over whatever subdirectories until
we re server one.
So let me show you that.
So let's go sudo actually without sudo.
So now I know splunk forwarder at C.
Apps.
And then.
Uff.
Which is our app that we've created local and that input stuff.
Now, as you can see in here, let's jump to this one.
So what I would like to do is I only want to monitor.
So let me just.
Show you that.
Opt.
Var look.
So let me bring this.
Apache Web server.
So I only want to monitor, for example, the access log.
And either.
So the star in here, the asterisk is pretty much a wild card.
So cert, which means several one.
Server two.
Server three.
And I only want to monitor access the lock underneath in this path.
But also I have included the three dots, which is the ellipsis.
So do a recursive until you find server star which is several one over to server three no matter how
many subdirectories you know along the path.
Search Server one.
So that means.
There is Apache still go 111 level down until you reach server one, Server two and server three.
And this is exactly what we want to do.
So let's delete first this one.
I don't need it.
And let's save that.
And now.
Let me make let's make sure we don't have anything in here.
We don't.
So I'm just going to do.
So KD upped.
Splunk.
Forwarder.
And then Ben Splunk.
We start or start.
I've already cleared the fish pocket, so let's restart it.
And let's wait for this to happen.
So what we have instructed the universal folder is to do a recursive search until you search and find
server one, server two, server three and only along the path find me the access to unlock.
So let's go ahead and search our index again.
Let's put it to all.
And voila, we found some logs.
So let's take and examine this.
So under the source, in fact, if we put this.
So let me just show you.
So where is it?
And here we can see that we're only.
Instructed the universal folder to monitor access to a log from server three server to and from server
one.
Take a look here.
Log Apache web server and Apache, which is exactly what we have done in here.
I would encourage you guys to go ahead to this website and it has a lot of different examples where
you can experiment and do some tests.
Now let's examine again the logs.
Now, as you can see here, the naming I don't want to include actually the whole path.
Maybe I want only to include server three, server two and server one, which is going to imply that
this these are the logs belonging to Server three.
So what we can do.
So there is another option.
What we can do is to add here, and I've already mentioned that before, which is host underscore segment.
Now what we can do is.
Now if I put number four in here.
And that means I will take as a host.
Only the fourth name into the path.
So let's examine this.
So for which means first, second, third and fourth.
But you will see in a moment why this is not going to work.
Well, because maybe it is good for server three and server server two and server three, but then we
will have Apache only along the path.
So let's do this change and I'll let you know what we can do.
So first let's delete the data again.
And by the way, notice this is host you.
So let's delete first the data.
So now we don't have anything in here.
Now let's clear the fish bucket.
So let's stop first the universal Florida.
And then let's wait for a second and then let's clear the fish bucket so we can be able to re index
and instruct the universal folder to look for those files again.
So let's clear the fish bucket.
By the way, this is a complete wipe of the whole fish bucket.
Let's start.
Spunk.
Universal Forward again.
Supply the password.
Done.
Let's wait for this to happen.
So it's going to take.
Sometime until the universal folder is going to go and look for a monitor, all of these files, and
put them into monitoring mode.
So let's search the data again.
So index equal to Linux.
And let's put all time.
And now.
As you can see.
We have assigned them.
The name Server three, Server two and Apache.
Because we have chosen host underscore segment to the nth name in the path along the path.
So that's exactly what we have done.
So let me show you again.
So host segment to be assigned is number four.
So along the path.
The fourth one would be.
And actually we can go to the inputs and show you what this that means.
So.
So control F.
Post underscore segment.
If set to end the next slunk platform sets the north separated segment of the path.
So it's the fourth portion of the path is going to be assigned.
But now we are facing another problem.
What if the server is on a different subdirectory?
And that's why we are having Apache in here and not server three or server one.
So let me show you that again.
So in here we have several one, but since it's the ninth or the fourth segment portion, so one, two,
three and four, which in fact we want the right one.
So how we can fix this?
Now there's another way where we can do is.
So let me first take this all.
And let me just go in here.
Actually, we have it already, but let me just delete this.
And then var log Apache web server server one.
And actually I can paste the other one and it was Apache then.
Server one.
Slash, whatever axis, dot log, etc..
So I'm going to change this to three.
So the other way, what we can do instead of host segment, we can do it with regex.
So host regex equal and I think we have it already in here.
So let me just find it.
So.
Host underscore regex.
There you go.
So if specified, a regular expression extracts the host from the path of that file.
Now you need to be familiar with regex how to use regex.
So I would put a link so you can get an idea on how to use regex because they are crucial to splunk.
So let's create a regex only to extract the server name.
So what we can do, we can do basically.
Um, this.
So how we can do that?
Because what we're going to do with this regex when we are setting this control is to go ahead and look
in here for whatever into the path and look only for the desired regex match.
So how we will do that?
So let me just skip.
This then let me put server and a backslash DD which means an a digit.
Then I will need to round this with a capturing group.
So it should be something similar to this.
So it's pretty much taking the CAPTCHA group.
Server three.
Server two and server one.
We copy this.
Then we paste it in here.
So let me save that.
And now.
We need gross to repeat this test again.
Delete.
We have deleted everything.
Let's stop.
Splunk.
Take it a moment.
Clear again.
The fish bucket.
Of course.
There's a command where you can specify to clear using the fish bucket for a specific file.
But for simplicity, I'm just going to delete the whole fish bucket directory.
There you go.
And I'm going to just start Splunk Universal, Florida again so we can instruct it to go ahead and monitor
those files again.
So let's see what's going to happen.
So let's face it again.
And do search.
Now it's 24 hours.
Let's put it all.
So, guys.
Take a look.
Let's see what's going to happen.
So did that change or not?
And yes, server one, server two and server three.
So we fixed that issue.
So what we have done.
We have used a regex match to go through.
You know, these are the paths that we want and we want to only extract a specific segment of that path.
And this is exactly what we have done and we have copied this and we've put it under house rejects.
So I really encourage you to go through this documentation in here and do some tests.
