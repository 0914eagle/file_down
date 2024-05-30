
def max_prettiness_contest(q, queries):
    results = []
    
    for query in queries:
        n = query[0]
        problems = query[1]
        problems.sort(reverse=True)
        
        max_prettiness = 0
        
        if n >= 1:
            max_prettiness = max(max_prettiness, problems[0])
        
        if n >= 2:
            max_prettiness = max(max_prettiness, problems[0] + problems[1])
            if problems[0] % problems[1] != 0 and problems[1] % problems[0] != 0:
                max_prettiness = max(max_prettiness, problems[0] + problems[1])
        
        if n >= 3:
            max_prettiness = max(max_prettiness, problems[0] + problems[1] + problems[2])
            if problems[0] % problems[1] != 0 and problems[1] % problems[0] != 0 and problems[0] % problems[2] != 0 and problems[2] % problems[0] != 0 and problems[1] % problems[2] != 0 and problems[2] % problems[1] != 0:
                max_prettiness = max(max_prettiness, problems[0] + problems[1] + problems[2])
        
        results.append(max_prettiness)
    
    return results

# Input
q = 3
queries = [
    (4, [5, 6, 15, 30]),
    (4, [10, 6, 30, 15]),
    (3, [3, 4, 6])
]

# Output
output = max_prettiness_contest(q, queries)
for result in output:
    print(result)
```
