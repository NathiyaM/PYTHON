class queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop(0)
    def items(self):
        return self.items

def letter_queue(commands):
    q=queue()
    for i in commands:
        i=i.split(' ')
        if i[0]=='PUSH':
            q.push(i[1])
        elif i[0] == 'POP':
            if q.is_empty():
                print("Empty Queue")
            else:
                q.pop()
    result=""
    while not q.is_empty():
        result=result+q.pop()
    return result

letter = ['PUSH A','POP','POP',"PUSH Z","PUSH D","PUSH O","POP", "PUSH T"]
print(letter_queue(letter))