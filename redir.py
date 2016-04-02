#!/usr/local/bin/python
#
#url_rewrite_program ver. 1.0 (02.04.2016)
#Bekhterev Evgeniy jbe@mail.ru https://bekhterev.me 


import sys,os


def modify_url(line):
    list = line.split(' ')
    # first element of the list is the URL
    old_url = list[0]
    # second contain client ip
    client = list[1]
    client = client.split('/', 1)[0]
    # last two characters could be warning label
    warning = old_url[-2:]
    new_url = '\n'
    from urlparse import urlparse
    # get domain from url requested
    parsed_uri = urlparse( old_url.replace("?", "") )
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    if domain == '':
	#domain could be blank, we do not like it
	domain = 'do not like empty'

    # take the decision and modify the url if needed
    # do remember that the new_url should contain a '\n' at the end.

    #create client file if does not exist
    if not os.path.exists('/usr/pbi/squid-amd64/share/warn/warned/'+client):
        open('/usr/pbi/squid-amd64/share/warn/warned/'+client, 'w').close()

    #check if warning already shown and request was redirected by squidGuard
    if warning == '&w':
	#check if domain from url was really added by client after warning shown
        if domain in open('/usr/pbi/squid-amd64/share/warn/warned/'+client).read():
	    new_url = old_url[:-2] + new_url
	#if client is playing tricks
	else:
	    new_url = 'https://google.com' + new_url

    #check if request is temporary whitelisted and return blank line to squid direclty meaning no rewrites needed
    elif domain in open('/usr/pbi/squid-amd64/share/warn/warned/'+client).read():
	new_url = '\n'

    #if not call squidGuard to check for block or warning or pass
    else:
        new_url = os.popen("echo \"" + line + "\" | /usr/pbi/squidguard-amd64/bin/squidGuard -c /usr/pbi/squidguard-amd64/etc/squidGuard/squidGuard.conf")
        new_url = new_url.read()

    #return url to squid
    return new_url

while True:
    #create user validation folder if not exist
    if not os.path.exists('/usr/pbi/squid-amd64/share/warn/warned/'):
    os.makedirs('/usr/pbi/squid-amd64/share/warn/warned/')


    # the format of the line read from stdin is
    # URL ip-address/fqdn ident method
    # for example
    # http://saini.co.in 172.17.8.175/saini.co.in - GET -
    line = sys.stdin.readline().strip()
    # new_url is a simple URL only
    # for example
    # http://fedora.co.in
    new_url = modify_url(line)

    sys.stdout.write(new_url)
    sys.stdout.flush()
