# You want to match text using the same wildcard patterns as are commonly used when
# working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc.).

from fnmatch import fnmatch, fnmatchcase
fnmatch('foo.txt', '*.txt')
#True
fnmatch('foo.txt', '?oo.txt')
#True
fnmatch('Dat45.csv', 'Dat[0-9]*')
#True
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
[name for name in names if fnmatch(name, 'Dat*.csv')]
# ['Dat1.csv', 'Dat2.csv']