
def calculate_button_presses(t, test_cases):
    for test_case in test_cases:
        n, m = test_case[0], test_case[1]
        s = test_case[2]
        p = test_case[3]

        button_presses = [0] * 26
        total_presses = [0] * n
        for i in range(m):
            total_presses[p[i] - 1] += 1

        cumulative = 0
        for i in range(n):
            button_presses[ord(s[i]) - ord('a')] += 1 + total_presses[i] + cumulative
            cumulative += total_presses[i]

        print(" ".join(map(str, button_presses)))

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    p = list(map(int, input().split()))
    test_cases.append((n, m, s, p))

# Calculate and print button presses for test cases
calculate_button_presses(t, test_cases)
```
