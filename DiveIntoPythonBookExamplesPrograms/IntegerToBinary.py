import Stack

def IntegerToDecimal(number):
    s=Stack.Stack()
    while(number>0):
        if(number%2==0):
            s.push(0)
        else:
            s.push(1)
        number=number//2
    result=''
    while not s.is_empty():
        result=result+str(s.pop())
    return result

result=IntegerToDecimal(233)
print(result)

