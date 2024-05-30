
def solve_query(n, problems):
    problems.sort(reverse=True)
    max_prettiness = 0
    
    if n >= 3:
        max_prettiness = max(max_prettiness, problems[0] + problems[1] + problems[2])
    
    max_prettiness = max(max_prettiness, problems[0])
    
    for i in range(1, n):
        for j in range(i+1, n):
            if problems[i] % problems[j] != 0 and problems[j] % problems[i] != 0:
                max_prettiness = max(max_prettiness, problems[0] + problems[i] + problems[j])
    
    return max_prettiness

q = int(input())
for _ in range(q):
    n = int(input())
    problems = list(map(int, input().split()))
    result = solve_query(n, problems)
    print(result)
```
