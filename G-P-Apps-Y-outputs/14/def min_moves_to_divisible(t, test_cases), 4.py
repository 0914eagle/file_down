
def min_moves_to_divisible(t, test_cases):
    result = []
    for i in range(t):
        a, b = test_cases[i]
        if a % b == 0:
            result.append(0)
        else:
            result.append(b - (a % b))
    
    return result

# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    a, b = map(int, input().split())
    test_cases.append((a, b))

# Call the function and print results
result = min_moves_to_divisible(t, test_cases)
for res in result:
    print(res)
```
