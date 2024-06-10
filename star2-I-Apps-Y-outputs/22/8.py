
def solve(k):
    a = 0
    b = 1
    for _ in range(k):
        a, b = b, 2 * b + a
    return a, b

k = int(input())
a, b = solve(k)
print(a, b)

