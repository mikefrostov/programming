line = 'asdf fjdk; afed, fjek,asdf, foo' >>> import re
re.split(r'[;,\s]\s*', line)
#['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


fields = re.split(r'(;|,|\s)\s*', line)
fields

values = fields[::2]
delimiters = fields[1::2] + ['']
values
#['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo'] >>> delimiters

delimiters
#[' ', ';', ',', ',', ',', '']

''.join(v+d for v,d in zip(values, delimiters))
#'asdf fjdk;afed,fjek,asdf,foo'