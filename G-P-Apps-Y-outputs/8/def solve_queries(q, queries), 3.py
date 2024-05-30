
def solve_queries(q, queries):
    results = []
    
    for i in range(q):
        n = queries[i][0]
        a = queries[i][1]
        
        a.sort(reverse=True)
        
        max_prettiness = 0
        
        for j in range(n):
            for k in range(j+1, n):
                if a[j] % a[k] != 0:
                    max_prettiness = max(max_prettiness, a[j])
                    
                for l in range(k+1, n):
                    if a[j] % a[l] != 0 and a[k] % a[l] != 0:
                        max_prettiness = max(max_prettiness, a[j] + a[k] + a[l])
                        
        results.append(max_prettiness)
        
    return results


# Input parsing
q = int(input())
queries = []
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    queries.append((n, a))

# Solve queries
results = solve_queries(q, queries)

# Output results
for res in results:
    print(res)
```
