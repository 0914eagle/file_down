
 def parse_nested_parens(paren_string: str) -> List[int]:
    
    # split the string into a list of strings
    paren_list = paren_string.split()
    # initialize a list to store the result
    result = []
    # iterate through the list of strings
    for paren in paren_list:
        # initialize a variable to store the current level of nesting
        current_level = 0
        # initialize a variable to store the deepest level of nesting
        deepest_level = 0
        # iterate through each character in the string
        for char in paren:
            # if the character is an opening parenthesis, increment the current level of nesting
            if char == '(':
                current_level += 1
            # if the character is a closing parenthesis, decrement the current level of nesting
            elif char == ')':
                current_level -= 1
            # update the deepest level of nesting if the current level is deeper
            if current_level > deepest_level:
                deepest_level = current_level
        # append the deepest level of nesting to the result list
        result.append(deepest_level)
    # return the list of deepest levels of nesting
    return result

