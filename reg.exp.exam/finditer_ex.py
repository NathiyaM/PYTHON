import re
text = '1034567810378103'
pattern = '78'
count = 0
print re.finditer(pattern,text)
for match in re.finditer(pattern,text):
    s = match.start()
    e = match.end()
    count = count + 1
    print 'The pattern "%s" starts at %d and ends at %d ' %(pattern, s, e)
print 'In the given text, "%s" occured  %d times' %(pattern, count)
print dir(re);
