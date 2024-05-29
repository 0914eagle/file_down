
def calculate_button_presses(t, test_cases):
    for case in test_cases:
        n, m = case[0], case[1]
        s = case[2]
        p = case[3]

        button_presses = [0]*26
        for i in range(n):
            button_presses[ord(s[i]) - ord('a')] += 1

        total_presses = [0] * 26
        for i in range(m):
            for j in range(p[i]):
                total_presses[ord(s[j]) - ord('a')] += 1

        remaining_letters = [0] * 26
        for i in range(n):
            remaining_letters[ord(s[i]) - ord('a')] += 1
            for j in range(i, n, n):
                remaining_letters[ord(s[j]) - ord('a')] += 1
        
        for i in range(26):
            button_presses[i] += total_presses[i] + remaining_letters[i]

        print(' '.join(map(str, button_presses)))

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
