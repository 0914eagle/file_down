
def find_common_subsequence(t, test_cases):
    for i in range(t):
        n, m = test_cases[i][0]
        a = test_cases[i][1]
        b = test_cases[i][2]

        common_elements = set(a) & set(b)

        if len(common_elements) > 0:
            k = 1
            common_element = common_elements.pop()
            print("YES")
            print(f"1 {common_element}")
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

# Call the function with the input
find_common_subsequence(t, test_cases)
