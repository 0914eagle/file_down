
def construct_binary_string(t, test_cases):
    for test_case in test_cases:
        n = test_case[0]
        s = test_case[1]

        w = ""
        for i in range(n):
            if s[i] == s[i + n - 1]:
                w += s[i]
            else:
                w += "0" if s[i] == "1" or s[i + n - 1] == "1" else "1"

        print(w)

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

# Solve the problem
construct_binary_string(t, test_cases)
