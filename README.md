# Nozzlr v1.0 

Nozzlr is a multithread bruteforcer, trully modular and script-friendly.

**Author**: intrd@dann.com.br - http://github.com/intrd/nozzlr

```
usage: nozzlr taskmodule wordlist threads resume [-quiet] [--help]

Nozzlr is a multithread bruteforcer, trully modular and script-friendly. 
Others tools are amazing but is always painful when you need to script over your bruteforce taks. Nozzlr comes to solve this problem. Script out the hell!

positional arguments:
  task            Task module name (filename from tasks directory without .py)
  wordlist        Wordlist path
  threads         The number of threads
  resume          0 = Restart, >= 1 Resume from a given linenumber

optional arguments:
  -h, --help      show this help message and exit
  -quiet [QUIET]  Supress most of program output (saves CPU)

Nozzlr didn't fix task parameters at command line, all your tasks are configured directly from the module. Just copy one of this sample, rename and customize to your protocol/task. 

default modules/tasks:
  tasks/ftp_sample.py : FTP login - RAW FTP bruteforcer (PoC: ProFTPd but works w/ any other server)
  tasks/http_sample.py : HTTP - POST bruteforcer (PoC: breaking pastd.com private notes)
  tasks/ssh_sample.py : SSH login bruteforcer
  tasks/ssh_sample.py : ARGV - pipe to commandline args (PoC: breaking ccrypt)
  tasks/ssh_sample.py : STDIN - pipe anything inside commandline tools (PoC: breaking LUKS)

sample: nozzlr tasks/ssh_sample.py wl/unix_passwords.txt 1 0
```

##INSTALL
```
mkdir ~/nozzlr && cd ~/nozzlr && git clone http://github.com/intrd/nozzlr && sudo ln -s $PWD/nozzlr/nozzlr.py /usr/bin/nozzlr
```
