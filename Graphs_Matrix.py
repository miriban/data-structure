"""
    Implementation of Graphs using Matrix
"""
class Vertex:
    def __init__(self,name):
        self.name = name

class Graph:
    vertices = {}

    def addVertex(self,v):
        if isinstance(v,Vertex) and v.name not in self.vertices:
            d = {}
            for key,value in self.vertices.items():
                value[v.name] = 0
                d[key] = 0
            d[v.name] = 0
            self.vertices[v.name] = d
            return True
        else:
            return False

    def addEdge(self,u,v,weight=1):
        if u in self.vertices and v in self.vertices:
            self.vertices[u][v] = weight
            self.vertices[v][u] = weight
            return True
        else:
            return False

    def printGraph(self):
        for key,value in self.vertices.items():
            print key," ",value



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
