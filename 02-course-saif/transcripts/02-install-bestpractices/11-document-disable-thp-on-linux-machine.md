---
course: saif-admin
theme: 02-install-bestpractices
lecture: 11
lecture-title: "Document - Disable THP on Linux machine"
kind: document
source: "the-splunk-enterprise-certified-admin-course-2022-with-labs_transcript.txt"
tags: [course/saif-admin, theme/02-install-bestpractices, transcript, kind/document]
---

# Lecture 11 — Document - Disable THP on Linux machine

> **This is a document lecture, not a video.** On Udemy it contains links, commands, or written resources rather than a video transcript.

`[No transcript available for this lecture]`

---

To disable the THP, please use the script I have provided in the resources section and change the permissions to make it executable, the file name is "disable_thp_script"



#sudo chmod 755 /etc/init.d/disable_thp_script



sudo update-rc.d disable-thp defaults



also, check the below link for further info about how to disable transparent Huge pages





https://community.splunk.com/t5/Monitoring-Splunk/How-do-I-disable-Transparent-Huge-Pages-THP-and-confirm-that-it/td-p/124490?_ga=2.76985692.817637445.1665312686-93827130.1664803635&_gac=1.223738217.1665332124.Cj0KCQjw4omaBhDqARIsADXULuXaKuIEGb3tJD_74EPf27jtQRnrTsbzXeYY5t3agm7nFFIE6G7GeNYaAqVIEALw_wcB&_gl=1*1hb4pj7*_ga*OTM4MjcxMzAuMTY2NDgwMzYzNQ..*_gid*ODE3NjM3NDQ1LjE2NjUzMTI2ODY.*_gac*Q2owS0NRanc0b21hQmhEcUFSSXNBRFhVTHVYYUt1SUVHYjN0SkRfNzRFUGYyN2p0UVJuclRzYnpYZVlZNXQzYWdtN25GRklFNkc3R2VOWWFBcVZJRUFMd193Y0IuMTY2NTMzMjEyMw..



https://www.liquidweb.com/kb/linux-runlevels-explained/



https://docs.couchbase.com/server/current/install/thp-disable.html



to verify the script is working, please check the below commands:





#sudo cat /sys/kernel/mm/transparent_hugepage/enabled

#sudo cat /sys/kernel/mm/transparent_hugepage/defrag







also, I am providing the complete script "disable_thp_script" for disabling the THP as per below: 



===========================================

#!/bin/bash
### BEGIN INIT INFO
# Provides:          disable-thp
# Required-Start:    $local_fs
# Required-Stop:
# X-Start-Before:    couchbase-server
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Disable THP
# Description:       Disables transparent huge pages (THP) on boot, to improve
#                    Couchbase performance.
### END INIT INFO
 
case $1 in
  start)
    if [ -d /sys/kernel/mm/transparent_hugepage ]; then
      thp_path=/sys/kernel/mm/transparent_hugepage
    elif [ -d /sys/kernel/mm/redhat_transparent_hugepage ]; then
      thp_path=/sys/kernel/mm/redhat_transparent_hugepage
    else
      return 0
    fi
 
    echo 'never' > ${thp_path}/enabled
    echo 'never' > ${thp_path}/defrag
 
    re='^[0-1]+$'
    if [[ $(cat ${thp_path}/khugepaged/defrag) =~ $re ]]
    then
      # RHEL 7
      echo 0  > ${thp_path}/khugepaged/defrag
    else
      # RHEL 6
      echo 'no' > ${thp_path}/khugepaged/defrag
    fi
 
    unset re
    unset thp_path
    ;;
esac
===========================================

