## Nozzlr template : Commandline arguments bruteforcer (PoC: breaking ccrypt .cpt encrypted file)
# @author intrd - http://dann.com.br/ 
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

# Make a copy of this template and adapt to your task!

from subprocess import Popen, PIPE, STDOUT

def nozz_module(payload, self=False, founds=False):
	payloads=':'.join(str(v) for v in payload.values())

	## Configs
	commandline="ccrypt -d test.txt.cpt -K '"+payload[0]+"'"

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
	if "No such file or directory" in output or "not found" in output:
		out["result"]="error: .cpt file does not exist"
		out["code"]="KILL"
		#os._exit(0)
		return out
	if "key does not match" in output:
		out["code"]="NEXT"
	else:
		out["code"]="found: \""+payloads+"\""
	return out
		