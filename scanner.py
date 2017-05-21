import socket
from optparse import OptionParser
import time
import sys
loading=["-","/","|"]
parser=OptionParser()
parser.add_option("-t",dest="ip",help="target ip or DNS")
parser.add_option("-p",dest="ports",type="string",help="target port[s] multiple ports separate with comma")
parser.add_option("-b",dest="banner",action="store_true",help="banner grabing",default=False)
(opts,args)=parser.parse_args()
if opts.ip is None or opts.ports is None:
    parser.error("You must provide target IP and port -h for more help")
ip=opts.ip
ports=[]
result=[]
if "," in opts.ports:
    ports=str(opts.ports).split(',')
    ports=map(int,ports)
elif "-" in opts.ports:
    ports=str(opts.ports).split('-')
    ports=map(int,ports)
else:
    ports.append(int(opts.ports))
   

if "-" in opts.ports:
 
        for port in range(ports[0],ports[1]):
            for i in loading:
                sys.stdout.write("%s [%s]\r" %("scanning in progress",i))
                sys.stdout.flush()
                time.sleep(0.1) 
            try:
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((ip,port))
                #print "%d:open" %(port)
                s.close
                result.append(port)
            except:
                continue
                
else:
    
    for port in ports:
        for i in loading:
            sys.stdout.write("%s %s\r" %("scanning in progress",i))
            sys.stdout.flush()
            time.sleep(0.1)
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((ip,port))
            #print "%d:open" %(port)
            s.close
            result.append(port)
        except:
            continue
            
if opts.banner==True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect((ip,502))
        s.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
        reply=s.recv(4096)
        print reply
    except:
        print "Host is down"

for i in result:
    print "\n%d:open" %(i)
    
