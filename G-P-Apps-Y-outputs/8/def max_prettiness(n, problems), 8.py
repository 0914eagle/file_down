
def max_prettiness(n, problems):
    problems.sort(reverse=True)
    
    max_prettiness = 0
    
    # Case 1: Choose one problem
    max_prettiness = max(max_prettiness, problems[0])
    
    # Case 2: Choose two problems
    for i in range(1, n):
        if problems[0] % problems[i] != 0:
            max_prettiness = max(max_prettiness, problems[0] + problems[i])
    
    # Case 3: Choose three problems
    for i in range(1, n):
        for j in range(i+1, n):
            if problems[0] % problems[i] != 0 and problems[0] % problems[j] != 0 and problems[i] % problems[j] != 0:
                max_prettiness = max(max_prettiness, problems[0] + problems[i] + problems[j])
    
    return max_prettiness

q = int(input())
for _ in range(q):
    n = int(input())
    problems = list(map(int, input().split()))
    result = max_prettiness(n, problems)
    print(result)
``` 
