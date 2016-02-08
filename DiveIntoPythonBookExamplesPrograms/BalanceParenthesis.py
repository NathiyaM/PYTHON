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

def matches(open,close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)


def balance_parenthis(string_symbol):
    s=Stack()
    balance=True
    index=0
    while(index<len(string_symbol)and balance == True):
        symbol=string_symbol[index]
        if(string_symbol[index] in '({['):
            s.push(string_symbol[index])
        else:
            if(s.is_empty()):
                balance=False
            else:
                top=s.pop()
                if not matches(top,string_symbol[index]):
                    balance=False

        index=index+1
    if balance and s.is_empty():
        print("Balanced Parenthesis")
    else:
        print("Inbalanced Parenthesis")




balance_parenthis('({[(])})')

