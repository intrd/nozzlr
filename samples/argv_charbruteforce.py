## Nozzlr module : ARGV - pipe to commandline args (PoC: bruteforcing char by char looping the same wordlist)
# @author intrd - http://dann.com.br/ 
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

# Make a copy of this module and adapt to your task!

from subprocess import Popen, PIPE, STDOUT

def nozz_module(payload, self=False, founds=False):
	payloads=':'.join(str(v) for v in payload.values())

	print founds
	foundslen=len(founds)
	print foundslen
	flag=list("AAAAAAAAAAAAAAAAAAAA")
	
	flag[foundslen]=payload[0]

	commandline="./bin "+"".join(flag)
	print commandline

	out={}
	out["code"]=""
	out["result"]=""
	code="null"
	try:
		process = Popen(commandline, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=False)
		(output, err) = process.communicate()
	except Exception as e:
		out["result"]=format(str(e)).strip()
		out["code"]="error"
		return out
	if not "Peem! Get out of here" in output:
		out["code"]="NEXT"
	else:
		print output
		founds=payload[0]
		out["code"]="NEXT"
		out["founds"]=founds
		return out
	return out