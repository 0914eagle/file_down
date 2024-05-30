
def max_visitors(t, test_cases):
    max_visitors_list = []
    
    for i in range(t):
        a, b, c = test_cases[i]
        total = a + b + c
        max_visitors_list.append(min(total, (a + b + c) // 2))
    
    return max_visitors_list

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    a, b, c = map(int, input().split())
    test_cases.append((a, b, c))

# Call the function and print the output
max_visitors_list = max_visitors(t, test_cases)
for visitors in max_visitors_list:
    print(visitors)
```
