
def min_integers_to_insert(n, array):
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i+1] = prefix_sums[i] + array[i]

    count = 0
    prefix_sum_set = set()
    for i in range(1, n+1):
        if prefix_sums[i] in prefix_sum_set:
            count += 1
            prefix_sum_set = set([prefix_sums[i]])
        prefix_sum_set.add(prefix_sums[i])

    return count

# Read input
n = int(input())
array = list(map(int, input().split()))

# Call the function and print the result
print(min_integers_to_insert(n, array))
```
