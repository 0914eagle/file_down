
def min_mistakes(n, s, superiors):
    mistakes = 0
    for i in range(1, n + 1):
        if i != s:  # Skip the chief
            if superiors[i-1] != 0 and superiors[i-1] != superiors[s-1]:  # Check if the reported superiors match the chief's
                mistakes += 1
    return mistakes

# Input
n, s = map(int, input().split())
superiors = list(map(int, input().split()))

# Output
print(min_mistakes(n, s, superiors))
```
