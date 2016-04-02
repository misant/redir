#!/bin/sh
/usr/bin/find /usr/pbi/squid-amd64/share/warn/warned/* -type f -delete

# enable if you want to clean up logs too
#/usr/bin/find /var/squid/logs/* -type f -delete 
#/usr/bin/find /var/squidGuard/log/* -type f -delete

