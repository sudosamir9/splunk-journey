---
course: saif-admin
theme: 10-capstone-lab
lecture: 55
lecture-title: "LAB: Introduction to AWS and Deploy Splunk Instances on AWS"
kind: video
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/10-capstone-lab, transcript, kind/video]
---

# Lecture 55 — LAB: Introduction to AWS and Deploy Splunk Instances on AWS

> Raw transcript. Notes go in `02-course-saif/notes/`, not here.

In the previous section, I have walked you through the different Splunk components as well as provided
an overview about the different use cases, as well as the data collection methods that we're going
to be implementing throughout this lab.
Now, in this section, however, instead of configuring and deploying the Splunk instances on my local
machine, however, we will be switching gears and rely on us to actually deploy our Splunk instances
in distributed architecture design.
So the reason why switching to a is it just that because in this specific lab, which is this one here,
we're going to be deploying a lot of Splunk instances.
So for the folks out there that you don't have enough hardware specs on your computers, I would highly
suggest to go ahead and create an account.
So let's actually go ahead and create a launch a server instance.
So I'm going to go ahead and click on launch instances.
And then for the sake of this demo, I'm going to just name my instance as Splunk demo.
Of course, I'm going to be choosing the Ubuntu flavor, which is my Linux based distribution.
Now if you see here, this is a free tier eligible.
So let's go through that.
Now this is an instance type of to dot micro.
So if we compare the instance types as well as the prices, you would see here that this is of type
micro that comes with one virtual CPU and one gigabyte of memory which could handle low to moderate
network performance at a price of 0.0116 US dollar per hour.
So you can actually deploy your whole Splunk environment and maybe keep it running for one day or two
days as soon as you're done with your lab and then you can just terminate all your Splunk instances.
So let's go ahead and choose this one.
Now, bear in mind that I'm choosing this one specifically for the universal forwarders and for the
intermediate forwarders, because if we go back to our hardware reference, which is in Splunk documentation,
this one.
So you'd see that the minimum specs for a universal folder is 1.5 gigahertz of CPU and a ram of 512
and B and a free disk space of five gigabyte, which specifically for this lab setup would be more than
enough.
So let's go back to our launching instance.
So in here, what I'm going to do, I'm going to set up a public key authentication for SSH.
So by creating this new key pair, it's going to enable me to log in to this instance via sage.
So let's go ahead and create a new key pair.
So I'm going to name it as well.
Splunk Demo.
Now I'm going to create this one.
And as soon as I create this one, I'm going to download the private key.
So let's go further with the network settings.
I'm going to leave it as it is.
I'm going to create a new security group.
Now, here, this will allow safe traffic from anywhere.
Of course, we don't want to do that because that means that we're going to be exposing our instance
to the whole Internet and we don't want to do that.
So let's keep it here as it is, and then we will go ahead and make the change in the next section by
creating a new security group.
So let's leave the configuration for the storage to a gigabyte, which is more than enough.
So let's launch the instance.
Now, this will take a bit of time.
As soon as that's done, then we will go ahead and open it.
So we have just created this Splunk demo.
And as you can see, it's still inside the build process.
So let's click on it for a moment and let's go through the basics of its network configuration.
Now, here, this is the public IP where AWS has assigned it to this instance.
So using this one is going to enable me to say to this instance, and this is actually the private IP
of this instance, and we will cover that more in depth later on.
Now, what is very much important for me is under security.
So under the security, we see that there are the inbound rules and the outbound rules.
And of course, by default, for the outbound rules, you mean that all the traffic leaving aggressing
your instance is going to the Internet and we're allowing that pretty much.
However, for the inbound rules, we will need to make sure that we restrict access to this instance.
So what we need to do is we need to go to security groups in here.
And let's go ahead and create a new security group.
So I'm going to name this as Splunk Demo instance group.
I'm just going to provide a meaningful kind of description.
So I'm just going to put SSH HTTPS and maybe Splunk Port.
Now I'm going to add in the inbound rules.
I'm going to add a new role.
So I would like to restrict access for S.H., not to everyone from the Internet, but only to me.
So what I'm going to do, I'm going to go ahead and I want to see what is the public IP of my ISP provider.
So I what is my IP address?
So this is actually the IP address.
So let me copy this one.
Let's go back to our.
Instance, let me just provide the Sidr block, which is a 32.
Now, let's add a new rule, and this one specifically to provide access for the web glory of this instance.
And if we go back to here, you can see according to this documentation, you will need to provide access
to Port 8000.
So you're you're able to access certain web.
So let's go back in here.
And also provide my public IP.
In your case, you need to provide your public IP IP address.
So let's add another rule.
I'm going to just add four for three.
Just in case we will need it later on.
And then also, I'm going to.
Allow all support.
80.
32 and I think we are done.
Maybe we will need to add other ports, but for now, let's keep it this way.
So let me just create this security group.
So now that we have just created the security group, let's go ahead and click on the instance that
we've just created.
Then we go to action and then we add the new security group.
So let's go ahead and add this new security group, which is this demo instance group.
So let's click on that one.
Let's add the security group, and this is the one.
Let's save it.
Once we are done, we can go back to security.
And we can see that we have added these new ones.
Now, take a look in here.
Of course, we don't want to have this one.
So what we need to do, we need to go back again.
And then delete this one.
So.
So let's go to action.
Let's go to Security change security group.
And then we will need to remove this one because this one was added during the configuration wizard.
So let's save this one.
So now that we have already set up the security group and we made sure that the open ports are only
restricted to be accessed from my public ISP provider IP address.
Now let's go ahead and connect to this instance.
So what I'm going to be doing, if you remember from previous section, what we've just discussed,
the creation of the public private key.
So basically I've downloaded the private key.
What I'm going to do, I'm just going to copy the content of this private key.
So I'm just going to copy this one.
Copy.
And then I'm going to go back to my Linux machine in here.
I'm going to do sudo.
No, no.
I'm going to name it.
Maybe private underscore key dot p m format.
Based it.
Control X.
Save it.
Now I have the private key.
I just copy it from here.
What I'm going to do.
I'm going to change the.
File permissions of this private underscore key dot p m format so sudo change modes to 400 and then
private underscore key.
Which is this one?
So let's go ahead and copy this one here.
So we go back, we paste it.
However, if you remember, we named our private key as.
Private underscore key.
PM.
And let's put sudo at the beginning.
Now that we have successfully connected to our AWS instance that we have just launched earlier.
Now you need to repeat the same steps again into configuring and deploying all the other Splunk instances,
which are part of our lab.
So spend some time to go ahead and repeat the same steps and create all of this in preparation for our
lab deployment.
