class Stack:
    def __init__(self, n) -> None:
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
        self.arr[self.top - 1] = 0
        self.top -= 1

    def is_empty(self):
        return not any(self.arr)
    
    def __str__(self):
        return "".join([f"{str(element)}\n" for element in self.arr[::-1]])
    




