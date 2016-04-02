# redir
Custom URL rewrite program for squid with squidGuard, allowing to show warning page and pass if user insists.
Created for pfSense 2.2.6 but can be modified for any other installation. Tested with transparent mode.

I am not a programmer, so it full of dirty hacks and dirty methods. But it works.

# Installation

1. Copy redir.py to /usr/pbi/squid-amd64/share/warn/redir.py and make it executable
2. Copy cleanup.sh to whatever you like folder, make it executable and add to cron. If you want user to see warnings not rare then every 10 minutes, make it run every 10 minutes.
3. Copy with replacement sgerror.php to /usr/local/www/sgerror.php (
4. Copy sgwrite.php to /usr/local/www/sgwrite.php 
5. Copy with replacement squidguard.inc to /usr/local/pkg/squidguard.inc
6. Create SquidGuard target category name Warning (case sensitive), Redirect mode = int error page
7. Add desired URLs, domains and regular expressions for which warning will be shown, modify message (Redirect section)
8. Add Warning target category to ACL with block decision. 
9. Save and apply SquidGuard configuration.
10. Check Squid integration, it should be like:
redirector_bypass off;url_rewrite_program /usr/pbi/squid-amd64/share/warn/redir.py;url_rewrite_bypass off;url_rewrite_children 16 startup=8 idle=4 concurrency=0

# How it works

Redir takes requests from squid, if requested domain was remorary whitelisted tell squid to show page.
If not gives request to SquidGuard. SquidGuard as usual determines if url request will be passed or blocked.
If blocked and target category is Warning it will show Agree button.
If Agree button pressed, sgwrite.php starts, writing url into users temp file. Temp files are deleted with CRONed cleanup.sh
Sgwrite.php redirects request to URL+&w, its needed because if URL will be not changed it will return cached by browser block page sgerror.php

# Known issues

Fills /var/squid/logs/cache.log with garbage. 

# TODO
1. Remove squid cache.log spamming
2. Replace python os.popen with subprocess
3. Installation script? Not sure if needed

# Inspired by
That script was taken as starting point
https://gofedora.com/how-to-write-custom-redirector-rewritor-plugin-squid-python/ 
Undesranding of redirectors chaining thanks to
http://adzapper.sourceforge.net/
