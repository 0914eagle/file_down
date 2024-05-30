
def min_mistakes(n, s, superiors):
    mistakes = 0
    
    chief_superiors = superiors[s-1]
    
    if chief_superiors != 0:
        mistakes += 1
    
    for i in range(n):
        if i+1 != s and superiors[i] == 0:
            mistakes += 1
    
    return mistakes

# Input
n, s = map(int, input().split())
superiors = list(map(int, input().split()))

# Output
print(min_mistakes(n, s, superiors))
```
