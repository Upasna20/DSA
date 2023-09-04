class Stack:
    def __init__(self, n):
        self.arr = [0] * n
        self.top = 0
        self.size = n

    def push(self, val):
        if self.top >= self.size:
            return "Stack Overflow"
        self.arr[self.top] = val
        self.top += 1
        
    def pop(self):
        if self.top <= 0:
            return "Stack Underflow"
        val = self.arr[self.top - 1]
        self.arr[self.top - 1] = 0
        self.top -= 1
        return val

    def is_empty(self):
        return not any(self.arr)
    
    def push_at_bottomRec(self, val):
        #base_statement: when the count == 0, store the popped value and push the val at count , return the popped value
        #recurseive_statement: store the popped value and since the count > 0, call the function again, while returning, 
        # you come to this stack again and then push the returned value returning the popped value
        num = self.pop()
        if self.top == 0:
            self.push(val)
            return num
        num2 = self.push_at_bottomRec(val)
        self.push(num2)
        return num
    
    def __str__(self):
        return "".join([f"{str(element)}\n" for element in self.arr[::-1]])

stack = Stack(4)
stack.push(2)
stack.push(3)
stack.push(4)
# stack.push(stack.push_at_bottomRec(1))
stack.push_at_bottomRec(1)
print(stack)

