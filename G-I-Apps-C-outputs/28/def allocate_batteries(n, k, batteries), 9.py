
def allocate_batteries(n, k, batteries):
    batteries.sort()
    
    l, r = 0, max(batteries)
    ans = r
    
    while l <= r:
        mid = (l + r) // 2
        possible = True
        for i in range(0, 2*n*k, 2*k):
            if batteries[i + k - 1] - batteries[i] > mid:
                possible = False
                break
        if possible:
            ans = min(ans, mid)
            r = mid - 1
        else:
            l = mid + 1
    
    return ans

# Input
input_line = input().split()
n = int(input_line[0])
k = int(input_line[1])

batteries = list(map(int, input().split()))

# Output
print(allocate_batteries(n, k, batteries))
```
