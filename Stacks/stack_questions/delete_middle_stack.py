class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        val = self.head.data
        self.head = self.head.next
        self.size -= 1
        return val
    
    def is_empty(self):
        return self.head is None
    

    def del_helper(self, mid):
        if mid == 1:
            self.pop()
            return
        num = self.pop()
        self.del_helper(mid - 1)
        self.push(num)

    def del_middle(self):
        mid = int(self.size / 2) + 1 
        self.del_helper(mid)

    def printStack(self):
        currNode = self.head
        while currNode:
            print(currNode.data)
            currNode = currNode.next

        


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.printStack()
stack.del_middle()
stack.printStack()
