def checkio(number):
    result=1
    while(number<=0):
        digit=number%10
        print digit
        number=number/10
        if(digit!=0):
            result=result*digit
       
    return result

result=checkio(123405)
print result