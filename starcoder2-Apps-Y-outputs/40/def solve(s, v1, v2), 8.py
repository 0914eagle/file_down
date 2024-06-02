
def solve(s, v1, v2):
    if s % (v1 - v2) != 0:
        return 'Impossible'
    else:
        n1 = s // v1
        n2 = 0
        while n1 % v2 != 0:
            n1 -= 1
            n2 += 1
        return n1, n2

s, v1, v2 = map(int, input().split())
print(*solve(s, v1, v2))

