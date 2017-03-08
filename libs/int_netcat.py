## intrd's netcat python socket (v1.1)
# @author intrd - http://dann.com.br/ (original: http://stackoverflow.com/a/36419867)
# @license Creative Commons Attribution-ShareAlike 4.0 International License - http://creativecommons.org/licenses/by-sa/4.0/

import socket
import socks

class Netcat:
    def __init__(self, ip, port, timeo=10, scks=False):
        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(timeo) 
        if scks:
            self.socket = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM) 
            self.socket.setproxy(PROXY_TYPE_SOCKS5, scks['host'],scks['port'])
        self.socket.connect((ip, port))

    def read(self, length = 1024):
        return self.socket.recv(length)
 
    def read_until(self, data):
        while not data in self.buff:
            self.buff += self.socket.recv(1024)
            #print(self.buff) #enable 4 debug
 
        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]
        return rval
 
    def write(self, data):
        self.socket.send(data)
    
    def close(self):
        self.socket.close()

## Usage
# nc = Netcat('ip.ip.ip.ip', port)
# data=nc.read_until(':')
# print(data)
# nc.write(number + '\n')