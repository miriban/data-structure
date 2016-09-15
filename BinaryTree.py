class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self,data):
        if self.data == data:
            return self
        if self.data > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        print self.data
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print self.data
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print self.data

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print "PreOrder"
        self.root.preorder()

    def postorder(self):
        print "PostOrder"
        self.root.postorder()

    def inorder(self):
        print "InOrder"
        self.root.inorder()


"""
    Test
"""
tree = Tree()
tree.insert(7)
tree.insert(4)
tree.insert(2)
tree.insert(3)
tree.insert(6)
tree.insert(5)
tree.insert(12)
tree.insert(9)
tree.insert(8)
tree.insert(11)
tree.insert(19)
tree.insert(15)
tree.insert(20)

tree.inorder()
tree.preorder()
tree.postorder()
