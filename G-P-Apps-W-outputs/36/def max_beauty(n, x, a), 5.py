
def max_beauty(n, x, a):
    def max_sum(arr):
        curr_max = 0
        max_so_far = 0
        for num in arr:
            curr_max = max(num, curr_max + num)
            max_so_far = max(max_so_far, curr_max)
        return max_so_far

    original_max = max_sum(a)
    multiplied_max = max_sum([num if num > 0 else num * x for num in a])
    return max(original_max, multiplied_max)

# Input
n, x = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(max_beauty(n, x, a))
```
