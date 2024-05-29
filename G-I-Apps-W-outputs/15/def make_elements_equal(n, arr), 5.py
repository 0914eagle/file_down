
def make_elements_equal(n, arr):
    min_num = min(arr)
    max_num = max(arr)
    diff = max_num - min_num
    count_diff = 0
    for num in arr:
        if num != min_num:
            count_diff += 1
    if count_diff <= 1 or diff == 0 or diff % count_diff == 0:
        print("YES")
    else:
        print("NO")

n = int(input())
arr = list(map(int, input().split()))
make_elements_equal(n, arr)
```
