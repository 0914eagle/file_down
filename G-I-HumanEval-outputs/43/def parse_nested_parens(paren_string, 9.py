
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def max_depth(s: str) -> int:
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        return max_depth

    groups = paren_string.split()
    return [max_depth(group) for group in groups]

# Testing the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
