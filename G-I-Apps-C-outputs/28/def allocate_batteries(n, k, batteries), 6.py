
def allocate_batteries(n, k, batteries):
    batteries.sort()
    start, end = 0, max(batteries) - min(batteries)
    result = float('inf')

    while start <= end:
        mid = start + (end - start) // 2
        if is_possible(n, k, batteries, mid):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1

    return result

def is_possible(n, k, batteries, diff):
    count = 0
    for i in range(0, len(batteries), 2*k):
        if batteries[i + k - 1] - batteries[i] > diff:
            count += 1
    return count <= n

# Sample Input
n, k = 2, 3
batteries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(allocate_batteries(n, k, batteries))
```
