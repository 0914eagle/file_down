
def min_mistakes(n, s, superiors):
    mistakes = 0
    reported_superiors = [0] * n
    
    for i in range(n):
        if i != s - 1:
            reported_superiors[i] = superiors[i]
    
    reported_superiors[s - 1] = 0
    
    reported_superiors[s - 1] = 0
    for i in range(n):
        if i != s - 1:
            if reported_superiors[i] == 0:
                if i + 1 != s:
                    mistakes += 1
            else:
                if i + 1 == s:
                    mistakes += 1
    
    return mistakes

# Input parsing
n, s = map(int, input().split())
superiors = list(map(int, input().split()))

# Call the function and print the result
print(min_mistakes(n, s, superiors))
```
