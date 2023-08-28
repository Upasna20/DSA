class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self, value: int):
        self.head = self.tail = Node(value)
        self.size = 1
    
    def add_at_head(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_at_back(self, value: int) -> None:
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        new_node.next = None
        self.size += 1
    
    def printLL(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.data, "->", end=" ")
            curr_node = curr_node.next
        print()

    # def reverse_sliceLL(self, pos) -> None:
    #     curr_node = self.head
    #     for i in range(pos - 1):
    #         prev_node = curr_node
    #         curr_node = curr_node.next
    #     link_node = prev_node
    #     pseudo_head = curr_node
    #     while curr_node != None:
    #         next_node = curr_node.next
    #         curr_node.next = prev_node
    #         prev_node = curr_node
    #         curr_node = next_node
        
    #     pseudo_head.next = None
    #     link_node.next = prev_node
    def getNode(self, pos: int):
        curr_node = self.head
        for i in range(pos - 1):
            curr_node = curr_node.next
        return curr_node

    def reverseLL(self, start = 1, end = None):
        if end is None:
            end = self.size
        start_node = prev_node = self.getNode(start)
        curr_node = prev_node.next 
        for i in range(start, end):  # i have the idea of putting all of the reverse for loop code in a separate function
            next_node = curr_node.next  # but then it would lead to a reverse function with lots of parameter, what do you
            curr_node.next = prev_node # recommend would that be a good practice to ensure modularity?
            prev_node = curr_node
            curr_node = next_node
        
        start_node.next = curr_node
        if start == 1:
            self.head = prev_node
        else:
            self.getNode(start - 1).next = prev_node # in the second version this is already stored in link_node to reduce the number of iterations, since it stores the start_node as link_node.next

    # def slice_reverseLL(self, start = 1, end = None):
    #     if end == None:
    #         end = self.size
    #     real_start = start - 1
    #     real_end = end - 1

    #     if real_start == 0:
    #         start_Node = prev_node = self.getNode(real_start)
    #     else:
    #         link_node = self.getNode(real_start - 1)
    #         start_Node = prev_node = link_node.next
    #     curr_node = prev_node.next
    #     for i in range(real_start, real_end):
    #         next_node = curr_node.next 
    #         curr_node.next = prev_node
    #         prev_node = curr_node
    #         curr_node = next_node
        
    #     start_Node.next = curr_node
    #     if real_start == 0:
    #         self.head = prev_node
    #     else:
    #         link_node.next = prev_node

    def isPalindrome(self):  # with space complexity O(1), constant space complexity
        if self.size % 2 == 0:       #is the slow fast approach better here, i mean i don't see the reason to go with that approach.
            mid = int((self.size) / 2 + 1)
        else:
            mid = int((self.size + 1) / 2 + 1)

        self.reverseLL(mid)
        pointer1 = self.head
        pointer2 = self.getNode(mid)
        while pointer2 != None:
            if pointer1.data != pointer2.data:
                return False
            pointer2 = pointer2.next
            pointer1 = pointer1.next
        return True
    

    def is_loop(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None : # this is an important condition, look into this.
            # if fast.next == None:
            #     return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            
        return False
    
    def remove_common_node(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            prev = fast
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    prev = prev.next
                    slow = slow.next
                    fast = fast.next
                prev.next.next = None
                return
                
        return "No cycle found"


            

    


       


        



l1 = LinkedList("d")
# l1.printLL()
l1.add_at_head("a")
# l1.printLL()
l1.add_at_head("ji")
# l1.printLL()
l1.add_at_back("d")
# l1.printLL()
l1.add_at_back("a")
# l1.printLL()
l1.add_at_back("m")
l1.tail.next = l1.head
# l1.printLL()
print(l1.is_loop())
l1.remove_common_node()
print(l1.is_loop())
# l1.add_at_head(0)
# l1.reverseLL()
# l1.slice_reverseLL(2, 5)
# print(l1.isPalindrome())
# l1.printLL() 
