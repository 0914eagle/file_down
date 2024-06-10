
def solve(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a, b

k = int(input())
a, b = solve(k)
print(a, b)

