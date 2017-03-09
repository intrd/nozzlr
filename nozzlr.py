#!/usr/bin/env python
## Nozzlr v1.1 - Nozzlr v1.0 - The modular scriptable bruteforcer
# @author intrd - http://dann.com.br/ 
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

# Do not edit anything in this file, copy/edit one of the tasks from "samples/".

import signal, sys, os, time, Queue, threading, imp, argparse, ntpath

realpath=os.path.realpath(__file__).replace(os.path.basename(__file__)+".py","")
sys.path.append(realpath+"/libs")

def banner_welcome():
	print "## Nozzlr v1.0 - The modular scriptable bruteforcer "
	print "## Author: intrd@dann.com.br - http://github.com/intrd/nozzlr\n"

def banner_loading():
	print "** loading module: "+taskpath+"\n>> task running @ "+str(threadsnum)+" threads.."

def banner_end():
	print "\n## end of nozzlr session."

def pprint(text):
	sys.stdout.write(text)
	sys.stdout.flush()

def import_(filename):
    path, name = os.path.split(filename)
    name, ext = os.path.splitext(name)
    file, filename, data = imp.find_module(name, [path])
    mod = imp.load_module(name, file, filename, data)
    return mod

def handler(signal, frame):
    print "trl-C.. exiting nozzlr."
    os._exit(0)

def int_filew(path,text,mode):
	file = open(path, mode)
	file.write(text)
	file.close()

banner_welcome()
parser = argparse.ArgumentParser( description="The other bruteforce tools are amazing, but the hardcoded parameters make it painful to script over complex tasks. Nozzlr comes to solve this problem. All your task parameters/engine is managed directly in the task module(a python script).\n", \
	usage="nozzlr taskmodule wordlists threads [--offset] [--resume_each] [--quiet] [--help]\n", \
	formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""\
Just copy one of this samples below to your working directory and customize to your needs.  

default task modules:
  samples/argv_bruteforce.py : ARGV - pipe to commandline args (PoC: bruteforcing ccrypt)
  samples/stdin_bruteforce.py : STDIN - pipe inside commandline tools (PoC: bruteforcing LUKS)
  samples/ftp_bruteforce.py : RAW FTP (PoC: proFTPd, but works w/ any other server)
  samples/http_bruteforce.py : HTTP POST (PoC: bruteforcing pastd.com private notes)
  samples/ssh_bruteforce.py : SSH login (PoC: openSSH bruteforce)

sample: nozzlr samples/ssh_bruteforce.py wordlists/unix_users.txt wordlists/unix_passwords.txt 1

This is a proof-of-concept tool, any actions and or activities is solely your responsibility. The misuse of this tool can result in criminal charges brought against the persons in question. The authors and collaborators will not be held responsible in the event any criminal charges be brought against any individuals misusing this tool to break the law.
""")
parser.add_argument('taskmodule', type=str, help='Task module filepath')
parser.add_argument('wordlists', type=str, nargs='*', help='Wordlist paths(space separated, 2 max)')
parser.add_argument('threads', type=str, help='The number of threads')
parser.add_argument('--offset', nargs='?', default=False, help='>= 0 start from wordlist linenumber')
parser.add_argument('--resume_each', nargs='?', default=100, help='100 = default, save session every 1k tries')
parser.add_argument('--quiet', nargs='?', default=False, help='Supress most of program output (saves CPU)')
args = parser.parse_args()

threadsnum=int(args.threads)
taskpath=args.taskmodule
modulename=ntpath.basename(taskpath)+".session"
resume_each=int(args.resume_each)

resum=args.offset
if resum==False:
	if not os.path.isfile(modulename):
		resum=0
	else:
		resum=int(open(modulename).readline().rstrip())
else:
	resum=int(args.offset)

wordlists=args.wordlists
nodebug=False
if args.quiet != False: nodebug=True

banner_loading()
queue = Queue.Queue()
class worker(threading.Thread):
	def __init__(self,queue):
		self.alive = True
		threading.Thread.__init__(self)
		self.queue=queue
	def run(self):
		retry=False
		while self.alive:
			workerid=threading.current_thread().getName().strip()
			out=""
			if not retry:
				if self.queue.empty() is True:
					out+="** queue empty, closing thread.."
					print workerid+" - "+out
					self.alive = False
					break
				else:
					self.clear=self.queue.get()
				payload = self.clear
				ind = str(payload["id"])
				payload = payload["payloads"]
				payloads=':'.join(str(v) for v in payload.values())
				if int(ind)%resume_each==0:
					int_filew(modulename,ind+"\n","w")
			out+=(" <"+ind+"> '"+payloads+"'")
			#print out
			#exit()
			retry=True
			task = import_(taskpath)
			t1 = time.time()

			runn=task.nozz_module(payload,self)
			# runn={}
			# runn["code"]="NEXT"
			# runn["result"]="aa"
			# time.sleep(0.1)

			code=runn["code"]
			#code="error"
			code=format(str(code)).strip()
			out+=" "+runn["result"]
			if code == "KILL":
				print out
				self.queue.task_done()
				os._exit(0)
			if code == "EOF":
				out+="** queue empty, closing thread.."
				self.queue.task_done()
			if "found" not in code and code != "NEXT":
				time.sleep(1)
				retry=True
			else:
				if code == "NEXT":
					retry=False
				if "found" in code:
					pprint("\n# # # # # # # # "+code+" # # # # # # # #\n")
					file = open("founds.txt", 'a')
					file.write(payloads+"\n")
					file.close()
					t2 = time.time()
					banner_end()
					print "## benchmark %s threads, time=%s" % (threadsnum, t2 - t1)
					self.queue.task_done()
					os._exit(0)
				self.queue.task_done()
			out=workerid+": "+out
			out=out.replace("  "," ")
			if not nodebug: print out
			#self.queue.task_done()
			#os._exit(0) #debug


def main():
	wlists={}
	wlists_sizes={}
	wid=0
	for wordlist in wordlists: #get wordlists
		wlists_sizes[wid]=os.path.getsize(wordlist)
		wlists[wid]=open(wordlist,'r')
		wid+=1

	jobs={}
	payloads={}
	i=0
	if len(wlists)==1: #create jobs (only 1 wordlist)
		for word in wlists[0].readlines(): 
			if i >= resum: 
				payloads={"id":i, "payloads": {0: word.strip()}}
				#jobs[i]=payloads
				queue.put(payloads)
			i+=1
	else: #create jobs (2 combined wordlists)
		if wlists_sizes[0] >= wlists_sizes[1]:
			bigger=wlists[0]
			smaller=wlists[1]
		else:
			bigger=wlists[1]
			smaller=wlists[0]
		for w2 in smaller.readlines():
			bigger.seek(0)
			for w1 in bigger.readlines():
				if i >= resum: 
					payloads={"id":i, "payloads": {0: w2.strip(), 1: w1.strip()}}
					queue.put(payloads)
					#jobs[i]=payloads
				i+=1
	#print queue
	#exit()

	for i in range(threadsnum): #assign jobs to the workers
		t=worker(queue)
		t.setDaemon(True)
		t.start()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)
    main()
    while True:           
        signal.pause()    