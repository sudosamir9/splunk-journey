---
course: saif-admin
theme: 06-forwarders-distributed
lecture: 32
lecture-title: "LAB: Configure the UF for monitoring input and forward the logs to the Indexer"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/06-forwarders-distributed, transcript, kind/video]
---

# Lecture 32 — LAB: Configure the UF for monitoring input and forward the logs to the Indexer

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So now that we are done pretty much with the Splunk Universal folder installation on this Linux machine,
let me let's go back to the diagram.
This is the diagram.
Let me just explain here a bit further.
So we have.
Deployed the universal forwarder.
Now, for the purpose of this demo, I would like to monitor certain files.
And send these files.
That's going to be monitored to the indexer, how we will achieve that.
So first, let's go back and show you the files that I would like to monitor.
So.
For the purpose of this demo.
I have these two files.
So I'm going to copy these files under the VAR log directory.
So let's go back.
To the next machine.
So let's go and move.
So let's Zullo move.
Home.
I count.
Desktop.
Secure.
I'm going to put.
STARR So that's going to be for both.
Those two, secure the log and secure one point log.
I'm going to be moving those to var.
Log.
So let's see.
Let's see to the var.
Lock.
So the log files are those, too.
Now you need to make sure.
Since you are running Splunk and also Forwarder with the Splunk user, it is very important to pay a
special attention to the owner of these two files if its true truth.
So Splunk won't be able to read them.
So make sure always to provide the correct.
Ownership for these two files.
So it's Splunk.
Splunk.
And in order to do that, you just need to do sudo.
John.
Splunk.
And then.
Put the file name.
This is.
What you need to do.
So.
There you go.
Once we are done with that and we know that these are the files that we want to monitor.
So let's go back.
To the desktop.
So I have prepared.
An app, which is this app.
That we will be copying this app.
To the Splunk forwarder under Etsy apps and then we will.
Work on creating the inputs dot com and the outputs dot com.
So if we go back to the.
Here you can see that we want to instruct the universal forwarder.
Through this configuration.
To monitor.
These files.
So this is the path.
Var log secure and then a star.
So this is a wild card.
So anything which starts with secure, you know, is going to monitor.
Now the disabled equal to zero.
So let me just zoom in.
The disabled equal to zero means that.
To activate this stanza.
So if you put to one that means is deactivated or disabled.
If you put one means that the disabled is pretty much on.
So you see the logic behind it.
When you put disabled to equal to zero, that means it's pretty much enabled.
Then we want to once we monitor these logs, we want to know and instruct the indexer as to where this
data is going to go.
And that's why we want this data to go to the index equal to security.
Now, bear in mind, when you put this index equal to whatever index, you need to make sure that that
index also exists under the indexer or where the logs are being forwarded to.
And we want to the source type to be Linux underscore secure.
Now the host segment equal to three.
So this is pretty much taking.
The third name and the subdirectory directory where you are pretty much more during the logs.
So let me show you that.
So if we go to inputs dot com.
So let me just first.
Delete this and let's search for host underscore segment.
What does it mean?
If a set to the end.
The Splunk platform sets the end with a forward slash separated segment of the path as host.
So, for example, if you set the host underscore segment equal to three, that means that whatever
the path which is going to be monitored is going to take the third one.
So that means it's.
Host zero eight, so one, two and the third.
Similarly, in our case, we are doing the same.
So what I'm doing in here, let me zoom in.
I'm putting the whole segment equal to three.
That means whatever the file name the ninth, which is going to be the third.
Take that as a name for the host.
In our case, we have secure one log and secure the log.
So when we get a monitor or instruct the universal forwarder to monitor these two files.
We're going to pretty much assign.
Secure one dot log as the host value and for the other file which is going to be only secure log is
going to be assigned as a host.
So I would encourage you to go through these to better understand the inputs and the associated parameters.
So let me show you that one more time.
So if you go, for example, and put disabled.
Whether or not the file system changed more to our input is active.
And that's exactly what I meant.
So if it's if you set it to zero, that means that whatever you have configured, it's active.
If you put it to one, that means that stanza that you have configured for the inputs dot com means
that it's deactivated.
Set a value of true to disable the input and false to enable it.
Default is false.
So let's go back and show you.
What else do we have?
This is the index.
This is the source type and this is the monitor.
So let's first start copying these settings.
So what I'm going to do.
I'm going to copy.
This is delete this part.
And go under our Kelly.
So let's move to CD.
Opt Splunk forwarder CD.
See.
Under here.
We have all of this.
I would encourage you to create an app.
Under the apps directory.
So I already created that for you guys.
So I'm just going to copy and paste it in here.
So this is just pretty much to know at which app level you are working.
So when you start to customize things and configurations for your universal forwarder or your Splunk
instance, it's always advised to create a separate app where you're going to be doing and manipulating
all the configurations so you know exactly at which level you're working.
So let's copy.
Pseudo copy.
Oh.
And then desktop.
Admin course then uff of course I need to put minus R in here.
So I'm going to copy the whole file.
To opt splunk forwarder at C apps.
So now if we do an LZ, I have that UDF base app that I've created.
Now.
Take a look at here.
We need to change this to Splunk.
Splunk?
Of course.
Otherwise, Splunk won't be able to actually read because of the ownership limitation.
It's Root and Splunk Universal Forwarder is running as would the user Splunk.
So let's do a CD to the UDF base.
Now, remember from the previous slides, normally you have local and default.
In this case, I only need to use the local because I'm doing a brand new app.
So this is my own customized app.
This is for metadata.
Now, for the metadata, we will be touching that briefly in subsequent slides, but for now I have
just created for you, so don't take a look at this one.
So let's see the two local.
And create pseudo nano inputs dot com.
I'm going to paste.
Think I didn't paste it right?
So let's paste that.
Copy.
Then go back to the Cly.
Yeah.
There you go.
Based it.
So I'm going to be monitoring.
I'm instructing the Splunk Universal forwarder.
This is the stanza.
Monitor Colon This is to instruct Splunk to read this file path.
Var log.
And then forward, slash, secure whatever files you have under the logs with the name secure with the
wild card is going to read it.
So for instance, if you're going to have secure one log, secure two dot log, secure three dot log.
Pretty much Splunk Universal Forwarder is going to read them.
This is disabled equal to zero means that read those files.
I mean, activate this stanza, which is the one core.
Then I'm going to be whatever I'm going to be monitoring under here, dump it into an index equal to
security.
And then assign it the source type of Linux secure, and then the host segment assign the host to be
the third the sub directory, which is going to be in this path following this path.
So first, second and third.
So let me just save it.
So we have now the inputs, of course.
Again, this is root.
So we need to take care of these.
So.
We have now configured the universal forwarder through the inputs dot com that we've just created.
Taking care of all of these parameters.
And this is the stanza monitor colon.
Now, if you don't know again, what does that mean?
Let's go back to inputs and search.
Four monitor colon.
Now, what does that stands for?
There you go.
So the monitor colon forward slash slash path to the file, configures a file monitor input to watch
all of these files you specify.
So always go back to the Splunk documentation.
It's pretty much easy to understand and write to the point.
So let's delete that and go back to our demo.
So we have done this part.
Now what we want to do is we want to construct this universal forwarder.
To send these logs, which we're going to be monitoring under the VAR log directory to forward to the
indexer.
How we will do that, Achieve that by configuring the outputs.
So let's go ahead and configure that.
Now, don't forget.
Once we are done with our app, we need to make sure that instead of root, we need to put it under
Splunk Splunk ownership.
So let's create first the output of.
So let's go ahead and copy.
This configuration file.
There you go.
Copy.
Let's go to our Kelly.
Now remember, we are under the local directory of that Splunk app.
So I know.
Outputs dot com.
Let me face that.
I think it didn't work.
Let me just copy it again.
But.
Paste.
So TCP output.
And now we're instructing the universal forwarder.
To forward all the logs.
To this IP address.
Now, remember, and this is the port that we're going to be setting as a destination port for that
server.
Now, remember one thing.
In order to do that.
You need to make sure that on the indexer.
You also setting the indexer on a listening mode on Port 9997.
Otherwise you're going to be sending those logs.
For a destination which and you don't have the ports opened, which is the indexer in this case.
Also in real life scenario, you might see that there might be some firewalls in between between those
two.
So you need to make sure to make a change request and talk to your customer if there are any firewalls
between.
So you will need to open the outbound traffic to the indexer by changing these settings or opening port,
which is 9997, I'm using 9997 as a default.
You can use whatever port you want.
So let's go back to our configuration and this is what we're going to be doing.
Let me save that.
So.
I've saved it.
So now.
We have the outputs dot com and we have the they have the inputs dot com and we have the output stock
of.
So.
Now.
This is ready.
What I'm going to be doing is Sudo chan minus Splunk.
Splunk minus R.
And then I'm going to be just putting the US.
So we've just changed the ownership of the file.
Whole file because we done recursive from root root to Splunk Splunk.
I'm not going to restart the universal forwarder now because I need to go.
First to the indexer and configure all of these.
