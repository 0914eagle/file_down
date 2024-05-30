
def max_prettiness_contest(q, queries):
    results = []
    
    for _ in range(q):
        n = queries[_][0]
        a = queries[_][1]
        
        a.sort(reverse=True)
        
        max_prettiness = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if a[i] % a[j] != 0:
                    max_prettiness = max(max_prettiness, a[i])
                for k in range(j+1, n):
                    if a[i] % a[j] != 0 and a[j] % a[k] != 0 and a[i] % a[k] != 0:
                        max_prettiness = max(max_prettiness, a[i] + a[j] + a[k])
        
        results.append(max_prettiness)
    
    return results

# Input parsing
q = int(input())
queries = []
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    queries.append((n, a))

# Call the function and print the results
results = max_prettiness_contest(q, queries)
for res in results:
    print(res)
```
