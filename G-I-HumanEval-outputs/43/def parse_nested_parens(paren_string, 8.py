
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    max_depth = 0
    depth = 0

    for char in paren_string:
        if char == '(':
            depth += 1
            if depth > max_depth:
                max_depth = depth
        elif char == ')':
            depth -= 1

    depths.append(max_depth)

    return depths

# Test the function
result = parse_nested_parens('(()()) ((())) () ((())()())')
print(result)  # Output should be [2, 3, 1, 3]
