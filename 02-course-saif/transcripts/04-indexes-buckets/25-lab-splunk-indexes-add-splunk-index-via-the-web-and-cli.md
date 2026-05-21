---
course: saif-admin
theme: 04-indexes-buckets
lecture: 25
lecture-title: "LAB: Splunk Indexes -  Add Splunk Index via the web and CLI"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/04-indexes-buckets, transcript, kind/video]
---

# Lecture 25 — LAB: Splunk Indexes -  Add Splunk Index via the web and CLI

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

We will actually add our first index.
Now, we will start with via the web and then via the CLI.
So we will put.
All of these into action.
So let me just go to Splunk.
Settings.
Indexes.
You can click on new index.
So let's name this index.
Security or actually I would call it firewall.
Cisco or Cisco Firewall?
Cisco Dash Firewall.
Now keep it on events.
This is the home path.
It's optional unless you want to specify it.
Cold path, thought path.
Now this is.
If you specify it, then data once it reached the frozen.
Then the data will be archived.
If you don't specify anything by default, it's empty.
That means the data will be marked for deletion once it reaches either the maximum total size of the
index or the time retention policy period.
So let me just delete this for a moment and come back.
So this is the maximum size of the entire index.
Let's keep it to 500.
Maximum size of what we cold buckets.
It's kept to order.
And.
Let's keep it under Cisco Network app level.
So let's save it.
And there you go.
We have the Cisco firewall has been created.
Now, of course, other than all the the preconfigured indexes, you can delete this index.
And if you see at the app level, it's under the Cisco iOS app level, you see current size, maximum
size.
There are no currently no events coming in.
And this is the path to the DB.
Directory.
And of course, it is enabled.
Obviously, you can actually also disable it if you want from the gooey.
Now to disable it, click on disable and then you can disable that.
Lets disable disable and it's marked as disabled.
And you can see that as disabled in here.
So we have created already an index via the web.
Now I'm going to go ahead and create an index via the CLI.
Now, before I actually create an index via the CLI, let's jump ahead to Splunk.
Let me show you something which I would typically do whenever I am with customers.
I would try to keep all my configurations that I will be doing in a separate app level, if you will.
So let me explain to you what I mean by that.
So you see here, there are different apps in here.
So let's go ahead under.
This list, click here.
This is going to go into the app management dashboard.
So I'm going to create an app.
So.
Let's give it a name.
Admin.
Course app.
Let's copy.
Let me just go.
So let's go ahead and create it again.
So admin.
Of course.
For control c.
Control V Now the version, this is an initial version, so I will do like 1.0.0.
Visible.
Yes.
Author.
That should be fine.
Let's save it.
Since we have saved it.
So I could see that should be here.
There you go.
So this is the app that I've just created.
Now sharing the app at the app level.
I'm going to go ahead and change that to Global.
So all system.
I'm going to put read everyone and write for power users and for admin users.
So let's say that I already have the admin user.
So let me show you.
What did I do exactly?
So let's go to the right, Seelye.
So now let's zoom in.
I'm now under OPI Splunk at C.
Apps.
Let me show you.
What did I just create?
So I created an app level.
Where I will be doing all the changes, like creating an index, for instance, which is the security
index.
Awesome.
So let's go into admin course.
And you can see by default when we create an app.
You're going to have the default directory and the local directory and remember from the previous slides.
Local takes precedence over defaults.
So the changes that I'm going to be doing is under the local.
So.
Now this is one way to create it.
Like the app from the web.
And then you're going to go ahead and create it radically another way.
What you can do, you need to make sure that you are under the right app.
So if you take a look in here, you're under app now.
If you go, for example, normally people will go under the search app.
So you see app search.
Search.
So if you go ahead and create an index from here.
So let me zoom out.
So it's going to be clear.
So if you go to settings indexes.
And you create an index in here.
Take a look.
Carefully at the URL, you're actually creating an index.
Under the search app.
So whatever you're going to change in here is going to go and land under the index, under the search
app level.
So let's let me show you that in action.
So security.
Let's keep everything optional.
You see it's under app search and reporting.
So let me save that.
Let me trigger a reload of what we've just changed or configure.
Let's go back to the Seelye.
Let me zoom in.
Now.
Let's go to the.
Search app.
Seed local.
Take a look here.
We've just created an index dotcom.
So let me just.
No, no.
Indexes.
You see.
So security has been created under.
The search.
Up level.
So you need to pay a special attention here whenever you want to create an app.
That's why a moment ago I was explaining to actually whenever you want to make some customization or
configuring something, create your own app from here.
Actually from here.
Let me show you again.
So on this one and then create your own app and then go to that app.
And then from there you can go to create whatever you need.
So you see here at the main course, this is the one that I've just created.
So let's go back to Search App.
And actually.
Um, let's go to indexes.
And you see this is the security that we've just created.
So what I'm going to do, I'm going to go to the ClA again.
And I'm actually going to delete everything in here.
So.
Control x.
Y.
So by the eye indexes, nothing is there.
I'm going to just reload the changes that I've done.
Now you see, this is the security.
I will do a refresh.
Still the security there because this did not finish yet.
So let's wait for the reload.
So everything all the changes will take effect in at runtime.
So it has finished.
Let's go back and do a refresh.
Security is gone right now.
So what I'm going to do instead now let's go ahead and create that index from the CLI, which is the
best way to do.
I've already created that index.
So what I'm going to do, let me just remove this index here.
So let me just copy again.
Opt Splunk.
Admin course.
Actually, I am at the wrong directory.
So let's.
So let's move to the admin course.
Local.
There you go.
I have the indexes in here, so let's view that.
So I have created now this index with the configuration.
Now this is the global DB directory variable.
Sorry.
So for this.
Now the default path for Splunk DB, which is the system variable, is opt Splunk.
Var lib.
Splunk.
So let me show you that.
So it should be opt splunk, var lib splunk.
Now if you want to change that, what you can do is.
You can go under here.
So let me just expand.
So.
Path is opt slung at sea and you can change the variable here.
So under Splunk dash launch dot com.
So let let me show you that in a moment.
So now I know.
Splunk.
Dash lunch.
So you see, these are the changes.
So what you can do, you can specify the Splunk, underscore DB into a different path.
Of course, you see, this is actually an example they have put.
So the default should be opt out.
Splunk var lib splunk.
This is giving you an example.
If by chance you want to change the directory, you know for where you want to store your data a.k.a
the indexes.
Normally customers they would want maybe to separate this into a different disk mounted to the Splunk
instance and network attach network as well.
Storage you can do that as well.
So it's really up to you in the end.
But by default it's opt in splunk, var lib splunk.
So let's.
Let's go out from here and go back to the main settings of setting up our security index.
So this is the stanza.
This is the cold path for the cold buckets.
You see, it's on a different directory.
This is the home path.
It's called the DB.
If you remember from the previous slides when I have mentioned those, so this is the cold and this
is the DB which is going to hold the warm and the hot buckets.
This is how you configure it.
And then this is for data integrity.
Check on the data that you're going to be indexing now.
Max total data size, this is 512 now, if you remember.
If we go back to.
Actually any.
Well, let's see this one, for example.
This is the max size of the entire index called warm.
Hot.
Everything.
This is the one.
So let's go back to the clay.
There you go.
Please go ahead and spend some time to read through all of these configurations.
I mean, the parameters, this is the home path for the max data size.
This is pretty much the warm, hot bucket.
This is the max data size, which is only for the hot pocket.
And of course, this is the thought and.
I have configured coal to frozen.
So if you remember from the pure slides when we talked about the.
So let me bring that slide to the front and I'll show you what I mean by that.
You remember when we talked about the data was going to roll from cold?
To frozen.
Now if it's under Frozen and you didn't configure any path for the archive by default, going to go
to bin.
Unless you configure.
An archive path and then the data is going to move not to thought, but it's going to move into archive
mode and then via the thought, you can actually restore the data back.
Remember, when the data is under thought, it's not going to be searchable.
Very important to remember.
So let's delete this and go back to our.
Let me show you.
There you go.
So this is the Max Hot buckets, which are five hot buckets and then frozen time periods in seconds.
Now, this is in seconds.
I think this would mean if you if you divide it by 24 and then by 30 by 3600, then it should give you
maybe I think, six years or something like that.
Not sure.
And this is bucket rebuild.
Don't don't pay special attention to this one.
You don't need to worry about this.
This is what we've just talked about.
The thought then this is compression, right?
Then delete hot buckets After restart, you start Splunk.
This is idle when the when there is nothing to be written into.
The hot buckets, then roll them to the next bucket, which is going to be the warm.
If you put to zero, then this is not going to be activated.
So pretty much these are the things that we're going to be doing.
So let me just.
Go ahead.
Make sure that the index is there.
Now, I will go back to my here.
I'm going to reload the configuration that I've just made.
Under the admin course app.
And now I'm going to do a refresh.
So it should appear.
There you go.
Take a look and take a look in here.
So let me just zoom out.
Actually, I forgot to do that.
So take a look in here.
This is the frozen path that I've just configured.
So data, when it's going to move from cold.
Normally by default is going to be marked for deletion unless you specify a frozen path.
So the data will go and to be archived.
So this is pretty much what we've just configured.
Now, take a look in here.
At what app level.
We've just created the security.
This is the layering that we talked in the beginning of this course.
So this is because.
I have created my indexes dot com under the admin course app.
This is very much important.
So now let's go back to the slides.
So we have added the index via the web.
Also via the CLI showed you the different parameters that are relevant to this course as well as shown
you the layering.
When you can create an app and then you can attribute those settings to that app level.
