class LinkedList:
    def __init__(self, data):
        self.head = self.tail = Node(data)

    def add_at_head(self, data):
        firstNode = Node(data)
        firstNode.next = self.head
        self.head = firstNode

    def add_at_back(self, data):
        endNode = Node(data)
        self.tail.next = endNode
        self.tail = endNode

    def printLL(self):
        curr_node = self.head
        count = 0
        while curr_node != None:
            print(f"{curr_node.data} -> ", end= "")
            curr_node = curr_node.next
            count += 1
        print()

    def reverseLL(self):
        prev_node = None
        curr_node = self.tail = self.head
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        self.head = prev_node

    def isPallindrome(self):
        curr_node = self.head
        data_string = ""
        pallin_string = ""
        while curr_node != None :
            data_string += str(curr_node.data)
            curr_node = curr_node.next
        self.reverseLL()
        rev_node = self.head
        while rev_node != None:
            pallin_string += str(rev_node.data)
            rev_node = rev_node.next
        return data_string == pallin_string

        

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

l1 = LinkedList("b")
l1.add_at_head("c")
l1.add_at_head("a")
l1.add_at_back("d")
l1.printLL()
l1.reverseLL()
l1.printLL()
print(l1.isPallindrome())
    