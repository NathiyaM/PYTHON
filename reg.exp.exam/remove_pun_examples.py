import re
p=re.compile(r'\W+')
punc=p.split('This is,a..test')
print punc
