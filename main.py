import sys
import requests
import time
import urllib
#import validators
from pyquery import PyQuery    


if __name__ == "__main__":
    #counter = int(sys.argv[1])
    #print(sys.argv[1])
    
    #print (url)
#    if validators.url(url):
#        while(True):
#            r = requests.get(url)    
#            if r.status_code == 200:
#                html = r
#            if r.status_code != 200:
#                print("ERR({" + str(r.status_code) + "})")
#            time.sleep(counter)
#    else:
#        print("URL parsing error: " + url)
    url = sys.argv[1]
    r = requests.get(url)
    #print(str(r.content).split("\n"))
    print(r.content)

    

    #pq = PyQuery(html)
    #tag = pq('pre')
    #print tag.text()





