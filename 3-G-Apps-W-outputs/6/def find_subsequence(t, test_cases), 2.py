
def find_subsequence(t, test_cases):
    for _ in range(t):
        n, m, a, b = test_cases[_]
        common_elements = set(a) & set(b)
        if common_elements:
            print("YES")
            print("1", common_elements.pop())
        else:
            print("NO")

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, m, a, b))

# Call the function
find_subsequence(t, test_cases)
