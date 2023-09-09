from stack_list_implementation import Stack
INPUT_DATA = "}}}}{{{{"
OPENING = "{"
CLOSING = "}"
DATA = {"}": "{"}
count = 0

stack = Stack()

for item in INPUT_DATA:
    if item in OPENING:
        stack.push(item)
    
    if item in CLOSING:
        if stack.is_empty():
            count += 1
            stack.push("{")
        else:
            stack.pop()
if stack.stack_size == 0:
    print(count)

elif stack.stack_size % 2 == 0:
    if count != 0:
        print(stack.stack_size // 2 + count)
    else:
        print(stack.stack_size // 2)

else:
    print(-1)