
def max_prettiness_contest(q, queries):
    results = []
    
    for query in queries:
        n = query[0]
        prettiness = sorted(query[1], reverse=True)
        
        max_prettiness = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if prettiness[i] % prettiness[j] != 0 and prettiness[j] % prettiness[i] != 0:
                    max_prettiness = max(max_prettiness, prettiness[i] + prettiness[j])
                for k in range(j+1, n):
                    if prettiness[i] % prettiness[j] != 0 and prettiness[j] % prettiness[i] != 0 and prettiness[i] % prettiness[k] != 0 and prettiness[j] % prettiness[k] != 0 and prettiness[k] % prettiness[i] != 0 and prettiness[k] % prettiness[j] != 0:
                        max_prettiness = max(max_prettiness, prettiness[i] + prettiness[j] + prettiness[k])
        
        results.append(max_prettiness)
    
    return results

# Input
queries = [(4, [5, 6, 15, 30]), (4, [10, 6, 30, 15]), (3, [3, 4, 6])]
q = 3

# Output
output = max_prettiness_contest(q, queries)
for result in output:
    print(result)
```
