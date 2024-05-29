
def match_parens(lst):
    first_string = lst[0]
    second_string = lst[1]

    total_open_count = first_string.count('(') + second_string.count('(')
    total_close_count = first_string.count(')') + second_string.count(')')

    if total_open_count == total_close_count:
        return 'Yes'
    else:
        return 'No'

# Test cases
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens([')', ')']))     # Output: 'No'
