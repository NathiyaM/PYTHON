class BinHeap:
    def __init__(self):
        self.heap = []
        self.currentsize = 0
    def insert(self,item):
        self.heap.append(item)
        self.currentsize+=1
        self.percup(self.currentsize)

    def percup(self,i):
        while(i//2 >0):
            if self.heap[i]<self.heap[i//2]:
                self.heap[i],self.heap[i//2]=self.heap[i//2],self.heap[i]
            i = i//2

    def delmin(self):
        retval = self.heap[1]
        self.heap[1]=self.heap[self.currentsize]
        self.currentsize = self.currentsize-1
        self.heap.pop(1)
        self.percdown(1)
        return retval

    def percdown(self,i):
        while i*2 >= self.currentsize:
            mc = self.minsize(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i],self.heap[mc] = self.heap[mc],self.heap[i]
            i = mc

    def minsize(self,i):
        if i*2 + 1 > self.currentsize:
            return i*2
        else:
            if self.heap[i*2] > self.heap[i*2+1]:
                return i *2
            else:
                return i *2 +1

    def build(self,alist):
        i = len(alist)//2
        self.currentsize = len(alist)
        self.heaplist = [0] + alist [:]
        while i >0:
            self.percdown(i)
            i = i - 1

