class Stack:
    def __init__(self, size):
        self.arr = [0] * size 
        self.size = size
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
        if self.is_empty():
            return -1
        return self.arr[self.top]
    
    def __str__(self):
        return "".join([f"{str(element)}\n" for element in self.arr[::-1]])
    


def solve(stack, mid):
    if mid == 1:
        stack.pop()
        return 

    num = stack.pop()
    solve(stack, mid - 1)
    stack.push(num)

def del_mid(stack):
    mid = stack.size // 2 + 1
    solve(stack, mid)
    
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack)
del_mid(stack)
print(stack)

