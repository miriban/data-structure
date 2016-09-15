class Queue:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False

    def enqueue(self,data):
        self.data.append(data)

    def dequeue(self):
        return self.data.pop(0)


# Testing
s = Queue()
s.enqueue(10)
s.enqueue(34)
s.enqueue(3)
s.enqueue(33)

print s.dequeue()
print s.dequeue()
