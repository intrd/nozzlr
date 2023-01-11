# Nozzlr v1.1

[![Rawsec's CyberSecurity Inventory](http://inventory.raw.pm/img/badges/Rawsec-inventoried-FF5050_flat-square.svg)](http://inventory.raw.pm/tools.html#Nozzlr)

Nozzlr is a multithread bruteforcer, trully modular and script-friendly - **author**: intrd@dann.com.br & github collaborators

The other bruteforce tools are amazing, but the hardcoded parameters make it painful to script 
over complex tasks. Nozzlr comes to solve this problem. All your task parameters/engine is 
managed directly in the task template(a python script). 

![nozzlr](/nozzlr.gif?raw=true "nozzlr bruteforcer")

```
usage: nozzlr taskmodule wordlists threads [--offset] [--resume_each] [--quiet] [--repeats] [--help]

positional arguments:
  taskmodule            Task template filepath
  wordlists             Wordlist paths(space separated, 2 max)
  threads               The number of threads

optional arguments:
  -h, --help            show this help message and exit
  --offset [OFFSET]     >= 0 start from wordlist linenumber
  --resume_each [RESUME_EACH]
                        100 = default, save session every 1k tries
  --quiet [QUIET]       Supress most of program output (saves CPU)
  --repeats [REPEATS]   Loops the same wordlists N times, default=1

Just copy one of this templates below to your working directory and customize to your needs.  

default task templates:
  templates/args_bruteforce.py : Commandline arguments bruteforcer (PoC: breaking ccrypt .cpt encrypted file)
  templates/args_bruteforce.py : Commandline arguments bruteforcer (PoC: recovering SSH RSA private keys passphrase)
  templates/args_gpgbruteforce.py : Commandline arguments bruteforcer (PoC: breaking GpG .gpg encrypted files)
  templates/args_charbruteforce.py : Commandline arguments bruteforcer (PoC: char by char looping the same wordlist)
  templates/stdin_bruteforce.py : STDIN - pipe inside commandline tools (PoC: bruteforcing LUKS)
  templates/ftp_bruteforce.py : RAW FTP (PoC: proFTPd, but works w/ any other server)
  templates/http_bruteforce.py : HTTP POST (PoC: bruteforcing pastd.com private notes)
  templates/ssh_bruteforce.py : SSH login (PoC: openSSH bruteforce)
  ...more at templates/

This is a proof-of-concept tool, any actions and or activities is solely your responsibility. 
The misuse of this tool can result in criminal charges brought against the persons in question. 
The authors and collaborators will not be held responsible in the event any criminal charges 
be brought against any individuals misusing this tool to break the law.

```
Yes! your tasktemplates/contributions are welcome :) 

## INSTALL
```
cd ~/ && git clone http://github.com/intrd/nozzlr appz/nozzlr && cd appz/nozzlr \
&& wget -O libs/int_netcat.py https://gist.github.com/intrd/00a39c83f752acf81775bfa9721e745a/raw/ \
&& sudo ln -s $PWD/nozzlr.py /usr/bin/nozzlr
```

## USAGE
Copy selected task xxx_bruteforce.py from /samples to your working directory, edit, and run:
```
nozzlr templates/ssh_bruteforce.py wordlists/unix_users.txt wordlists/unix_passwords.txt 1
```

## UPDATE
```
cd ~/appz/nozzlr && git fetch --all && git reset --hard origin/1.1  \
&& wget -O libs/int_netcat.py https://gist.github.com/intrd/00a39c83f752acf81775bfa9721e745a/raw/
```

## CHANGELIST
```
v1.1
  - added SSH Passphrase - RSA private keys bruteforcer
  - added Asterisk Call Management bruteforcer (port 5038)  
  - added Wordpress bruteforce
  - fixed gpg template
  - added breaking ccrypt .cpt encrypted file
  - added char by char looping the same wordlist
  - now processing multiple wordlists
```

