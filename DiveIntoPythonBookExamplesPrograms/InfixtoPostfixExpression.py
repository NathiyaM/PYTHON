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

def InfixToPostfix(expr):
    s = Stack()
    prec = {'/': 3, '*': 3, '+': 2, '-': 2, '(': 1}
    infixlist = expr.split()
    postfix = []
    for char in infixlist:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            s.push(char)
        elif char == ')':
            top_item = s.pop()
            while top_item!='(':
                postfix.append(top_item)
                top_item=s.pop()
        else:
            while(not s.is_empty()) and (prec[s.peek()] >= prec[char]):
                postfix.append(s.pop())
            s.push(char)
    while not s.is_empty():
        top_item=s.pop()
        postfix.append(top_item)
    return " ".join(postfix)

print(InfixToPostfix('A * B + C * D'))
print(InfixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
result=(InfixToPostfix('( 25 + 43 ) * ( 3 + 5 )'))

