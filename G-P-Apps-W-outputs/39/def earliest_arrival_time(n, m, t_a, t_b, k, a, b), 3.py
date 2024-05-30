
def earliest_arrival_time(n, m, t_a, t_b, k, a, b):
    def binary_search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return high

    def possible(time):
        count = 0
        i = 0
        j = binary_search(b, time - t_a)
        while i < n and j < m:
            if b[j] < a[i] + t_a:
                j += 1
                continue
            count += 1
            if count > k:
                return False
            i += 1
            j += 1
        return count <= k

    a.sort()
    b.sort()

    left = max(a[0] + t_a, b[0])
    right = a[-1] + t_a + t_b

    while left < right:
        mid = (left + right) // 2
        if possible(mid):
            right = mid
        else:
            left = mid + 1

    return left if left < a[0] + t_a + t_b else -1

# Input parsing
n, m, t_a, t_b, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Function call and output
print(earliest_arrival_time(n, m, t_a, t_b, k, a, b))
```
