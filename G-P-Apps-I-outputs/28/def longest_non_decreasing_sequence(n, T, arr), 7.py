
def longest_non_decreasing_sequence(n, T, arr):
    arr_extended = arr * T
    longest_seq = [1] * len(arr_extended)

    for i in range(1, len(arr_extended)):
        for j in range(i):
            if arr_extended[i] >= arr_extended[j]:
                longest_seq[i] = max(longest_seq[i], longest_seq[j] + 1)

    return max(longest_seq)

# Input
n, T = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(longest_non_decreasing_sequence(n, T, arr))
```
