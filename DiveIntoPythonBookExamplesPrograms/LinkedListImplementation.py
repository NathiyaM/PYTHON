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

class unorderedlist:
    def __init__(self):
        self.head=None
        self.No_nodes=None

    def is_empty(self):
        return self.head==None

    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current !=None:
            count+=1
            current = current.get_next()
        self.No_nodes = count
        return self.No_nodes

    def search(self,item):
        Found=False
        current=self.head
        while(current!=None and not Found):
            if(current.get_data()==item):
                Found = True
            current=current.get_next()
        return Found

    def remove(self,item):
        Found=False
        current = self.head
        previous = None
        while not Found:
            if current.get_data() == item:
                Found = True
            else:
                previous = current
                current = current.get_next()
        if previous==None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def middleElement(self):
        count = self.size()
        count = count//2
        i = 0
        current = self.head
        data = 0
        while(i<=count) and current !=None:
            data = current.get_data()
            current = current.get_next()
            i=i+1
        return data

    def printElement(self):
        current = self.head
        while(current!=None):
            data = current.get_data()
            print(data)
            current = current.get_next()

    def last3Element(self):
        current = self.head
        previous = current.get_next()
        while(previous!=None):
            current = previous
            previous = previous.get_next()

        print(current.get_data())
    def reverse(self):
        current = self.head
        while current!=None:

list = unorderedlist()
list.add(93)
list.add(94)
list.add(56)
list.add(57)
print(list.size())
print(list.search(97))
print(list.middleElement())
list.printElement()
list.last3Element()


