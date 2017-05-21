
import socket
c=open('D.wordlist','r')
for line in c:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(100)
        s.connect(('127.0.0.1',445))
        s.send("%s\r\n") %(line)
        reply=s.recv(1024)
        print reply
    except:
        print "gagal"

