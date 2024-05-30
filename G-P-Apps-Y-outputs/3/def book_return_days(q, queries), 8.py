
def book_return_days(q, queries):
    results = []
    
    for query in queries:
        n = query[0]
        p = query[1]
        
        days_to_return = [0] * n
        visited = [False] * n
        
        for i in range(n):
            if visited[i]:
                continue
            
            count = 0
            j = i
            
            while not visited[j]:
                visited[j] = True
                j = p[j] - 1
                count += 1
            
            days_to_return[i] = count
        
        results.append(days_to_return)
    
    return results

q = int(input())
queries = []
for _ in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    queries.append((n, p))

results = book_return_days(q, queries)

for result in results:
    print(*result)
```
