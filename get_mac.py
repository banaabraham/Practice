import urllib2,sys,urllib

if len(sys.argv)<2:
    print "Input mac address"
    sys.exit(0)
    
target = "https://api.macvendors.com/" + urllib.quote(sys.argv[1])
print target

def retrieve(target):
    target = str(target)
    try:
        #request = urllib2.Request(target, headers={"Accept" : "text/html"})
        contents = urllib2.urlopen(target).read()
        print(contents)
    except Exception as e:
        print e

retrieve(target)
