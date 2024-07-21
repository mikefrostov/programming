filename = 'spam.txt'
filename.endswith('.txt') True
filename.startswith('file:') False
url = 'http://www.python.org' >>> url.startswith('http:')

import os
#filenames = os.listdir('.')
filenames = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
[name for name in filenames if name.endswith(('.c', '.h')) ]
# ['foo.c', 'spam.c', 'spam.h']
any(name.endswith('.py') for name in filenames)
# True