from collections import Counter
string1="Helliio"
string2="Ol Helio"
string1=string1.lower().strip(' ')
print(string1)
string2 = string1.lower().strip(' ')
print(string2)
breakfast_counter=Counter(string1)
breakfast_counter1=Counter(string2)
for k,v in zip(breakfast_counter.items(),breakfast_counter1.items()):
    print(k,v)
    if k==v:
        continue
    else:
        print(False)
print(True)


