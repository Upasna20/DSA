import sys
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
            return -sys.maxsize - 1
        return self.arr[self.top]
    
    def __str__(self):
        return "".join([f'{str(element)}\n' for element in self.arr[::-1]])
    

# def sort_push(stack, temp_stack):
#     # print("In sort_push function")
#     # print(stack)
#     # print(temp_stack)
    
#     while not temp_stack.is_empty():
#         a = temp_stack.pop()
#         count = 0
#         if stack.
            
#         # while not stack.is_empty() and stack.peek() is not None and stack.peek() > a:
#         # while not stack.is_empty() and (stack.peek() is not None) and (stack.peek() > a):
#         # while stack.peek() > a:/
#             # print(type(stack.peek()))
#             # print(type(a))
#             while stack.peek() > a:
               
               
#                 temp_stack.push(stack.pop())
              
#                 count += 1
        
   
#         stack.push(a)
    

#         for i in range(count):
#             stack.push(temp_stack.pop())
           



def sort_the_stack(stack):
    temp_stack = Stack(stack.size)

    while not stack.is_empty():
        count = 0
        a = stack.pop()
        while True :
            if temp_stack.is_empty() or temp_stack.peek() < a:
                temp_stack.push(a)
                break
            stack.push(temp_stack.pop())
            count += 1
        for i in range(count):
            temp_stack.push(stack.pop())
        
        
    print(temp_stack)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

stack = Stack(5)
stack.push(1)
stack.push(3)
stack.push(2)
stack.push(5)
stack.push(4)
print(stack)
sort_the_stack(stack)
print(stack)
