class LinkedList:
    def __init__(self, data):
        self.head = self.tail = Node(data)
    
    def add_at_head(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def add_at_last(self, data):
        # next_node = self.head.next
        # while next_node.next != None:
        #     next_node = next_node.next 
        endNode = Node(data)
        self.tail.next = endNode
        self.tail = endNode
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    

l1 = LinkedList(13)
l1.add_at_head(23546)
l1.add_at_head(34)
print(l1.head.data) # output is 34
# next_node = l1.head.next
# while next_node.next != None:
#     next_node = next_node.next
# print(next_node.data) # output is 13
print(l1.tail.data)
