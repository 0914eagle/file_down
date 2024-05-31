
def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']' and stack:
            if stack[-1] == '[':
                return True
            else:
                stack.pop()
    return False

# Test cases
print(is_nested('[[]]'))  # True
print(is_nested('[]]]]]]][[[[[]'))  # False
print(is_nested('[][]'))  # False
print(is_nested('[]'))  # False
print(is_nested('[[][]]'))  # True
print(is_nested('[[]][['))  # True
```
