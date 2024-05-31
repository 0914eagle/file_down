
def match_parens(lst):
    s = lst[0] + lst[1]
    count = 0
    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return 'No'
    if count == 0:
        return 'Yes'
    return 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))  # Output: 'No'
