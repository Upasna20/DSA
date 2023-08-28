class Stack:
    def __init__(self):
        self.stack = LinkedList()
        self.size = self.stack.size

    def push(self, val):
        self.stack.add_at_head(val)
        self.size = self.stack.size

    def pop(self):
        if self.size == 0:
            return "StackEmpty"
        val = self.stack.head.data
        self.stack.remove_at_head()
        self.size = self.stack.size
        return val
    

    def print_stack(self):
        if self.size == 0:
            return "StackEmpty"
        self.stack.printLL()

            

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def add_at_head(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def remove_at_head(self):
        self.head = self.head.next 
        self.size -= 1

    def printLL(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.data, "->", end=" ")
            curr_node = curr_node.next

    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

        

stack = Stack()
print(stack.size)
print(stack)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(7)
print(stack.pop())
print(stack.print_stack())

# ll = LinkedList()
# ll.add_at_head(23)
# ll.add_at_head(23)
# ll.add_at_head(24)
# ll.remove_at_head()
# ll.printLL()