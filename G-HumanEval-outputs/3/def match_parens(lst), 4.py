
def match_parens(lst):
    left_count = 0
    right_count = 0
    
    for s in lst:
        for char in s:
            if char == '(':
                left_count += 1
            elif char == ')':
                if left_count > 0:
                    left_count -= 1
                else:
                    right_count += 1
    
    if left_count == 0 and right_count <= 1:
        return 'Yes'
    else:
        return 'No'

# Test cases
print(match_parens(['()(', ')']))  # 'Yes'
print(match_parens([')', ')']))     # 'No'
