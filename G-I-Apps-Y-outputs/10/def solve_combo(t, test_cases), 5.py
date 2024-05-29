
def solve_combo(t, test_cases):
    for test_case in test_cases:
        n, m = test_case[0]
        s = test_case[1]
        p = test_case[2]
        
        total_presses = [0] * 26
        last_correct = 0
        mistakes = [0] * (n + 1)
        
        for i in range(m):
            mistakes[p[i]] += 1
        
        for i in range(1, n + 1):
            mistakes[i] += mistakes[i - 1]
        
        for i in range(1, n + 1):
            length = i - last_correct - mistakes[i - 1]
            total_presses[ord(s[i - 1]) - ord('a')] += length
            last_correct = i
        
        remaining_length = n - last_correct
        total_presses[ord(s[-1]) - ord('a')] += remaining_length
        
        print(' '.join(map(str, total_presses)))

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    p = list(map(int, input().split()))
    test_cases.append((n, m, s, p))

# Solving and printing output
solve_combo(t, test_cases)
```
