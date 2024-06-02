
 def parse_nested_parens(paren_string: str) -> List[int]:
    
    # split the string into a list of strings
    paren_groups = paren_string.split()

    # create a list to store the deepest level of nesting for each group
    deepest_level = []

    # loop through each group of parentheses
    for group in paren_groups:
        # create a stack to keep track of the current level of nesting
        stack = []
        # create a variable to keep track of the deepest level of nesting
        max_level = 0

        # loop through each character in the group
        for char in group:
            # if the character is an opening parenthesis, add it to the stack
            if char == "(":
                stack.append(char)
            # if the character is a closing parenthesis, remove the opening parenthesis from the stack
            elif char == ")":
                stack.pop()
            # if the stack is empty, update the deepest level of nesting
            if not stack:
                max_level += 1

        # add the deepest level of nesting for the current group to the list
        deepest_level.append(max_level)

    return deepest_level

