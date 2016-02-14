str1 = 'A but tuba'
str = str1.replace(' ','')
list1 = []
list2 = []
for i in str.lower():
    list1.append(i)
for i in str.lower()[::-1]:
    list2.append(i)
Found = True
for i in range(len(str)):
    if list1[i] != list2[i]:
        Found = False
        break
print(Found)