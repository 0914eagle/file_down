
def good_indices(n, arr):
    if n < 3:
        print(0)
        return

    total_sum = sum(arr)
    good_indices = []
    for i in range(n):
        if (total_sum - arr[i]) % 2 == 0 and (total_sum - arr[i]) // 2 in arr[:i] + arr[i+1:]:
            good_indices.append(i+1)

    print(len(good_indices))
    if len(good_indices) > 0:
        print(' '.join(map(str, good_indices)))

# Reading input
n = int(input())
arr = list(map(int, input().split()))

# Call the function
good_indices(n, arr)
```
