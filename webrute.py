import socket
import urllib2
from termcolor import colored
from optparse import OptionParser
import sys
parser=OptionParser()
parser.add_option("-u",dest='url',help='insert url, tambahkan FUZZ untuk letak fuzzing')
parser.add_option("-w",dest='wordlist',help='wordlist for brute',type="string")
(opts,args)=parser.parse_args()
if opts.url is None or opts.wordlist is None:
    parser.error("-h for help")
                  
wordlist=open(opts.wordlist,'r')                  
web=opts.url
total=sum(1 for line in open(opts.wordlist))
count=0

def progress(count, total,result,suffix="bruteforcing in progress, entuk "):
    
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s %s %s\r' % (bar, percents, '%', suffix,result))
    sys.stdout.flush()  # As suggested by Rom Ruben

def parsing(web,wordlist):
    global w
    for line in wordlist:
        w=web.replace('FUZZ',line)
        return w
        
        
def webs(web,wordlist):
    global count
    global total
    result=0
    for line in wordlist:
        parsing(web,wordlist)
        progress(count,total,result)
        count=count+1
        try:
            read=urllib2.urlopen(w)
            n=read.getcode()
            result=result+1
            print (colored("\n%s%s",'green')) %(w,n)            
        except urllib2.HTTPError:
            #print(colored('404','red'))
            continue
        except KeyboardInterrupt:
            print "bye-bye"
            break
        except:
            continue
webs(web,wordlist)    
       
    
    
