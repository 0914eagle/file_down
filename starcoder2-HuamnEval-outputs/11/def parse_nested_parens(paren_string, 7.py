
 def parse_nested_parens(paren_string: str) -> List[int]:
    
    paren_string = paren_string.split()
    result = []
    for paren in paren_string:
        level = 0
        max_level = 0
        for char in paren:
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            elif char == ')':
                level -= 1
        result.append(max_level)
    return result
