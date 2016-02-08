def HammingDistance(number1,number2):
    numb1=bin(number1)
    print(num1)
    num2=bin(number2)
    print(num1,num2)
    count1=count2=0
    for ch in str(num1):
        if ch=='1':
            count1+=1
    for ch in str(num2):
        if ch=='1':
            count1+=1
    diff=abs(count1-count2)
    return diff

num1=117
num2=7
result=HammingDistance(num1,num2)
print(result)

