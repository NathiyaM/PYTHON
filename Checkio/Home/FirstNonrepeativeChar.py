from collections import Counter
str = 'abccdeba'
result = Counter(str)
key = []
for k ,v in result.items():
    if v == 1:
        key.append(k)
for i in str:
    if i in key:
        print(i)
        break
print(result,key)

