---
course: saif-admin
theme: 11-data-onboarding
lecture: 67
lecture-title: "LAB: Manipulating the Data using SEDCMD in props.conf"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/11-data-onboarding, transcript, kind/video]
---

# Lecture 67 — LAB: Manipulating the Data using SEDCMD in props.conf

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So now there is one another command, which I think is useful, which is the z cmd command.
So let's create one.
So let's go back to our props dot com configuration and let's take a look at that.
Now this is the command set cmd.
And now it's used only at index time.
It's commonly used to anonymize incoming data at index time, such as credit cards, social security
numbers, etc..
Now the way we will create this control.
So let me show you that.
So let's go back to our search.
Now let's examine the data.
So, for instance, I would like to anonymize the first or mask the first part or the first half of
our source, Mac.
So how we would do that?
So let's go back to our CLI and do that together.
So the format would be something like.
Set seemed.
Let's give it a class name.
I'm going to call it maybe test.
Let's do equal.
Now the format is as follows.
So an SX for substitute.
And then here.
We will provide the regex match or the regex pattern.
And then we will replace it with something that we would like to anonymize so we can put here like a
replacement.
And then we can do backslash one, which is the capturing group.
And then a forward slash for a G, which means the global attribute.
So let's do that together.
Now, let me just copy.
One.
Sample event.
Let's copy it.
Let's go to RegEx.
Let's remove this.
Let's face it, and let's remove all of this.
Now the way to do it, I want to only substitute.
This first part.
With maybe exes.
So how can I do that?
So let's do.
So let me copy first this part.
Let me just baste it in here.
Now I have highlighted this regex match.
Now what I'm going to do and I'm going to put a backslash w.
And may be a plus.
Or actually what we can do, we can do as well.
Quantifier maybe of three.
Or that won't work.
Maybe what we can do, we can add.
This, and that means I'm going to do like this.
So basically, what does that mean?
If we highlight it, it matches a single character not present into the set.
So now I'm going to use this substitute the quantifier.
I'm going to put maybe two, three.
Four, Maybe five.
Actually, six.
Yeah.
So six.
Now I am, actually.
Matching all of this.
So now what I'm going to do.
I'm going to put a backslash w.
Or actually, I'm going to put.
To quotation marks.
Or maybe this one.
Then a dot a star.
And then maybe this one.
And then I'm going to put the two quotation marks.
So basically, now I'm doing a capturing group in here.
So I'm only defining this part.
So.
Now what I'm going to do, I'm just going to copy all of this.
So, Control C.
And let's go back to our Kelly.
I'm just going to paste it in here.
I'm actually going to remove this part.
To this point and now.
I'm going to put.
Or slash.
And then I'm just going to copy this substitute.
Or the replacement.
So I'm just going to copy maybe this part and based it in here.
And then I'm going to put like x x colon x x, colon x x, backslash one, a forward slash g.
So let me explain with this right X pattern.
I'm catching all of this piece or all of this portion.
And with this part, this is a capturing group which I'm keeping.
So this part.
And I want to replace everything which is here.
With this part, and I'm keeping whatever I'm capturing in here with the capturing group.
And leave it as it is.
So basically the end result will be the first part will be replaced with this.
But I'm keeping the second part because I'm putting the one which is referring to the capturing the
first capturing group here.
So let's save that.
And now what we need to do, we need to do a debug refresh.
So let's go back to our search.
So let's go back to here.
Let me just copy this part.
Control C paste it and let's do debug.
Refresh.
Actually, before I do debug refresh, I almost forgot to check if.
Yeah, it's still Splunk.
Splunk, which should be OC.
So now let's trigger the debug refresh.
Let's wait.
So now let's go back again and search our data.
Actually, it's not going to work because I need to delete the data.
And do it again.
So let's delete first the data.
Because it's at index time, it happens.
So we need to ingest the data again.
So let's add the data one more time.
So upload.
Select the file, which is the same sample logs.
So let's hit next.
Let's choose now the same source type that we've created earlier.
And it's showing it here.
Let's go for next.
Let's go with the main index again and let's do a preview and then submit.
So now let's wait for this to finish.
And then we can see if the masking of the data did happen correctly and successfully.
So let's start searching.
And as you can see now, actually, it has been anonymized.
So this is how you can use the set cmd control to actually anonymize your data.
I would encourage you to go under the props dot com and read more about this, but this is how it works.
Now, if we go back to our fields and under the source, Mac, you can see that now the data has been
anonymized.
So let me just recap one more time.
So basically the Z cmd, this is a Unix Z like syntax and it's used to search and replace.
So basically this is the flag substitution here.
Now this is the regex match.
So basically search for this pattern in your data and whatever you're going to place or put between
brackets.
This is going to be a capturing group which is going to be replaced by this flag.
So this is the regex match.
Again, this is the part where you want to substitute with.
So basically, whatever you're going to capture as the first portion substituted with this part and
this part is going to be referenced by the flag one.
So this flag one indicates the first capturing group, which is this one.
So it means that we are keeping this portion, but we are replacing this portion with this portion.
And this flag, this is a global.
