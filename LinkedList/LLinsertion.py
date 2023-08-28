class LinkedList:
    def __init__(self, data):
        self.head = self.tail = Node(data)
        self.size = 1

    def add_at_front(self, data):
        front_node = Node(data)
        front_node.next = self.head
        self.head = front_node
        self.size += 1

    def add_at_end(self, data):
        end_node = Node(data)
        self.tail.next = end_node
        self.tail = end_node
        self.size += 1

    def printLL(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.data, "->", end=" ")
            curr_node = curr_node.next
    
    def insertLL(self, index, data):
        insert_node = Node(data)
        curr_node = self.head
        for i in range(index - 1):
            prev_node = curr_node
            curr_node = curr_node.next
        insert_node.next = curr_node
        prev_node.next = insert_node
        self.size += 1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    l1 = LinkedList(14)
    l1.add_at_front(30) #70, 30, 14, 28
    l1.add_at_end(28)
    l1.add_at_front(70)
    l1.insertLL(3, 21) #70, 30, 21, 14, 28
    l1.printLL()
    print()
    print("size is",l1.size)