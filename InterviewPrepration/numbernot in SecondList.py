#Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not present in the second array.

a= [1,2,3,4,5]
b = [2,3,1,0,5]
for i in a:
    if i not in b:
        missingnumber = i
print(missingnumber)
