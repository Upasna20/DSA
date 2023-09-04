class Stack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0
    
    def push(self, val):
        self.stack_list.append(val)
        self.stack_size += 1
    
    def pop(self):
        self.stack_size -= 1
        return self.stack_list.pop()
    
    def peek(self):
        return self.stack_list[-1]
    
    def is_empty(self):
        return self.stack_size == 0
    
    def __str__(self):
        return "".join([f"{element}\n" for element in self.stack_list])
    
    def insert_sorted(self, val):
        # if val < self.peek() or self.is_empty(): # here this arrangement of the condition gives an error because
        # if empty condition is not checked first, then in case of empty stack the self.peek fails to throw an error
        #thus if self.empty is true it won't check for the peek condition and it would pass on.
        if self.is_empty() or val < self.peek():
            return self.push(val)
        
        num = self.pop()
        self.insert_sorted(val)
        self.push(num)

    def sort_the_stack(self):
        if self.is_empty():
            return
        num = self.pop()
        self.sort_the_stack()
        self.insert_sorted(num)


