
def restore_secret_array(t, test_cases):
    for case in test_cases:
        n, x, y = case
        diff = y - x
        res = [x]
        for i in range(2, n):
            res.append(x + i * diff)
        res.append(y)
        print(*res)

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, x, y = map(int, input().split())
    test_cases.append((n, x, y))

# Function call
restore_secret_array(t, test_cases)
``` 
