class Vertex:
    def __init__(self,key):
        self.id =  key
        self.connectedto = {}

    def addneighbour(self,nbr,weight):
        self.connectedto[nbr] = weight

    def __str__(self):
        return str(self.id) + "ConnectedTo:" + str([x.id for x in self.connectedto])

    def getConnections(self):
        return self.connectedto.keys()

    def getId(self):
        return self.id

    def getweight(self,nbr):
        return self.connectedto[nbr]





class Graph:
    def __init__(self):
        self.vertList = {}
        self.sumofVertices = 0

    def addVertex(self,key):
        self.sumofVertices += 1
        numvertix = Vertex(key)
        self.vertList[key] = numvertix
        return numvertix

    def getvertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = Vertex(f)
        if t not in self.vertList:
            nv = Vertex(t)
        self.vertList[f].addneighbour(self.vertList[t],cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
    print(v)
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))



