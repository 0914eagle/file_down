
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def max_nested_paren_level(group: str) -> int:
        max_level = 0
        current_level = 0
        for char in group:
            if char == '(':
                current_level += 1
                max_level = max(max_level, current_level)
            elif char == ')':
                current_level -= 1
        return max_level

    groups = paren_string.split()
    return [max_nested_paren_level(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
