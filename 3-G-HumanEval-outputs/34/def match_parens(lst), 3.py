
def match_parens(lst):
    open_count = 0
    for s in lst:
        for char in s:
            if char == '(':
                open_count += 1
            else:
                if open_count == 0:
                    return 'No'
                open_count -= 1
    return 'Yes'

# Test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'