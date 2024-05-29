
def sort_third(l: list):
    sorted_thirds = sorted([l[i] for i in range(len(l)) if i % 3 == 0])
    return [sorted_thirds.pop(0) if i % 3 == 0 else value for i, value in enumerate(l)]

# Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
```
