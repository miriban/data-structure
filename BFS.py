"""
    Breadth First Search Implementation
    We are implementing an indirect Graph
"""

class Graph:
    verticies = {}
    def addVertex(self,v):
        if v not in self.verticies:
            self.verticies[v] = []

    def addEdge(self,u,v):
        if u in self.verticies and v in self.verticies:
            self.verticies[u].append(v)
            self.verticies[v].append(u)

    def BFS(self,s):
        level = {s:0} # setting the level of starting vertex to 0
        parent = {s:None} # setting the starting vertex parent to be None
        frontier = [s]
        i = 1 # because we have set the frontier that we are visiting in level 0
        while frontier:
            next = []
            for u in frontier:
                for v in self.verticies[u]:
                    if v not in level:
                        level[v] = i
                        parent[v] = u
                        next.append(v)
            frontier = next
            i = i + 1
        # We reach the end of BFS
        return parent

    def printShortestPath(self,parent,s,v):
        if v == s:
            print s
            return
        print v
        self.printShortestPath(parent,s,parent[v])


    def printGraph(self):
        for u in self.verticies:
            print u," => ", self.verticies[u]



# Testing
g = Graph()
g.addVertex("s")
g.addVertex("a")
g.addVertex("x")
g.addVertex("z")
g.addVertex("d")
g.addVertex("c")
g.addVertex("f")
g.addVertex("v")

g.addEdge("s","a")
g.addEdge("s","x")
g.addEdge("a","z")
g.addEdge("x","d")
g.addEdge("x","c")
g.addEdge("d","f")
g.addEdge("d","c")
g.addEdge("c","f")
g.addEdge("c","v")

parents = g.BFS("z")
g.printShortestPath(parents,"z","v")
#g.printGraph()
