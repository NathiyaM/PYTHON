def HammingDistance(number1,number2):
    print(bin(number1 ^ number2).count('1'))
    ''' list1 = []
    list2 = []
    while(number1>0):
        rem = number1%2
        number1 = number1//2
        list1.append(rem)
    while(number2>0):
        rem = number2%2
        number2 = number2//2
        list2.append(rem)
    if(len(list1)>len(list2)):
        while(len(list1)>len(list2)):
            list2.append(0)
    else:
        while(len(list2)>len(list1)):
            list1.append(0)

    list1.reverse()
    list2.reverse()

    print(list1,list2)
    result=[]
    for i ,j in zip(list1,list2):
        if (i==1 and j==1) or (i == 0 and j == 0) :
            result.append(0)
        elif (i==1 and j==0) or (i==0 and j==1 ):
            result.append(1)
    print(result)
    print(sum(result))'''



num1=1
num2=2
HammingDistance(num1,num2)


