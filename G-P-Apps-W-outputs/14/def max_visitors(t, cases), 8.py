
def max_visitors(t, cases):
    for case in cases:
        a, b, c = case
        max_visitors = min(a, b, c) + (a + b + c - min(a, b, c)) // 2
        print(max_visitors)

# Input parsing
t = int(input())
cases = []
for _ in range(t):
    case = list(map(int, input().split()))
    cases.append(case)

# Call the function with the inputs
max_visitors(t, cases)
