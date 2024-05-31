
def is_nested(string):
    stack = []
    nested = False
    
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if stack and stack[-1] == '[':  # Check if there is a matching opening bracket
                nested = True
                break
            else:
                stack.pop()
    
    return nested

# Test cases
print(is_nested('[[]]'))  # ➞ True
print(is_nested('[]]]]]]][[[[[]'))  # ➞ False
print(is_nested('[][]'))  # ➞ False
print(is_nested('[]'))  # ➞ False
print(is_nested('[[][]]'))  # ➞ True
print(is_nested('[[]][['))  # ➞ True
