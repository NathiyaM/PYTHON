class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self,newdata):
        self.data = newdata
    def set_next(self,newnext):
        self.next = newnext

class orderedlist:
    def __init__(self):
        self.head=None

    def add(self,item):
        previous = None
        current = self.head
        stop = False
        while(current!=None and not stop):
            if current.getdata() >item:
                stop=True
            else:
                previous = current
                current = current.getnext()
        temp=Node(item)
        if previous==None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current.get_next())
            previous.set_next(temp)

    def search(self,item):
        current = self.head
        stop = False
        Found = False
        while (current!=None and not Found and not stop):
            if current.getdata == item:
                Found = True

            else:
                if current.getdata > item:
                    stop = True
                else:
                    current = current.get_next()
        return Found
