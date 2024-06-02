
def parse_nested_parens(paren_string: str) -> List[int]:
    
    result = []
    for group in paren_string.split():
        stack = []
        max_depth = 0
        for paren in group:
            if paren == '(':
                stack.append(paren)
            else:
                stack.pop()
            max_depth = max(max_depth, len(stack))
        result.append(max_depth)
    return result
