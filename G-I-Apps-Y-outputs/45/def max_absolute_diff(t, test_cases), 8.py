
def max_absolute_diff(t, test_cases):
    res = []
    for i in range(t):
        n, m = test_cases[i]
        if n == 1:
            res.append(0)
        elif n == 2:
            res.append(2)
        else:
            if n % 2 == 0:
                res.append(2*m)
            else:
                res.append(2*m - 2)
    return res

# Input
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    test_cases.append((n, m))

# Call the function
result = max_absolute_diff(t, test_cases)

# Output
for r in result:
    print(r)
