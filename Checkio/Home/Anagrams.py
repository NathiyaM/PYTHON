from collections import Counter
from string import whitespace
string1="Kings Lead Hat"
string2="Talking heads"
string1=string1.lower()
string1 = string1.replace(" ",'')
print(string1)
string2 = string2.lower()
string2 = string2.replace(" ",'')
print(string2)
breakfast_counter=Counter(string1)
breakfast_counter1=Counter(string2)
result = True
for k,v in sorted(zip(breakfast_counter.items(),breakfast_counter1.items())):
    print(k,v)
    if k==v:
        continue
    else:
        result = False
print(True)


