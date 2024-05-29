
from collections import defaultdict

def calculate_button_presses(t, test_cases):
    for i in range(t):
        n, m = test_cases[i][0]
        s = test_cases[i][1]
        p = test_cases[i][2]
        
        button_presses = defaultdict(int)
        total_presses = [0] * n
        
        total_presses[0] = 1
        for position in p:
            total_presses[position] -= 1
        
        for j in range(1, n):
            total_presses[j] += total_presses[j-1]
            
        for j in range(n):
            button_presses[s[j]] += total_presses[j]
            
        result = [button_presses[char] for char in 'abcdefghijklmnopqrstuvwxyz']
        print(*result)

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    p = list(map(int, input().split()))
    test_cases.append((n, m, s, p))

# Output
calculate_button_presses(t, test_cases)
```
