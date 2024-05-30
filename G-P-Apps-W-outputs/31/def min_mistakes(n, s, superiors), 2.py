
def min_mistakes(n, s, superiors):
    mistakes = 0
    reported_superiors = [0] * n
    reported_superiors[s-1] = 1  # Chief is always a superior to all workers except himself
    
    for i in range(n):
        if i + 1 == s:
            continue
        
        if superiors[i] == 0:
            mistakes += 1
        else:
            reported_superiors[i] = 1
            if reported_superiors[superiors[i] - 1] != 1:
                mistakes += 1
    
    return mistakes

# Input parsing
n, s = map(int, input().split())
superiors = list(map(int, input().split()))

result = min_mistakes(n, s, superiors)
print(result)
```
