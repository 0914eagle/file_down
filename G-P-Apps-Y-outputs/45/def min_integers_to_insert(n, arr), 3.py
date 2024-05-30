
def min_integers_to_insert(n, arr):
    prefix_sums = [0]
    for num in arr:
        prefix_sums.append(prefix_sums[-1] + num)

    count = 0
    sum_counts = {}
    for prefix_sum in prefix_sums:
        if prefix_sum in sum_counts:
            count = max(count, sum_counts[prefix_sum] + 1)
        sum_counts[prefix_sum] = count

    return count

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(min_integers_to_insert(n, arr))
```
