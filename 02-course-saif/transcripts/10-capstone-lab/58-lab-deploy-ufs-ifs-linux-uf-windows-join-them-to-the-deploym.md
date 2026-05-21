---
course: saif-admin
theme: 10-capstone-lab
lecture: 58
lecture-title: "LAB: Deploy UFs, IFs (Linux), UF (Windows) & join them to the Deployment Server"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/10-capstone-lab, transcript, kind/video]
---

# Lecture 58 — LAB: Deploy UFs, IFs (Linux), UF (Windows) & join them to the Deployment Server

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

So in this section, I'm going to go ahead and deploy the intermediate forwarders as well as deploying
the universal forwarders.
So basically, if we go back to the diagram in here, I'm going to deploy these two intermediate forwarders
and these universal forwarders as well as I'm going to deploy the universal folder on my Windows machine.
At the same time, I'm going to deploy on all of these universal folders and intermediate folders,
the deployment client app.
So I get them to phone home back to the deployment server and I'm going to use this deployment server
as a centralized tool to configure all of these instances by deploying to them the apps, the add ons
and the custom apps that I'm going to be creating.
So let's jump ahead to my universal forwarders here.
For the sake of this lab, I'm going to configure one intermediate forwarder.
And you can actually follow the same steps to configure the other intermediate forwarder.
So let's click on this one.
Let's go ahead and connect.
I'm going to copy and then I'm going to go ahead paste it.
Let me just enlarge it.
Then I'm going to just change the private key.
So private.
Dot p m.
And of course, pseudo.
So now I'm logged in to the intermediate food one.
So let's go ahead and log in to Splunk so I can get to download the Universal folder package in here.
So let's go to Splunk.
Let's log in again.
And provide username.
Password.
And then we can go to products.
Free trials and downloads.
We scroll down to Universal to get my free download.
So on Linux, I'm going to download the 64 bit.
So this one.
So it's the target set file.
So let's download that one.
Just going to go to the command line and I'm just going to copy it from here.
So copy.
Let's go back to the CLI.
Nope.
Not this one.
This one.
So let's go see the opt.
So now I'm just going to paste it.
Do pseudo.
Hit.
Enter.
Downloaded.
There you go.
So let's untether it to minus exit.
VF Slunk.
That's on target.
So once we are done.
Let's check it.
We need to change the ownership.
So John minus are Splunk.
Splunk.
I've already created the Splunk user.
So So for the folks, you don't know how to do it.
So zoo dot ad user Splunk.
So if I do, it shows that I've already added it.
So now seed.
To Splunk.
And now Zoo zero minus you, Splunk.
Been.
Then.
Splunk.
Start.
Q Yes, provide the username.
You need to create a username and password.
There you go.
So now it is up and running.
We can verify that status.
So Splunk DX is running now.
At the same time, what I want to do.
I want this universal folder, which is the intermediate forward and here to actually phone home back
to my.
So let's go back to our diagram.
It's loading yet.
So I want this universal intermediate forwarder here to phone home back to the deployment server.
So to do that, I've already prepared an app.
So let's go to that app and let's copy paste the configurations.
So let's go to that one.
So the app is Demo Lab deployment client.
So what I'm going to do, I'm just going to rename.
Copy.
I'm going to go to my class.
So you can either skip that or you just can copy and paste it.
The choice is yours.
So seed to.
At sea.
Apps.
So here I'm going to create zero make directory.
Then I'm going to paste it.
And then I'm going to do local.
And I'm going to do meta data.
So.
I've already created this app.
Now we need to copy paste all the content.
So CD to demo.
Alice unless.
We have local and metadata.
So CD local.
And in here I'm going to go back to my app, which is this one under local.
I'm just going to.
Edit it.
And I'm just going to copy this and I'm going to go to my cle sudo nano.
And then I'm going to type deployment.
Client dot com if.
So let's hit enter.
Let's face it.
Of course, the target tree here.
You need to provide the IP address of your deployment server.
So let's go back to our deployment server in here under instances, and let's take the private IP address
of our deployment server.
So this would be the IP address.
So let me just copy that.
Let's go back to here.
Let's paste it.
Control X?
Yes.
It's going to phone home every 60 seconds.
So deployment client dot com was created.
One directory up.
Let's go to the metadata.
And then in here, I'm going to create the second configuration, which is the local matter.
So let's go back to our app.
This one.
And let's open this one and edit it with notepad Plus.
Plus.
By the way, I'm going to provide all these apps, you know, into the resources.
So.
Zero.
Nano Local Dot Metta.
Dot matter.
So base the configuration control x.
Save it.
Now.
We have created the demo Lab deployment client, which is referring to the phoning home interval of
one minute.
Now what you can do, you can copy this app basically to all of your other universal folders and intermediate
folders that you're going to have.
So let's first change the ownership of this directory.
So zero one minus our Splunk Splunk.
Then demo.
Now let's verify that test changed.
Now we're going to restart our universe, our intermediate folder in here, which is basically a universal
folder.
So let's do Sudo minus you Splunk.
And then.
Then Splunk.
Restart.
Let's wait for this to restart.
So once it's restarted, we can go back to our.
So let's go to our lab first and discuss that briefly.
So now I have configured the intermediate forwarder, number one, this one.
And also I've created, as I've shown you, the app.
So it's going to enable this intermediate folder one to phone home back to the deployment server.
So let's give it a moment.
And now let's go to the deployment server and access it via the Web and see if that intermediate folder
is actually showing under the deployment server.
So let's go to our instances and let's copy the public IP address so we can access that remotely.
So the deployment server is here.
Let's copy that.
Coach.
See?
Now.
8000.
Let's do HTTPS.
Yes.
Splunk.
And the password.
So now I have logged into my deployment server.
So let's go to settings for order management.
So now, as you can see now I can see the intermediate forwarder showing under the forwarder management.
So basically we were able to instruct.
This intermediate folder to phone home back to the deployment server.
And as you can see, it is showing under here.
This is the client.
Now, what you need to do, you need to repeat the same steps exactly to deploy the universal forwarder
package into your all other instances.
So basically, if we go back in here, you need to deploy it on your second intermediate forwarder,
on your universal forwarder here as well as here.
And then also what you need to do, need to go ahead and copy this demo lab deployment client to all
of your universal folders and the intermediate folder, except for the forwarder on the Windows machine,
which I'm going to be doing it right now.
So for the sake of this lab, go ahead, pause for a moment, finish the other universal folders and
intermediate forwarder too, and then resume that we can go ahead and deploy.
Now the universal folder on my Windows machine.
So now I have all my universal photos as well as the intermediate folders showing in here.
And I mean by that.
If we go to the diagram again, we have those two as well as those three.
Actually, I have Universal for the one, Universal for the two and I have a universal folder three
as well as another universal folder, which is the windows.
So what I'm going to do, I'm just going to delete this and I'm going to go back to my Windows machine.
So let's go first to download the universal folder for Windows.
So let's go to Universal folder.
Then windows.
I'm going to choose this one.
Now that's come online.
Actually, I'm downloading it here.
There you go.
Now, folks, make sure that you follow the same steps that I have shown you in creating and deploying
the app for the intermediate photo one.
Just replicate the same steps across the others.
So let's go ahead for the universal folder on my Windows machine.
Let's run it.
Now here checks the box to accept the license agreement on premises.
Next, going to provide a username.
Actually we can generate a random password that should be OC next.
Now here is showing me.
Do you have a deployment server?
Yes, I have a deployment server.
So what I'm going to do instead of providing the private IP of my deployment server, I need to provide
the public IP because this universal folder is on my local machine, whether these instances are on
the cloud on AWS.
So what I need to do is I need to go to the deployment server and copy this IP.
So let's go back to the configuration based it 8089.
Now bear in mind if you restart or reboot this deployment server instance, then this IP is going to
change.
So make sure that you don't restart or reboot.
Sorry, the deployment server instance.
Now of course 8089 next receiving index.
Don't do that.
Leave it as it is.
Let's go for next install.
Now.
Let's wait for this to install.
Now we need to know if my universal folder on my Windows machine can actually reach the deployment server.
So let's click on my deployment server and let's check the security group and see if I'm allowing access
from external or from the internet to my deployment server.
So I can see in here the inbound.
I'm allowing 8089 from anywhere on the internet, which should be OC.
So let's go back to our universal folder.
Let's do finish.
Let's go back to the forwarder management.
Let's do a refresh.
And now, in fact, I can see that from my local machine here.
I'm able to see it under the folder management under the deployment server.
So now that we are ready, we have now successfully done this part.
And also this part.
And we've also deployed the app so we can control the behavior of all these universal folders and intermediate
folders from one centralized location, which is the deployment server.
Now, if we go back actually to our deployment server and we expand, we can see that there are no apps
assigned to these intermediate folders as well as the universal folders.
