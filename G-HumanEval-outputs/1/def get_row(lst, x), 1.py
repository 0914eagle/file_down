
def get_row(lst, x):
    result = []
    for row_idx, row in enumerate(lst):
        for col_idx, val in enumerate(row):
            if val == x:
                result.append((row_idx, col_idx))
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)
    return result

# Test cases
print(get_row([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
], 1))  # [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

print(get_row([], 1))  # []

print(get_row([[], [1], [1, 2, 3]], 3))  # [(2, 2)]
```
