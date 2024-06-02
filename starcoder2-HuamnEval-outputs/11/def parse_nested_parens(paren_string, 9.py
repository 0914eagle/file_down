
 def parse_nested_parens(paren_string: str) -> List[int]:
    
    # split the string into a list of strings
    paren_list = paren_string.split()
    # initialize a list to store the max depth of each group
    max_depth_list = []
    # loop through each group
    for group in paren_list:
        # initialize a counter for the max depth of each group
        max_depth = 0
        # initialize a counter for the current depth of each group
        current_depth = 0
        # loop through each character in the group
        for char in group:
            # if the character is an opening parenthesis, increase the current depth
            if char == '(':
                current_depth += 1
            # if the character is a closing parenthesis, decrease the current depth
            elif char == ')':
                current_depth -= 1
            # update the max depth if the current depth is greater than the max depth
            if current_depth > max_depth:
                max_depth = current_depth
        # append the max depth to the list of max depths
        max_depth_list.append(max_depth)
    # return the list of max depths
    return max_depth_list
