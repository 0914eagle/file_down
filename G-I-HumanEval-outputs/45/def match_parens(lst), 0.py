
def match_parens(lst):
    # Create a variable to keep track of the balance of parentheses
    balance = 0
    
    # Iterate through each string in the list
    for s in lst:
        for char in s:
            if char == '(':
                balance += 1
            else:
                if balance == 0:
                    return 'No'  # More close parentheses than open parentheses
                balance -= 1
    
    if balance == 0:
        return 'Yes'
    else:
        return 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'
```
