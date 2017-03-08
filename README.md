# Nozzlr v1.0 

Nozzlr is a multithread bruteforcer, trully modular and script-friendly. 

**Author**: intrd@dann.com.br - http://github.com/intrd/nozzlr

The other bruteforce tools are amazing, but the hardcoded parameters make it painful to script 
over complex tasks. Nozzlr comes to solve this problem. All your task parameters/engine is 
managed directly in the task module(a python script). 

```
usage: nozzlr taskmodule wordlist threads resume [-quiet] [--help]

positional arguments:
  taskmodule      Task module filepath
  wordlist        Wordlist path
  threads         The number of threads
  resume          0 = Restart, >= 1 Resume from wordlist linenumber

optional arguments:
  -h, --help      show this help message and exit
  -quiet [QUIET]  Supress most of program output (saves CPU)

Just copy one of this samples below to your working directory and customize to your needs.  

sample task modules:
  samples/argv_sample.py : ARGV - pipe to commandline args (PoC: bruteforcing ccrypt)
  samples/stdin_sample.py : STDIN - pipe inside commandline tools (PoC: bruteforcing LUKS)
  samples/ftp_sample.py : RAW FTP (PoC: proFTPd, but works w/ any other server)
  samples/http_sample.py : HTTP POST (PoC: bruteforcing pastd.com private notes)
  samples/ssh_sample.py : SSH login (PoC: openSSH bruteforce)

This is a proof-of-concept tool, any actions and or activities is solely your responsibility. 
The misuse of this tool can result in criminal charges brought against the persons in question. 
The authors and collaborators will not be held responsible in the event any criminal charges 
be brought against any individuals misusing this tool to break the law.

```

##INSTALL
```
$ cd ~/ && git clone http://github.com/intrd/nozzlr appz/nozzlr && cd appz/nozzlr \
&& wget -O libs/int_netcat.py https://gist.github.com/intrd/00a39c83f752acf81775bfa9721e745a/raw/ \
&& sudo ln -s $PWD/nozzlr.py /usr/bin/nozzlr
```

##USAGE
```
Copy selected task xxx_sample.py from /samples to your working directory, edit, and run:

$ nozzlr xxx_sample.py /wordlistpath/yourpasswords.txt 5 0
```

##UPDATE
```
$ cd ~/appz/nozzlr && git pull \
&& wget -O libs/int_netcat.py https://gist.github.com/intrd/00a39c83f752acf81775bfa9721e745a/raw/
```