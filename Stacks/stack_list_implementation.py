class Stack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0
    
    def is_empty(self):
        return self.stack_size == 0
    
    def peek(self):
        return self.stack_list[-1]
    
    def push(self, value):
        self.stack_list.append(value)
        self.stack_size += 1

    def pop(self):
        if self.is_empty():
            return -1
        self.stack_size -= 1
        return self.stack_list.pop()
    
    def __str__(self):
        return str(self.stack_list)
    
