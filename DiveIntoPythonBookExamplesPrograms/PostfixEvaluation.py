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

def postfix_evaluation(expr):
    s=Stack()
    numlist=expr.split(" ")
    print(numlist)
    for num in numlist:
        if num.isalnum():
            s.push(int(num))
        else:
            operand1 = s.pop()
            operand2 = s.pop()
            result = operation(num,operand1,operand2)
            s.push(result)
    return s.pop()

def operation(op,operand1,operand2):
    if(op == '*'):
        print(operand2+operand1)
        return operand1 * operand2
    elif (op == '/'):
        return operand2 / operand1
    elif (op == '+'):
        print(operand1+operand2)
        return operand1 + operand2
    elif (op == '-'):
        return operand1 - operand2

print(postfix_evaluation('70 80 + 30 20 + /'))