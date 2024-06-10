
def solve():
    w, h, k = map(int, input().split())
    return sum(4*(w + h - 4*i - 4) for i in range(k))

print(solve())

