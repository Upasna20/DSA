from better_stack_implementation import Stack
BRACKET_SET = "{([](}))}"

BRACKET_PAIR = {"(": ")", "{": "}", "[": "]"}
func_tion = [Stack.push, Stack.pop]


def parse(bracket=BRACKET_SET) -> list[str]:
    return list(bracket)

                
def choose_method(bracket_type: str) ->  str:
    if bracket_type in "[{(":
        return 0
    elif bracket_type in ")}]":
        return 1
    else:
        return "Input needs to be a single bracket nothing else"
    
def main():
    stack = Stack()
    for bracket in parse():
        func = choose_method(bracket)
        if func == "Input needs to be a single bracket nothing else":
            return func
        if func == 1:
            if BRACKET_PAIR[stack.head.data] != bracket:
                return "Invalid Brackets"
            func_tion[func](stack)
        else:
            func_tion[func](stack, bracket) # a new approach of sending self because our func_tion sent the class's method as the method which doesn't know of the instanstiated object.
    
    if stack.size != 0:
        return "Invalid Brackets"
    return "Valid Brackets"

print(main())




