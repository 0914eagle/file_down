
def min_mistakes(n, s, superiors):
    mistakes = 0
    is_chief_reported = False
    superiors_count = [0] * n
    
    for i in range(n):
        if i + 1 != s:  # skip the chief
            superiors_count[superiors[i]] += 1
    
    for i in range(n):
        if i + 1 == s and superiors_count[i] == 0:
            is_chief_reported = True
        elif superiors_count[i] != superiors[i]:
            mistakes += 1
    
    if not is_chief_reported:
        mistakes += 1
    
    return mistakes

# Input
n, s = map(int, input().split())
superiors = list(map(int, input().split()))

# Output
print(min_mistakes(n, s, superiors))
```
