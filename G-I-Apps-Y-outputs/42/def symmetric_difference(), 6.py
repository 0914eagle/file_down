
def symmetric_difference():
    M = int(input())
    set_M = set(map(int, input().split()))
    N = int(input())
    set_N = set(map(int, input().split()))
    
    symmetric_diff = list((set_M.symmetric_difference(set_N)))
    symmetric_diff.sort()
    
    for num in symmetric_diff:
        print(num)

symmetric_difference()
```
