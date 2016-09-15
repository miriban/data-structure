class Stack:
    def __init__(self):
        self.data = []

    def push(self,thingToPush):
        self.data.append(thingToPush)

    def pop(self):
        if len(self.data) != 0:
            return self.data.pop(-1)
        return False


# Testing
s = Stack()
s.push(10)


print s.pop()
print s.pop()
