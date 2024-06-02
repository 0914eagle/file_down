
def parse_nested_parens(paren_string: str) -> List[int]:
    
    def helper(paren_string: str, start: int, end: int) -> int:
        
        if start > end:
            return 0
        max_depth = 0
        depth = 0
        for i in range(start, end + 1):
            if paren_string[i] == '(':
                depth += 1
            elif paren_string[i] == ')':
                depth -= 1
            max_depth = max(max_depth, depth)
        return max_depth

    paren_string = paren_string.strip()
    if not paren_string:
        return []
    res = []
    start = 0
    for i in range(len(paren_string)):
        if paren_string[i] == ' ':
            res.append(helper(paren_string, start, i - 1))
            start = i + 1
    res.append(helper(paren_string, start, len(paren_string) - 1))
    return res
