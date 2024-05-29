
def calculate_button_presses(t, test_cases):
    for _ in range(t):
        n, m = test_cases[_][0]
        s = test_cases[_][1]
        p = test_cases[_][2]

        button_presses = [0] * 26
        total_presses = 0

        wrong_presses = [0] * (n + 1)

        for pi in p:
            wrong_presses[pi] = 1

        for i in range(n, 0, -1):
            if wrong_presses[i] == 1:
                total_presses += 1
            wrong_presses[i] = total_presses

        for i in range(n):
            button_presses[ord(s[i]) - ord('a')] += 1 + total_presses - wrong_presses[i]

        result = ' '.join(map(str, button_presses))
        print(result)

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    s = input().strip()
    p = list(map(int, input().split()))
    test_cases.append((n, m, s, p))

# Solve the problem for the given test cases
calculate_button_presses(t, test_cases)
