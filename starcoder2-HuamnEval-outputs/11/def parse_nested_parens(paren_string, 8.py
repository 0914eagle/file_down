
 def parse_nested_parens(paren_string: str) -> List[int]:
    
    paren_string = paren_string.split()
    result = []
    for i in paren_string:
        count = 0
        max_count = 0
        for j in i:
            if j == '(':
                count += 1
            elif j == ')':
                count -= 1
            if count > max_count:
                max_count = count
        result.append(max_count)
    return result
