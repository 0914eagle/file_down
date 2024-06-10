
def solve(k):
    a = 0
    b = 1
    for i in range(k):
        a, b = b, a + b
    return a, b

k = int(input())
a, b = solve(k)
print(a, b)

