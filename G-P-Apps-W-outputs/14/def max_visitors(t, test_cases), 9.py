
def max_visitors(t, test_cases):
    result = []
    for i in range(t):
        a, b, c = test_cases[i]
        total = a + b + c
        result.append(min(total, (a+b+c+1)//2))
    return result

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    a, b, c = map(int, input().split())
    test_cases.append((a, b, c))

# Call the function and print the output
output = max_visitors(t, test_cases)
for val in output:
    print(val)
```
