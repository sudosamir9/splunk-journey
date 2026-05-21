---
course: saif-admin
theme: 02-install-bestpractices
lecture: 5
lecture-title: "Splunk Deployment Prerequisites"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/02-install-bestpractices, transcript, kind/video]
---

# Lecture 5 — Splunk Deployment Prerequisites

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So we're going to go ahead and create an account on Splunk website.
So let's go ahead.
So.
You need to sign up if you don't have an account.
Fill in all the information in here and then agree to the terms and conditions and create an account.
In my case, I already have an account, so I'm just going to go ahead and log in.
That the username.
Password.
And then.
We're going to go ahead and click on Free Spunk.
Now Splunk offers two trial categories.
Either provision of Splunk Cloud platform, which gives you access for 14 days, or you can go ahead
with a Splunk Enterprise, which we were going to be doing, and download the 60 day trial version.
Now, it allows you to ingest 500 and B per day.
Now, as of this recording, it's 9.0.1, the Splunk Enterprise version.
Now, note isn't here that Splunk is supported by many OS platforms.
Windows with the CI Linux, different flavors start to tarball file and then the RPM for Red Hat and
DBM.
As well as macros.
Now I'm going to go to Linux.
And I'm going to install for the purpose of this demo.
I'm going to go with Target zip file.
Hate on that one.
Click on command line W get this is a command where you're going to be using to download Splunk.
Now, in case you don't have the W command.
So let's first jump ahead.
Zoom in.
In case you don't have the W command, what you can do is I'm a root now.
So apt.
Install.
Did you get?
I already have it, so it's fine.
Now, before we even download Splunk, I would recommend you guys.
Not to use the root account because Plunk recommends.
Not to use the root account, but a non root account.
So we will need to actually create a Splunk user.
So.
If you are not rude, you need to do it like sudo ad user and then this splunk account.
In my case, I'm already a root.
You.
And then I'm going to hit like that.
Already exists, so it should be okay.
Now, let me just go ahead and do a cat at sea password yet Splunk users there.
Once you create the user, then you need to hit password.
Splunk.
It's going to prompt you.
To enter a password.
And re enter that for verification.
So now we have the Splunk user.
Let's clear the screen.
Now, Splunk recommends to install Splunk package under OPT.
So let's go ahead.
And.
Copy.
That command.
Go back in here.
Ed.
So it's going to take a while.
To download the file.
So we're almost there another few seconds and it's going to be downloaded completely.
So let's wait.
Now that we have it downloaded, let's check.
So there you go.
The touch is that files there.
Now, notice that it's under root.
Root.
We need to change the ownership of that file.
So.
John.
Change ownership.
Splunk.
But then stuck.
Now let's see.
There you go.
Splunk and Splunk.
So let's switch to the Splunk user.
I am now a Splunk user, as you can see in here.
So seed.
I'm already under opt.
So what are we going to do?
Is.
To to.
And toward the file.
Minus exit to VF.
Just look.
So we are unzipping entering the Splunk package, the target set file.
Yeah.
Once it's done.
There you go.
So let's confirm now.
There you go.
We have the Splunk there now.
To run it.
Let's do.
So I'm already under the opt.
So I'm going to do Splunk.
Dot forward slash Splunk.
Then.
Splunk.
Start it.
Enter.
Press.
Q To go to the end of the file, you agree to the license?
Yes.
Put an administrator user, I'm going to name it Splunk.
And then please enter a password.
Any password that you desire.
Confirm that password.
I think I had I put it wrong.
No, it's it's correct.
Now it's running some check.
And you see here the 8000 port is the port for accessing the web.
So let's wait for this to happen.
And then we can go to ten.
Ten.
And then 8000.
So there you go.
We are here.
So let's log in.
And here we are.
We've just installed Splunk now.
Let's actually.
Give you a command where we can say so instead of start.
Status.
So this is going to show you the Splunk daemon is running and the Splunk Helpers as well.
Now, if you want to stop Splunk, you just hit stop.
But I'm not going to do that.
Then if you want to know more about the different commands, I think you hit help.
Yes.
And that's going to give you an idea about all the different commands that's there.
I'm going to also be.
Attaching a reference for all the different commands that from the CLI, you know, to have a better
idea about what you can do and what you can manage with this Splunk.
Now that we have installed Splunk right now.
So let me show you.
There is this command which is going to give you an overview about the different commands that you can
use to further administer Splunk.
And also what you can do.
You can go to the website here.
And under this section about CLL, I get help with CLI commands.
Now if you click on this one, right click.
These are also the different commands that you can be using.
Now, since Monk is up and running.
Now this is where we are.
Let's go and do some changes so you can go to the server settings.
Now under general settings.
This is the server name plus the master.
You can also change it the way you like it.
I'm going to name it Linux Demo.
This is the management Porche 8089.
Run Splunk web.
There's an option on the Gooey where you can actually disable Splunk web and you can also enable SSL.
You know you can as a best practice, you have to put as a yes.
Web port is 8000 app server ports.
Don't worry about the session.
Timeout is an hour.
Default hostname.
Let's name it.
Linux.
Demo now Pause Indexing.
If free disk space falls below 5000 in my case, because I have not much of disk space.
So this is an issue that is going to show as yellow.
Now, what I'm going to be doing, I'm going to decrease that 1000 so I can get rid of that yellow alert.
Let's save that.
Now that I've saved it.
It's going to ask me to actually restart from server controls.
So what I can do, I can go to settings again, server control.
That's going to take me to the restart Splunk Pane.
So let's click on that and hit.
Okay.
Now, let's wait a while.
Now, remember, guys, I have enabled the cell.
So that means.
I need to include HTTPS in the end.
So let's hit enter now.
Let's wait until Splunk comes up.
Let's verify if Splunk is already up or not.
Status.
So Splunk is running.
It in turn.
There you go.
Click on advance.
Proceed.
Their connection is not private.
Why?
It's not private?
Because it's a it's a self signed certificate.
So let's put Splunk.
The password and hit enter.
Now you can see.
Of course, certificate is not valid.
Because it's not signed by a co authority.
But you can see here, this is the certificate, which is a self signed certificate.
Now we are secured.
