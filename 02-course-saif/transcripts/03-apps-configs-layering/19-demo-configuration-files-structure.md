---
course: saif-admin
theme: 03-apps-configs-layering
lecture: 19
lecture-title: "Demo: Configuration Files structure"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/03-apps-configs-layering, transcript, kind/video]
---

# Lecture 19 — Demo: Configuration Files structure

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So in this section we will be talking about Splunk configuration files as well as Splunk Directory structure.
In this section, I would like you to pay a lot of attention to the concepts in here, because they're
going to be very much important for a successful Splunk deployment and ultimately for our demo lab,
which is theme for this entire course.
So let's start.
Now Splunk uses different configuration files, which going to determine the Splunk behavior or its
functionality.
Now, Splunk can have multiple copies of the same configuration file across different directories.
Now, first, let's talk about the directories which are of interest to us and which we're going to
be working with most of the time.
So let me bring that.
Let me just zoom in.
So let me just go up a bit further.
There you go.
So let's clear.
Okay.
So.
So let's go.
Seed.
Opt Splunk Etsy.
Now in here, the ones which are really of interest to us are normally the apps directory.
The system directory and the users directory.
Now, if you remember from the previous slide, we have deployed the Linux and the Cisco through the
web and through the CLI.
Pretty much those apps will reside under the apps directory.
So this directory will govern the apps configurations.
Now for this directory, which is the system directory is going to govern the system level, I mean
configurations.
And this is for the users.
Now.
To give you a better understanding of the file directory structure.
Let's jump ahead to the next slide.
Let me zoom out and talk briefly about this.
So this is where we where Salon.com.
I was mentioning it.
See, now we have here the user.
We have the apps.
And under the apps we have, for example, here, the search and the X, Y, Z apps.
I mean, whatever apps that you're going to be deploying under here and you have this system level which
are comprised of local and default directories, so pretty much under the user you will have local and
default under the apps.
You know, for every specific app that you're going to be deploying under the apps directory, you're
going to have also local and default.
Local and default.
Now, this is for the executables.
And this is the VAA directory.
Now, let's talk briefly about this one.
So under the world directory, the ones which are of interest for us is the VAR log Splunk.
Now, under the Splunk we will have the Splunk data log.
So these are pretty much the logs which are going to be the internal system level logs under Splunk
log.
So you're going to be troubleshooting, you know, so you're going to be looking at the Splunk log for
any troubleshooting, any issues that might arise with your system.
And this is also the audit log.
Now under the lib directory, this is where all the indexes, the data will be residing.
So let me show you actually that.
So let's just delete this.
Come back in here.
So city.
Actually, it's seed.
Var.
Lip.
Splunk.
Sorry CD opt.
Splunk.
Phar Lap.
Splunk.
So under here.
You can see we have the audit index.
We have the fish pocket.
We have the defaults.
All of these are offered of the box during the Splunk deployment.
Mostly are for the internal log of your Splunk instance.
For example, this is the fish bucket.
More to come in the next models, but take it as it is for now.
Now let's.
Go out from here and go to the log.
Splunk.
Now in here, the one which is of interest to us is the.
Splunk didn't log.
So if we do a cat.
Splunk dot log.
You can see in here, actually, these are all the logs, the internal system level logs of your Splunk
instance.
Now that we have talked briefly about the directory structure, let me show you actually the the configuration
file format that we have.
So let me just bring an example.
So you will see what I mean by that.
So.
Let's zoom in.
So.
A slung configuration file, again, as I've explained, governs specific behavior of Splunk functionality.
Now, normally the Splunk configuration files are configured.
With a dot conf extension now.
The the the Splunk configuration has stanzas, which are this one for example the general and the license
and think of these you know are like name value attribute kind of a format.
So for instance if you don't know what is the server dot com, this is the system level configuration
file which is going to govern the Splunk instance, whether, for example, you want to deploy a cluster
deployment, these are the changes where you're going to be doing in the server dot com.
But for now, let's take this example server name.
So if you don't know what is it, it's self-explanatory, but let me show you so you can just go to
server dot com and then under the general server configuration you can see that this is the name that
identifies this Splunk software instance to have a better understanding.
You know, this file contains settings and values to configure server options and server dot com.
So this is pretty much the format which is going to comprise of a stanza and under the stanza is going
to kind of have kind of like a name value, kind of a format.
Now you can change those directly under the server dot com or through the web.
But I would recommend to do it through the.
Directly on the configuration file.
Now, remember, the syntax here is always case sensitive.
So moving on, let's talk briefly about what we've just mentioned earlier.
So default.
And what I mean by defaults here.
Default should never be changed.
If you want to do some customization to your Splunk instance, always do it under the local directory.
Never under the default.
So let's go back.
So it may make modification under the local directory as it spreads, you know, supersedes the default
last resort.
Common used configuration files are props, dot com inputs, dot com output dot com server and transforms
dot com.
So mostly you're going to be working with these configuration files.
So I would encourage you guys to go ahead and take a look at those separately.
Now conf files are executed based on precedence, what does that mean?
Well, we will talk about that briefly in the subsequent slide.
Splunk configurations have to context.
Global Context Index time.
And user context app context, which is a search time.
Now think of the global context at index time.
Any configurations regarding indexing the data, forwarding it at search time, it's whenever you're
going to make some searches, etc..
So this is going to be governed.
Now, remember, at runtime, it merges all of them and create a single input.
Second of all, existing files directory.
What does that mean?
Remember when we talked about.
This one.
So basically this is the server dot com.
You could have multiple copies of the same configuration type, which is server dot com across.
For example, under the system, under apps, maybe searches, etc..
So at runtime it's going to merge all of the existing ones, but based on precedence.
Now.
We will talk about that as this is the core concept of Splunk layering.
