
def solve(a, b, c):
    if a == b:
        return c
    elif a == c:
        return b
    else:
        return a

a, b, c = map(int, input().split())
print(solve(a, b, c))

