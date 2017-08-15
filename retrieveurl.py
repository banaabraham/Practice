import urllib2,sys
from  BeautifulSoup import BeautifulSoup

if len(sys.argv)<2:
    print "provide url to retrieve"
    sys.exit(0)
    
target = sys.argv[1]
try:
    pry = sys.argv[2]
except:
    pry = None

def retrieve(target):
    target = str(target)
    urls = []
    try:
        request = urllib2.Request(target, headers={"Accept" : "text/html"})
        contents = urllib2.urlopen(request).read()
        soup = BeautifulSoup(contents)
        for anchor in soup.findAll('a',href=True):
            print anchor['href']
            urls.append(anchor['href'])
    except Exception as e:
        print e
        sys.exit(0)
    return urls


if __name__=='__main__':
    sop = retrieve(target)
    if pry is not None:
        print "\nPerforming Level 2.. \n"
        large = []
        for i in sop:
            try:
                request = urllib2.Request(i, headers={'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
                contents = urllib2.urlopen(request).read()
                soup = BeautifulSoup(contents)
                for anchor in soup.findAll('a',href=True):        
                    large.append(anchor['href'])                  
            except:
                continue
        large = list(set(large)-set(sop))
        try:
            for i in large:
                print i
        except:
            print "there is no more url to retrieve.."
        
