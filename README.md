# redir
Custom URL rewrite program for squid with squidGuard, allowing to show warning page and pass if user insists.
Created for pfSense 2.2.6 but can be modified for any other installation.

# TODO
1. Remove squid cache.log spamming
2. Replace python os.popen with subprocess

# Inspired by
That script was taken as starting point
https://gofedora.com/how-to-write-custom-redirector-rewritor-plugin-squid-python/ 
Undesranding of redirectors chaining thanks to
http://adzapper.sourceforge.net/
