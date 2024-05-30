
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    total_visitors = 0
    
    for i in range(8):
        dumplings = min(i, a)
        cranberry = min(i // 2, b)
        pancakes = min(i // 2, c)
        
        total_dishes = dumplings + cranberry + pancakes
        
        if total_dishes == i:
            total_visitors = i
    
    print(total_visitors)
```
