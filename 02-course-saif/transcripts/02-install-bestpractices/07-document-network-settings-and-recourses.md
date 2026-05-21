---
course: saif-admin
theme: 02-install-bestpractices
lecture: 7
lecture-title: "Document - Network settings and recourses"
kind: document
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/02-install-bestpractices, transcript, kind/document]
---

# Lecture 7 — Document - Network settings and recourses

> **This is a document lecture, not a video.** On Udemy it contains links, commands, or written resources rather than a video transcript.

`[No transcript available for this lecture]`

---

Create Splunk Account and Splunk Install Commands for Linux



1. Splunk Website to download free Trail of Splunk Enterprise ( you need to create a Splunk Account First )



https://www.splunk.com/en_us/download/splunk-enterprise.html



2. Download Splunk Enterprise in Linux

Go to the Splunk Enterprise Downloads page above from your Splunk Account and get the wget command to download splunk package as I have shown you in the video.



Make sure to run the commands in your Linux ubuntu system

sudo apt update

then install wget command from the Linux repository

sudo apt install wget



to download Splunk, please use the command format below ( see video on how I walk you through that )



wget -O splunk-9.0.2-17e00c557dc1-Linux-x86_64.tgz "https://download.splunk.com/products/splunk/releases/9.0.2/linux/splunk-9.0.2-17e00c557dc1-Linux-x86_64.tgz"



3. create a Splunk user account as well



sudo adduser splunk



4. Install Splunk in Linux under the /opt directory



tar -xzvf splunk_package.tgz

where Splunk package above corresponds to your downloaded package name



5. Make sure to change ownership of the splunk directory



sudo chown splunk:splunk /opt



6. Start Splunk

sudo -u splunk /opt/splunk/bin/splunk start

