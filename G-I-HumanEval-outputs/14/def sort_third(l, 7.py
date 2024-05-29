
def sort_third(l: list):
    indices_divisible_by_three = [i for i in range(len(l)) if i % 3 == 0]
    sorted_values = [l[i] for i in indices_divisible_by_three]
    sorted_values.sort()
    
    sorted_list = l[:]
    for i in indices_divisible_by_three:
        sorted_list[i] = sorted_values.pop(0)
    
    return sorted_list

# Test cases
print(sort_third([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Output: [2, 6, 3, 4, 8, 9, 5]
```
