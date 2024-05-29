
def check_array_equal(n, arr):
    total_sum = sum(arr)
    if total_sum % n != 0:
        return "NO"
    target = total_sum // n
    count_neg = sum((x - target) % 2 for x in arr)
    return "YES" if count_neg == 0 or count_neg == n else "NO"

n = int(input())
arr = list(map(int, input().split()))

result = check_array_equal(n, arr)
print(result)
```
