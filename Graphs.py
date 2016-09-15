"""
    Implementation of Graph using Adjacency List
"""
class Vertex:
    def __init__(self,name):
        self.name = name
        self.neighbors = list()

    def addNeighbor(self,v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = {}

    def addVertex(self,v):
        if isinstance(v,Vertex) and v.name not in self.vertices:
            self.vertices[v.name] = v
            return True
        else:
            return False

    def addEdge(self,u,v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].addNeighbor(v)
            self.vertices[v].addNeighbor(u)
            return True
        else:
            return False

    def printGraph(self):
        for key in sorted(list(self.vertices.keys())):
            print key,self.vertices[key].neighbors


g = Graph()
# print(str(len(g.vertices)))
a = Vertex('A')
g.addVertex(a)
g.addVertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.addVertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.addEdge(edge[:1], edge[1:])

g.printGraph()
