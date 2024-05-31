
def exact_change(q, test_cases):
    result = []
    for i in range(q):
        a, b, n, S = test_cases[i]
        if S % n <= b and (S // n <= a or S // n * n + b >= S):
            result.append("YES")
        else:
            result.append("NO")
    return result

# Input parsing
q = int(input())
test_cases = []
for _ in range(q):
    a, b, n, S = map(int, input().split())
    test_cases.append((a, b, n, S))

# Function call
output = exact_change(q, test_cases)

# Output
for ans in output:
    print(ans)
