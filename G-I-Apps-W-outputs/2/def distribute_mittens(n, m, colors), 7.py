
def distribute_mittens(n, m, colors):
    distinct_pairs = min(colors.count(i) for i in range(1, m + 1))
    
    print(distinct_pairs * 2)
    
    for i in range(n):
        print(i % m + 1, (i % m + 1) % m + 1)
        
n, m = map(int, input().split())
colors = list(map(int, input().split()))

distribute_mittens(n, m, colors)
```
