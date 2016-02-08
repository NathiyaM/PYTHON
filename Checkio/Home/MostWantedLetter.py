'''
punctuation="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 0123456789"
s="Hello World"
for c in punctuation:
    s=s.replace(c,'')
s=s.lower()
newlist={}
for i in s:
    newlist[i]=newlist.get(i,0)+1
max=0
result=[]
for k,v in newlist.items():
    if v>max:
        max=v
print(max)
for k,v in newlist.items():
    if(v==max):
        result.append(k)
result.sort()

print(result[0])
#list=sorted(newlist.keys())
print(newlist)
print(s)
'''

import string
def checkio(text):
    text=text.lower()
    print(max(string.ascii_lowercase,key=text.count))

text="Hello World"
result=checkio(text)
print(result)
