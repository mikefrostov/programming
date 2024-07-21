from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read() 
    else:
        with open(name) as f: 
            return f.read()


choices = ['http:', 'ftp:'] 
url = 'http://www.python.org' 
url.startswith(choices) 
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#TypeError: startswith first arg must be str or a tuple of str, not list 
url.startswith(tuple(choices))
#True


### same but slice()

filename = 'spam.txt'
filename[-4:] == '.txt'
#True
url = 'http://www.python.org'
url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:' True


### same but reg exp

import re
url = 'http://www.python.org'
re.match('http:|https:|ftp:', url) 
#<_sre.SRE_Match object at 0x101253098>

if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
    pass


