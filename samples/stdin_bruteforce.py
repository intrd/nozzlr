## Nozzlr module : STDIN - pipe anything inside commandline tools (PoC: bruteforcing LUKS)
# @author intrd - http://dann.com.br/ 
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

# Make a copy of this module and adapt to your task!

from subprocess import Popen, PIPE, STDOUT

def nozz_module(payload, self=False, founds=False):
	payloads=':'.join(str(v) for v in payload.values())

	## Configs
	commandline="cryptsetup luksOpen /dev/loop0 crypt_fun"

	## Engine
	out={}
	out["code"]=""
	out["result"]=""
	code="null"
	try:
		process = Popen(commandline, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
		(output, err) = process.communicate(input=payload[0])
	except Exception as e:
		#print " "
		out["result"]=format(str(e)).strip()
		out["code"]="error"
		return out
	exit_code = process.wait()
	#print output
	if "already exists." in output or "not found" in output:
		out["result"]="error: already decrypted or error ind commandline."
		out["code"]="KILL"
		#os._exit(0)
		return out
	if "No key available with this passphrase" in output:
		out["result"]=output.strip()
		out["code"]="NEXT"
	else:
		out["code"]="found: \""+payloads+"\""
	return out
		