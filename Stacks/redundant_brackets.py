from stack_list_implementation import Stack

INPUT_DATA = "(a + (b + c))"
DATA = {")": "(", "}": "{", "]": "["}
OPENING = "({["
CLOSING = ")}]"

stack = Stack()

def redundancy_checker(item, stack):
    count = 0
    while stack.peek() not in OPENING:
        count += 1
        stack.pop()
    # print(count)
    if stack.peek() != DATA[item]:
        print("brackets not proper")
        return True
    else:
        stack.pop()
    
    if count < 2:
        print("redundant bracket")
        return True
    
    

def is_redundant(INPUT_DATA, stack):
    flag = False
    for item in INPUT_DATA:
        if item not in CLOSING:
            stack.push(item)

        else:
            flag = redundancy_checker(item, stack)
            
        if flag:
            return flag
    return False
print(is_redundant(INPUT_DATA, stack))