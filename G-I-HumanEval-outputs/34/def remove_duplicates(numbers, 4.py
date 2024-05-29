
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    output = []
    seen = set()
    
    for num in numbers:
        if num not in seen:
            output.append(num)
            seen.add(num)
    
    return output

print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
