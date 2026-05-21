---
course: saif-admin
theme: 02-install-bestpractices
lecture: 9
lecture-title: "LAB: Deploy Splunk on a Linux Machine"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/02-install-bestpractices, transcript, kind/video]
---

# Lecture 9 — LAB: Deploy Splunk on a Linux Machine

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So we're going to go ahead and create an account on Splunk website.
So let's go ahead.
So you need to sign up if you don't have an account.
Fill in all the information in here and then agree to the terms and conditions and create an account.
In my case, I already have an account, so I'm just going to go ahead and log in.
That the username.
Password.
And then.
We're going to go ahead and click on Free Splunk.
Now Splunk offers two trial categories either provision of Splunk Cloud platform, which gives you access
for 14 days, or you can go ahead with a Splunk Enterprise, which we were going to be doing, and download
the 60 day trial version.
Now, it allows you to ingest 500 and B per day.
Now, as of this recording, it's 9.0.1, the Splunk Enterprise version.
Now, note isn't here that Splunk is supported by many OS platforms Windows with their MSCI Linux different
flavors that tarball file and then the RPM for Red Hat and DBM.
As well as Macross.
Now I'm going to go to Linux and I'm going to install for the purpose of this demo, I'm going to go
with Target zip file.
Hate on that one.
Click on command line W get this is a command where you're going to be using to download Splunk.
Now, in case you don't have the W command.
So let's first jump ahead.
Zoom in.
In case you don't have the W command, what you can do is I'm a root now.
So apt.
Install.
So you get.
I already have it, so it's fine.
Now, before we even download Splunk, I would recommend you guys.
Not to use the root account because PLUNK recommends not to use the route account but a non route account.
So we will need to actually create a Splunk user.
So.
If you are not rude, you need to do it like sudo ad user and then this bank account.
In my case I'm already route you and then I'm going to hit like that.
It already exists so it should be okay.
Now let me just go ahead and do a cat at C password yet splunk users there.
Once you create the user then you need to hit password Splunk.
It's going to prompt you.
To enter a password and re enter that for verification.
So now we have the Splunk user.
Let's clear the screen.
Now Splunk recommends to install Splunk package under opt.
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
That then stuck.
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
And Splunk.
So we are unzipping entering, you know, the Splunk package, the target set file.
The.
Once it's done.
There you go.
So let's confirm now.
There you go.
We have the Splunk there now.
To run it.
Let's do.
So I'm already under the opt.
So I'm going to do Splunk.
Dot forward slash Splunk, then Splunk.
Start.
Hit Enter Press.
Q To go to the end of the file.
You agree to the license?
Yes.
Put an administrator user, I'm going to name it Splunk.
And then please enter a password.
Any password that you desire.
Confirm that password.
I think I put it wrong.
No, it's.
It's correct.
Now it's running some check.
And you see here.
The 8000 port is the port for accessing the web.
So let's wait for this to happen.
And then we can go to ten Dark Ten.
Top ten.
And then 8000.
So there you go.
We are here.
So let's log in.
And here we are.
We've just installed Splunk now.
Let's actually.
Give you a command where we can see.
So instead of start.
Status.
So this is going to show you the Splunk daemon is running and the Splunk Helpers as well.
Now, if you want to stop Splunk, you just hit stop.
But I'm not going to do that.
Then if you want to know more about the different commands, I think you hit help.
Yes.
And that's going to give you an idea about all the different commands that's there.
I'm going to also be attaching a reference for all the different commands that from the CLI, you know,
to have a better idea about what you can do and what you can manage with the Splunk.
Now that we have installed Splunk right now.
So let me show you.
There is this command which is going to give you an overview about the different commands that you can
use to further administer Splunk.
And also what you can do.
You can go to the website here.
And under this section about I get help with CLI commands.
Now if you click on this one, right click.
These are also the different commands that you can be using.
Now, since Splunk is up and running, now this is where we are.
Let's go and do some changes.
So you can go to the server settings.
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
Default host name, let's name it Linux.
Demo.
Now Paul's indexing is free.
Disk space falls below 5000 in my case because I have not much of disk space.
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
I need to include HTTPS at the end.
So let's hit enter now.
Let's wait until Splunk comes up.
Let's verify if Splunk is already up or not.
Status.
So Splunk is running.
Hit enter.
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
Because it's not signed by authority.
But you can see here, this is the certificate, which is a self signed certificate.
Now we are secured.
