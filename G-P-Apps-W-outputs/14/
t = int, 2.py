
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    total_visitors = min(a, b, c)
    
    if a > b and a > c:
        total_visitors += min(a-1, b, c)
    elif b > a and b > c:
        total_visitors += min(b-1, a, c)
    elif c > a and c > b:
        total_visitors += min(c-1, a, b)
    
    print(total_visitors)

```
