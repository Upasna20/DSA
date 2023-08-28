class LinkedList:
    def __init__(self, data: int):
        self.Head = Node(data)
    

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
    
ll = LinkedList(23)
print(ll.Head.data)