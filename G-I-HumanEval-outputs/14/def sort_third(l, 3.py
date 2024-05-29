
def sort_third(l: list):
    new_list = []
    divisible_by_three = []
    for i, val in enumerate(l):
        if i % 3 == 0:
            divisible_by_three.append(val)
        else:
            new_list.append(val)
    new_list.extend(sorted(divisible_by_three))
    return new_list

# Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
```
