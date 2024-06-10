
def solve(k):
    if k == 1:
        return 0, 1
    a, b = solve(k - 1)
    return b, a + b

k = int(input())
a, b = solve(k)
print(a, b)

