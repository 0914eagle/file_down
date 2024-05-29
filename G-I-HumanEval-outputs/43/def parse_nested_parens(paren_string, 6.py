
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def find_deepest_nesting(paren_group: str) -> int:
        max_depth = 0
        current_depth = 0
        for char in paren_group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    groups = paren_string.split()
    result = [find_deepest_nesting(group) for group in groups]
    return result

# Test cases
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
