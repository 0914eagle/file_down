
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def count_nested_levels(s):
        max_depth = 0
        current_depth = 0
        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        return max_depth

    groups = paren_string.split()
    results = [count_nested_levels(group) for group in groups]
    return results

print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
