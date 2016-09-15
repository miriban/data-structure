"""
    Trie can be represented by list of lists or dict of dicts
"""
class Node:
    def __init__(self):
        self.data = None
        self.nodes = {}

    def __len__(self):
        return len(self.nodes)

    def insert(self,word,letterNum=0):
        if letterNum == len(word)-1:
            self.data = word
        else:
            if word[letterNum] not in self.nodes:
                self.nodes[word[letterNum]] = Node()
            self.nodes[word[letterNum]].insert(word,letterNum+1)

    def printdata(self,prefix,pos=0):
        if len(self.nodes) == 0:
            return False
        if pos >= len(prefix)-1:
            for key,node in self.nodes.iteritems():
                if node.data != None:
                    print node.data
        if len(prefix) > pos:
            self.nodes[prefix[pos]].printdata(prefix,pos+1)
        else:
            for key,node in self.nodes.iteritems():
                node.printdata(prefix,pos+1)






class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self,data):
        self.root.insert(data)

    def printdata(self,prefix):
        self.root.printdata(prefix)


t = Trie()
t.insert("cat")
t.insert("dog")
t.insert("banana")
t.insert("carpenter")
t.insert("door")
t.insert("dell")
t.printdata("b")
