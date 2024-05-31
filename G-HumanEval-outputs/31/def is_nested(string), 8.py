
def is_nested(string):
    stack = []
    
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']' and stack and stack[-1] == '[':
            stack.pop()
    
    return len(stack) < len(string) and len(stack) > 0

# Test cases
print(is_nested('[[]]'))      # ➞ True
print(is_nested('[]]]]]]][[[[[]'))  # ➞ False
print(is_nested('[][]'))       # ➞ False
print(is_nested('[]'))         # ➞ False
print(is_nested('[[][]]'))     # ➞ True
print(is_nested('[[]][['))     # ➞ True
```
