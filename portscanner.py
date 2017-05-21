import socket

ip=raw_input("IP address: ")
ports=raw_input("Port to scan:").split()
ports=map(int,ports)
if len(ports)==2:
    
    for port in range(ports[0],ports[1]):
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(100)
            s.connect((ip,port))
            print "%d:open" %(port)
            s.close
        except:
            continue
else:
    
    for port in ports:
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(100)
            s.connect((ip,port))
            print "%d: open" %(port)
            s.close
        except:
            continue
        
    
