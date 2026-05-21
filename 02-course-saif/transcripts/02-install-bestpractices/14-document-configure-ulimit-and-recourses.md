---
course: saif-admin
theme: 02-install-bestpractices
lecture: 14
lecture-title: "Document - configure Ulimit and recourses"
kind: document
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/02-install-bestpractices, transcript, kind/document]
---

# Lecture 14 — Document - configure Ulimit and recourses

> **This is a document lecture, not a video.** On Udemy it contains links, commands, or written resources rather than a video transcript.

`[No transcript available for this lecture]`

---

To increase ulimit values:



ulimit -Hn 65535

ulimit -Sn 65535

ulimit -Hu 20480

ulimit -Su 20480

ulimit -Hf unlimited

ulimit -Sf unlimited


you can also make this persistent by going to the below and copy past the below values:



sudo nano /etc/security/ulimit.conf





*     soft   nofile  65535

*     hard   nofile  65535



*     soft   nofile  unlimited

*     hard   nofile  unlimited

*     hard   core    unlimited

*     hard   nproc   unlimited

*     hard   data    unlimited

*     soft   data    unlimited

*     soft   nproc   unlimited

*     soft   core    unlimited

*     hard   cpu     unlimited

*     hard   fsize   unlimited

*     soft   fsize   unlimited

*     soft   sigpending   unlimited

*     hard   sigpending   unlimited



for further info, please refer to the following links:



https://linux.die.net/man/5/limits.conf

https://linuxhint.com/permanently_set_ulimit_value/



