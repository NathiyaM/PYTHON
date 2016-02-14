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


def digit_stack(list):
    s=Stack()
    sum=0
    for i in list:
        items = i.split(' ')
        print(items)
        if(items[0]=='PUSH'):
            s.push(int(items[1]))
        elif (items[0]=='POP'):
            if s.is_empty()==True:
                continue
            item = s.pop()
            sum=sum+item
        else:
            item=s.peek()
            sum=sum+item
    return sum

result=digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"])
print(result)