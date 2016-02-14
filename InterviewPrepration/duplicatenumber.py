
#In an array 1-100 exactly one number is duplicate how do you find it?

from collections import Counter
list = [1,1,2,2,3,4,5]
l = Counter(list)
print(l)
result = []
for k,v in l.items():
    if (v > 1):
        result.append(k)
print(result)