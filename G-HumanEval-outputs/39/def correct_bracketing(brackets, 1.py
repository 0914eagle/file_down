
def correct_bracketing(brackets: str):
    stack = []
    
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        elif bracket == ">":
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0

print(correct_bracketing("<"))  # Output: False
print(correct_bracketing("<>"))  # Output: True
print(correct_bracketing("<<><>>"))  # Output: True
print(correct_bracketing("><<>"))  # Output: False
