class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.root = None
		self.size = 0

	def printList(self):
		currentNode = self.root
		while currentNode != None:
			print currentNode.data
			currentNode = currentNode.next

	def get_size(self):
		return self.size

	def find(self,data):
		currentNode = self.root
		while currentNode != None:
			if currentNode.data == data:
				return currentNode
			currentNode = currentNode.next
		return False

	def add(self,data):
		if self.size == 0:
			self.root = Node(data)
		else:
			newNode = Node(data)
			newNode.next = self.root
			self.root = newNode
		self.size = self.size + 1

	def remove(self,data):
		if self.root == None:
			return False

		if self.root.data == data:
			self.root = self.root.next
			self.size = self.size - 1
			return True


		currentNode = self.root.next #7
		previousNode = self.root #8
		while currentNode != None: #6
			if currentNode.data == data:
				previousNode.next = currentNode.next
				self.size = self.size - 1
				return True
			previousNode = currentNode #7
			currentNode = currentNode.next #6

		return False

"""
    Tests
"""

list = LinkedList()
list.add(5)
list.add(6)
list.add(7)
list.add(8)
list.remove(6)
list.printList()
list.remove(5)
list.remove(8)
print "Size is ",list.get_size()
