import collections

fo =open('red-headed-league.txt','r')
contentlist=list()
for lines in fo.readlines():
	lineitems=lines.strip().split()
	contentlist.extend([items.lower() for items in lineitems])
	
word=collections.Counter(contentlist)
fo.close()
print word
