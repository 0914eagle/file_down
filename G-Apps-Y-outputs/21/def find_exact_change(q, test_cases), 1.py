
def find_exact_change(q, test_cases):
    answers = []
    for i in range(q):
        a, b, n, S = test_cases[i]
        max_x = min(a, S // n)
        if max_x * n + b >= S:
            answers.append("YES")
        else:
            answers.append("NO")
    return answers

# Input parsing
q = int(input())
test_cases = []
for _ in range(q):
    a, b, n, S = map(int, input().split())
    test_cases.append((a, b, n, S))

# Find answers
answers = find_exact_change(q, test_cases)

# Output
for ans in answers:
    print(ans)
