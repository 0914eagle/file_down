
def can_create_rectangles(q, queries):
    results = []
    
    for query in queries:
        n = query[0]
        lengths = query[1]
        
        lengths.sort()
        area = lengths[0] * lengths[-1]
        valid = True
        
        for i in range(n):
            if lengths[i] * lengths[-(i + 1)] != area:
                valid = False
                break
        
        if valid:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

q = int(input())
queries = []
for _ in range(q):
    n = int(input())
    lengths = list(map(int, input().split()))
    queries.append((n, lengths))

results = can_create_rectangles(q, queries)
for result in results:
    print(result)
```
