class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return -1
        val = self.top.data
        self.top = self.top.next
        return val
    
    def is_empty(self):
        return self.top is None

    def peek(self):
        return self.top.data
    
    def printStack(self):
        while not self.is_empty():
            print(self.pop())


def del_mid(stack):
    stack2 = Stack()
    mid = stack.size // 2 + 1
    for i in range(mid - 1):
        stack2.push(stack.pop())

    stack.pop()

    for i in range(mid - 1):
        stack.push(stack2.pop())

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
del_mid(stack)
stack.printStack()



