
def min_moves_to_divisible(t, test_cases):
    results = []
    for i in range(t):
        a, b = test_cases[i]
        if a % b == 0:
            results.append(0)
        else:
            moves = b - (a % b)
            results.append(moves)
    return results

# Input
t = int(input())
test_cases = []
for _ in range(t):
    a, b = map(int, input().split())
    test_cases.append((a, b))

# Output
results = min_moves_to_divisible(t, test_cases)
for res in results:
    print(res)
```
