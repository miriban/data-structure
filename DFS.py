"""
    Depth First Search Implementation
    We are implementing a direct Graph
"""

class Graph:
    verticies = {}

    def addVertex(self,v):
        if v not in self.verticies:
            self.verticies[v] = []

    def addEdge(self,u,v):
        if u in self.verticies and v in self.verticies:
            self.verticies[u].append(v)

    def DFS_Visit(self,u,parent):
        for v in self.verticies[u]:
            if v not in parent:
                parent[v] = u
                self.DFS_Visit(v,parent)
    def DFS(self):
        parent = {}
        for v in self.verticies:
            if v not in parent:
                parent[v] = None
                self.DFS_Visit(v,parent)
        return parent



    def printGraph(self):
        for u in self.verticies:
            print u," => ", self.verticies[u]



# Testing
g = Graph()
g.addVertex("a")
g.addVertex("b")
g.addVertex("c")
g.addVertex("d")
g.addVertex("e")
g.addVertex("f")

g.addEdge("a","b")
g.addEdge("a","d")
g.addEdge("b","e")
g.addEdge("c","e")
g.addEdge("c","f")
g.addEdge("d","b")
g.addEdge("e","d")
g.addEdge("f","f")

print g.DFS()

#g.printGraph()
