
def find_min_operations(n, arr):
    operations = []
    min_ops = 0

    while len(set(arr)) > 1:
        max_diff = 0
        max_diff_idx = -1

        for i in range(n - 1):
            diff = abs(arr[i] - arr[i + 1])
            if diff > max_diff:
                max_diff = diff
                max_diff_idx = i

        if arr[max_diff_idx] < arr[max_diff_idx + 1]:
            operations.append((1, max_diff_idx + 1, max_diff_idx + 2))
            arr[max_diff_idx] += max_diff
        else:
            operations.append((2, max_diff_idx + 1, max_diff_idx + 2))
            arr[max_diff_idx] -= max_diff

        min_ops += 1

    print(min_ops)
    for operation in operations:
        print(' '.join(str(x) for x in operation))

# Input parsing
n = int(input())
arr = list(map(int, input().split()))

# Call the function
find_min_operations(n, arr)
```
