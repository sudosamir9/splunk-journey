---
course: saif-admin
theme: 11-data-onboarding
lecture: 68
lecture-title: "LAB: Manipulating Raw Data and how to mask the data using props and transforms"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/11-data-onboarding, transcript, kind/video]
---

# Lecture 68 — LAB: Manipulating Raw Data and how to mask the data using props and transforms

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So in this section, I would like to do another data manipulation, which is I would like, for instance.
To overwrite our meta field, which is the host.
So let's examine our data.
Now, I here, I have my data.
And maybe what I can do.
I can overwrite the host by the source IP address in each event.
So how we can do that?
So we can overwrite the host field here by the IP address of every single event with the help of props
dot com and transforms dot com.
So let's do that together.
Now let's go to our CLI in here and let's make those changes.
So let's do seed opt splunk at C.
Apps.
Let me do zu Splunk, provide the password.
And now I'm logged in as Splunk.
So let's go to our demo lab app seed to local.
And here I have my props dot com.
So I'm going to create.
Another control in the prop stock.
So let's do that together.
So props nano dot com.
So in here I'm going to reference the transform class.
So let me just do that.
So transforms Dash.
I'm going to call it maybe host underscore change.
Now I'm going to give it a name.
Host Underscore over.
Right.
Now, let's discuss that briefly by going to the Splunk documentation.
So let me just copy this for a second.
And let's go to the Transforms.
Actually to the props.
So control F.
Control V.
This is the one.
So the Transform dash class.
This is used for creating indexed fields.
So index time, field extraction.
This is a unique literal string that identifies the namespace of the field you are extracting.
So think of this class as an identifier to the transform set, while the transform stanza name which
is this one.
This is the name of your stanza from the transforms dot com.
So basically what we are doing we are referencing the the transform stanza name inside the props dot
com.
So we're going to go ahead and call it from the transforms dot com.
So let's go back to our CLI and let's make that clear.
So here this is the identifier for the transforms.
So think of this transform set as a way to call the function inside the transform scope.
So let's save that.
Now remember we have named the transforms stanza as a host underscore overwrite.
So let's go ahead and create the transforms.
So I have to declare first the stanza name where I'm going to be calling it from the props dot com and
this is the one so host overwrite.
And in here we have regex as a control, we have dest underscore key and we have the format.
Now I'm going to discuss those three briefly.
Now there is another one, but normally we don't declare it.
But I'm going to declare it for the sake of clarification, which is the source underscore key.
Now, if we don't declare it by default, is going to be set to the raw.
So basically this indicates which data stream to use as the source for the pattern matching.
So it pretty much means what is the data where I want to do the manipulation or the changes do?
And by default, it's the raw data.
So the regex, however, identifies the events from the source key.
That will be processed.
So basically this is think of it as a regex match that I'm going to match against whatever I have into
my raw data.
Now the destination key indicates where to write that change, which I'm going to be capturing through
their regex, through their regex pattern.
The format is how to write that regex.
So let's go now and do the regex for our data.
So if we go now to our search.
Let me copy some of the events.
Let's go to regex 101.
And now.
Let's create a regex pattern to actually get the source IP, which is this one.
So let's do that.
So I'm going to do backslash.
And I'm going to type source underscore IP and then another escape, which is the backslash, another
escape for the colon and another backslash for the two quotation, double quotation mark.
And now in here, what I'm going to do, I'm going to open a capturing group and I'm going to include
the first IP octet.
So minus D, which is a digit, and then the quantifier from 1 to 3.
And then I'm going to put a backslash and escape for the dot.
And then I'm going to copy this same pattern in here three times.
So paste a dot based at dot and paste.
Now, in here I have copied this and I'm going to end it with a backslash and a double quotation mark.
So basically now what I'm doing capturing what is inside.
So the IP address in here.
So I'm going to copy this regex pattern and I'm going to go back in here.
And I'm going to paste it under the control regex.
So let me just copy this one again.
So copy.
Let's go back to our cli paste it now.
The destination key.
This is since I want to do an overwrite of the host, so I need to include it this way.
Meta data, double colon and then host.
And the host indicates.
The host field.
This one because this is a metadata field.
Let's go back to the CLI.
Now the format would be host.
Double colon.
And then.
A dollar sign and one.
Now the dollar one indicates the first capturing group, which is this one.
So any regex pattern between brackets in here, that means this is going to become a capturing group.
So this is what we are doing basically.
So now what I'm going to do, I'm just going to do save it.
Let's make sure that it is Splunk.
Splunk.
So what I'm going to be doing now, I'm going to do a debug refresh.
Of course, this is not going to work because this is index time field extraction.
So I need to delete the data and do re injects the data again.
So debug refresh.
Let's wait for this to finish.
So the changes that we have done to the Transformers and to the props will take effect.
So now if I do a search.
This is not going to change because I will need to delete the data first.
And then I will need to ingest it again.
So let's do that together.
So add the data one more time.
Upload the data.
Select file the same sample logs.
Let's wait for it to finish.
Let's do next, let's select our source type, which is the demo lab.
Now.
Let's hit next.
Under the main index.
And let's submit the data.
So now it's being uploaded.
So let's start searching.
Of course there is nothing.
So let's only go to our index main.
Let's remove this part.
Let's hit enter.
Now we have actually overwritten our host, the previous one, with the IP address taken from here.
So this is a good way or a good example on how to do data manipulation.
Now, bear in mind that there was a mistake that I have done, and let me show you this.
So before I said to Colon instead, you need to put only one colon in here.
So thanks for watching.
