## Nozzlr template : Commandline arguments bruteforcer (PoC: recovering SSH Passphrase from RSA private keys)
# @author intrd - http://dann.com.br/ 
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

# Make a copy of this module and adapt to your task!

from subprocess import Popen, PIPE, STDOUT

def nozz_module(payload, self=False, founds=False):
	payloads=':'.join(str(v) for v in payload.values())

	## Configs
	commandline="openssl rsa -in privatekey_filename.pem -out cracked.key -passin pass:"+payload[0] ##configure your privatekey filename here

	## Engine
	out={}
	out["code"]=""
	out["result"]=""
	code="null"
	try:
		process = Popen(commandline, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=False)
		(output, err) = process.communicate()
	except Exception as e:
		#print " "
		out["result"]=format(str(e)).strip()
		out["code"]="error"
		return out
	#print output
	if not "writing RSA key" in output:
		out["code"]="NEXT"
	else:
		print output
		out["code"]="found: \""+payloads+"\""
	return out
		