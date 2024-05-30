
def min_mistakes(n, s, superiors):
    count_mistakes = 0
    
    # Count the number of immediate superiors each worker has reported
    reported_superiors = [0] * n
    for i in range(n):
        if i+1 != s:
            reported_superiors[superiors[i]] += 1
    
    # Check the workers who could have made a mistake
    for i in range(n):
        if i+1 != s:
            if reported_superiors[i] != superiors[i]:
                count_mistakes += 1
    
    return count_mistakes

# Input parsing
n, s = map(int, input().split())
superiors = list(map(int, input().split()))

# Call the function and print the result
print(min_mistakes(n, s, superiors))
```
