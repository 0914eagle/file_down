
def min_mistakes(n, s, superiors):
    mistakes = 0
    reported_superiors = [0] * (n + 1)
    reported_superiors[s] = 1
    
    for i in range(1, n + 1):
        if i == s:
            continue
        if superiors[i-1] == 0:
            mistakes += 1
        else:
            reported_superiors[i] = 1
            reported_superiors[superiors[i-1]] += 1
    
    for i in range(1, n + 1):
        if i != s and reported_superiors[i] == 0:
            mistakes += 1
    
    return mistakes

# Input
n, s = map(int, input().split())
superiors = list(map(int, input().split()))

# Output
print(min_mistakes(n, s, superiors))
```
