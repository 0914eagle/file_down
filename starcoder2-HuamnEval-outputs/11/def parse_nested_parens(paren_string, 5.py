
def parse_nested_parens(paren_string: str) -> List[int]:
    
    # split the string into individual groups
    groups = paren_string.split()
    # initialize an empty list to store the results
    results = []
    # loop through each group
    for group in groups:
        # initialize a counter for the nesting level
        nesting_level = 0
        # initialize a counter for the current level of nesting
        current_level = 0
        # loop through each character in the group
        for char in group:
            # if the character is an opening parenthesis, increase the nesting level
            if char == '(':
                nesting_level += 1
            # if the character is a closing parenthesis, decrease the nesting level
            elif char == ')':
                nesting_level -= 1
            # if the nesting level is greater than the current level, update the current level
            if nesting_level > current_level:
                current_level = nesting_level
        # append the current level to the results list
        results.append(current_level)
    # return the results list
    return results
 