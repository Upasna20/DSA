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
        self.top -= 1
        return val
    
    def is_empty(self):
        return self.top == -1
    
    def peek(self):
        if self.is_empty():
            return -1
        return self.arr[self.top]
    
    def __str__(self):
        return "".join([f"{str(element)}\n" for element in self.arr])


staack = Stack(6)
print(staack)

SAMPLE_STRING = "upasna"
def stack_convertor(string_sample):
    stack = Stack(len(string_sample))
    for i in string_sample:
        stack.push(i)
    return stack

def reverse_string(string_sample):
    stack = stack_convertor(string_sample)
    Rev_String = ""
    while not stack.is_empty():
        Rev_String += stack.pop()

    return Rev_String

print(reverse_string(SAMPLE_STRING))

