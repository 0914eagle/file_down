
def sort_third(l: list):
    result = l.copy()
    divisible_by_three = [i for i in range(len(l)) if i % 3 == 0]
    divisible_values = [l[i] for i in divisible_by_three]
    sorted_values = sorted(divisible_values)

    for i, val in zip(divisible_by_three, sorted_values):
        result[i] = val

    return result

# Test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
```
