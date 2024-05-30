
def min_mistakes(n, s, superiors):
    mistakes = 0
    for i in range(1, n+1):
        if i != s:
            if superiors[i-1] == 0:
                mistakes += 1
    return mistakes

# Input
n, s = map(int, input().split())
superiors = list(map(int, input().split()))

# Output
print(min_mistakes(n, s, superiors))
```
