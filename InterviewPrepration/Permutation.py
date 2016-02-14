str = 'abc'
result = []
for i in str:
    str1 = str.replace(i,'')
    per = i + str1
    result.append(per)
    rev = ''
    for j in str1[::-1]:
        rev = rev + j
    per1 = i + rev
    result.append(per1)
    print(result)
    