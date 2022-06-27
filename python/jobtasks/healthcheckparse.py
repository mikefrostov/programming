import sys
import requests
import time
import urllib
import re
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
    result = str(r.content).split("\\n")
    while '' in result:
        result.remove('')
    while '\'' in result:
        result.remove('\'')
    dict1 = dict(e.split(':') for e in result)
    print(dict1)
    for k,v in dict1.items():
        if v != ' OK':
            print(" problem : " + k + " is " + v)

    #print(re.split('; |, |\*|\\n\'\n', str(r.content)))
    #d = dict(s.split(':') for s in result)
    #print(d)
    #pq = PyQuery(html)
    #tag = pq('pre')
    #print tag.text()
