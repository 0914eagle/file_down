
def shortest_test_scheme(k, allergens):
    max_duration = max(allergens)
    test_scheme = [0] * (max_duration + 1)

    for duration in allergens:
        for i in range(duration):
            test_scheme[i+1] += 1

    return max(test_scheme)

# Input parsing
k = int(input())
allergens = []
for _ in range(k):
    allergens.append(int(input()))

# Output
print(shortest_test_scheme(k, allergens))
```
