import socket
from optparse import OptionParser 
import time
import sys
from threading import *
parser=OptionParser()
parser.add_option("-t",dest="ip",help="target ip or DNS")
parser.add_option("-p",dest="ports",type="string",help="target port[s] multiple ports separate with comma")
parser.add_option("-F",dest="fast",action="store_true",help="fast scan",default=False)
parser.add_option("-T",dest='waktu',type="float",help="sleep time",default=3)
(opts,args)=parser.parse_args()
if opts.ip is None and opts.ports is None and opts.fast is False:
    parser.error("You must provide target IP and port -h for more help")
if opts.fast is True:
    opts.ports=[21,22,23,80,445,3306,3389]
#inisiasi global variable    
result=[]
detail=[]
#app list
daftar=open('list.txt','r')
#loading sign
def loading():
    batang=["-","/","|"]
    for i in batang:
        sys.stdout.write("%s [%s]\r" %("scanning in progress",i))
        sys.stdout.flush()
        time.sleep(0.1)
#port input parser
def parse(ports):
    portsl=[]
    if opts.fast is True:
        portsl=ports
    elif "," in ports:
        portsl=str(ports).split(',')
        portsl=map(int,portsl)
    elif "-" in ports:
        portsl=str(ports).split('-')
        portsl=map(int,portsl)
        portsl=range(portsl[0],portsl[1]+1)
    else:
        portsl.append(int(ports))   
    return portsl
#analisis reply 
def analyze(reply):
    """
    if "Apache" in reply:
        return "Apache"
    elif "Pure-FTPd" in reply:
        return "Pure-FTPd"
    elif "MySQL" in reply:
        return "MySQL"
    elif "OpenSSH" in reply:
        return "OpenSSH"
    """
    for line in daftar:
        if line in reply:
            return line

def sock(ip,ports):
    global result
    global detail
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(100)
        s.connect((ip,ports))
        s.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
        reply=s.recv(4096)
        detail.append(analyze(reply))
        result.append(ports)    
        s.close            
    except :
        pass
    return detail,result

def conn(ip,ports):
    ports=parse(ports)
    for p in ports:
        loading()
        t=Thread(target=sock,args=(ip,p))
        t.start()
    merge=zip(result,detail)
    if len(result)==0:
        print "\nAll ports are closed"
    else:
        for i in merge:
            print "\n%d open %s" %(i[0],i[1])
    
conn(opts.ip,opts.ports)        
