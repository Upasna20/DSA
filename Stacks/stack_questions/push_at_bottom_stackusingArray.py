class Stack:
    def __init__(self, size):
        self.arr = [0] * (size + 1)
        self.size = size + 1
        self.top = -1

    def push(self, val):
        if self.top == self.size - 1:
            print("Stack Overflow")
            exit()
        self.top += 1
        self.arr[self.top] = val

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            exit()
        val = self.arr[self.top]
        self.arr[self.top] = 0
        self.top -= 1
        return val
    
    def is_empty(self):
        return self.top == -1
    
    def peek(self):
        return self.arr[self.top]
    
    def __str__(self):
        return "".join([f'{str(element)}\n' for element in self.arr[::-1]])
    

        
def insert_at_bottom(stack, val):
    if stack.is_empty():
        stack.push(val)
        return
    
    num = stack.pop()
    insert_at_bottom(stack, val)
    stack.push(num)

stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack)
insert_at_bottom(stack, 10)
print(stack)
