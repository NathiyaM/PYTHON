class HashTable:
    def __init__(self,size):
        self.size = size
        self.slots = [None]*self.size
        self.data = [None]*self.size
    def put(self,key,data):
        hashvalue = self.hashfunction(key,self.size)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and \
                      self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

        if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
        else:
            self.data[nextslot] = data #replace

def hashfunction(self,key,size):
     return key%size

def rehash(self,oldhash,size):
    return (oldhash+1)%size


H=HashTable(11)
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
