class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def is_empty(self):
        return self.items==[]
    def size(self):
        return len(self.items)

def IntegerToDecimal(number,base):
    digits='0123456789ABCDEF'
    s=Stack()
    while(number>0):
        remainder=number%base
        s.push(remainder)
        number=number//2
    result=''
    while not s.is_empty():
        result=result+digits[(s.pop())]
    return result

result=IntegerToDecimal(233,2)
print(result)

