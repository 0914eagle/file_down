
def is_nested(string):
    opened_brackets = 0
    for char in string:
        if char == '[':
            opened_brackets += 1
        elif char == ']':
            if opened_brackets > 0:
                opened_brackets -= 1
    return opened_brackets < 0

# Test cases
print(is_nested('[[]]'))  # ➞ True
print(is_nested('[]]]]]]][[[[[]'))  # ➞ False
print(is_nested('[][]'))  # ➞ False
print(is_nested('[]'))  # ➞ False
print(is_nested('[[][]]'))  # ➞ True
print(is_nested('[[]][['))  # ➞ True
```
