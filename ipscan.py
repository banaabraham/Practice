
import subprocess
from optparse import OptionParser
target=[]

parser=OptionParser()
parser.add_option("-t",dest="ip",help="target ip or DNS",type="string")
(opts,args)=parser.parse_args()
if opts.ip is None:
    parser.error("you must provide IP")
satu=opts.ip.split("-")
dua=satu[0].split(".")
tiga=dua[0:3]
local=".".join(tiga)
for i in range(int(dua[3]),int(satu[1])+1):
    target.append(local+"."+str(i))
    

def cmd(command, args):
    """Launches 'command' windowless and waits until finished"""
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    return subprocess.Popen([command] + args, startupinfo=startupinfo).wait()

for i in target:
    a=cmd("ping",[i])
    if a==0:
        print i+" is up"
