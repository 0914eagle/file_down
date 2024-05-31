
def match_parens(lst):
    # Concatenate the two strings in the list
    combined_string = lst[0] + lst[1]

    # Initialize a stack to keep track of open parentheses
    stack = []

    # Check each character in the combined string
    for char in combined_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # If stack is not empty and top of stack is '(', pop '('
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 'No'  # Unbalanced parenthesis found

    # If stack is empty at the end, all parentheses are balanced
    if not stack:
        return 'Yes'
    else:
        return 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: Yes
print(match_parens([')', ')']))    # Output: No
```
