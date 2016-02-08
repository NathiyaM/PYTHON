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

def matches(top_item,char):
    open={'[':1,'(':2,'{':3}
    close={']':1,')':2,'}':3}
    if open[top_item]==close[char]:
        return True
    else:
        return False

def checkio(expression):
    s=Stack()
    balance=True
    for list in expression:
        if list.isalnum() or list in '+*-/':
            continue
        elif list in '({[':
            s.push(list)
        else:
            if s.is_empty():
                balance=False
                break
            else:
                top_item = s.pop()
                if not matches(top_item,list):
                    balance=False
                    break
    if s.is_empty() and balance == True:
        return True
    else:
        return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"

'''
Simpler Solution:

def checkio(expression):
    pairs = {"(": ")", "[": "]", "{": "}"}
    stack = ""
​
    for char in expression:
        if char in pairs:
            stack += char
        elif char in pairs.values():
            if not stack:
                return False
            else:
                if pairs[stack[-1]] == char:
                    stack = stack[:-1]
                else:
                    return False
    if not stack:
        return True
    else:
        return False'''