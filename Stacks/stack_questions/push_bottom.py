class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None
    
    def push(self, val):
        self.size += 1
        new_node = Node(val)
        if self.is_empty():
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node
       

    def pop(self):
        val = self.head.data
        if self.is_empty():
            return -1
        self.head = self.head.next
        self.size -= 1
        return val
    
    def peek(self):
        if self.is_empty():
            return False
        return self.head.data
    
# push an element to the bottom of the stack maintaining the existing stack order.
    def push_at_bottom(self, val): # O(n) space complexity, O(n) time complexity
        stack2 = Stack() 
        while not self.is_empty():
            stack2.push(self.pop())
        self.push(val)
        while not stack2.is_empty():
            self.push(stack2.pop())
        

    def push_at_bottom_rec(self, val):  # O(1) space complexity, O(n) time complexity
        if self.is_empty(): # you don't need to create any other stack here, recursion in itself uses an implicit stack.
            self.push(val)
            return
        num = self.pop()
        self.push_at_bottom_rec(val)
        return self.push(num)
    
    def reverse(self):
        if self.is_empty():
            return
        num = self.pop()
        self.reverse()
        self.push_at_bottom_rec(num)
    

    def __str__(self):
        if self.is_empty():
            return -1
        container = []
        curr_node = self.head
        while curr_node != None:
            container.append(f"{curr_node.data}\n")
            curr_node = curr_node.next

        return "".join(container)
stack = Stack()
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(7)
stack.pop()
stack.push_at_bottom(2)
stack.push_at_bottom(19)
stack.push_at_bottom_rec(20)
# stack.push_at_bottom(1)
# stack.push_at_bottom_rec(1)
print(stack)
stack.reverse()
print(stack)