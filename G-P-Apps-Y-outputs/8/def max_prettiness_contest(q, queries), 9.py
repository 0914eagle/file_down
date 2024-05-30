
def max_prettiness_contest(q, queries):
    results = []
    
    for query in queries:
        n = query[0]
        problems = query[1]
        problems.sort(reverse=True)
        
        max_prettiness = 0
        
        if n >= 3:
            for i in range(3):
                for j in range(i+1, 3):
                    for k in range(j+1, 3):
                        if problems[i] % problems[j] != 0 and problems[j] % problems[k] != 0 and problems[i] % problems[k] != 0:
                            max_prettiness = max(max_prettiness, problems[i] + problems[j] + problems[k])
        elif n == 2:
            if problems[0] % problems[1] != 0:
                max_prettiness = sum(problems)
            else:
                max_prettiness = max(problems)
        else:
            max_prettiness = max(problems)
        
        results.append(max_prettiness)
    
    return results

# Input
queries = [
    (4, [5, 6, 15, 30]),
    (4, [10, 6, 30, 15]),
    (3, [3, 4, 6])
]

# Number of queries
q = 3

# Running the function
output = max_prettiness_contest(q, queries)
for result in output:
    print(result)
```
