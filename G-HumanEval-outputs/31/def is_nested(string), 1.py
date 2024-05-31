
def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return True
    
    return False

# Test cases
print(is_nested('[[]]'))  # ➞ True
print(is_nested('[]]]]]]][[[[[]'))  # ➞ False
print(is_nested('[][]'))  # ➞ False
print(is_nested('[]'))  # ➞ False
print(is_nested('[[][]]'))  # ➞ True
print(is_nested('[[]][['))  # ➞ True
```
