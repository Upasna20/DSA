class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return "StackEmpty"
        val = self.head
        self.head = self.head.next
        self.size -= 1
        return val
    
    def printStack(self):
        if self.size == 0:
            return "StackEmpty"
        curr_node = self.head
        while curr_node != None:
            print(curr_node.data, "->", end=" ")
            curr_node = curr_node.next

    def is_empty(self):
        return self.size == 0

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

if __name__ == "__main__":
    stack = Stack()
    stack.push(23)
    stack.push(45)
    stack.push('upasna')
    stack.push(2)
    print(stack.pop())
    stack.printStack()
