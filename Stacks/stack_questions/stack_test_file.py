from sort_a_stack_recur import Stack

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack)
    stack.sort_the_stack()
    print(stack)

if __name__ == "__main__":
    main()

    
