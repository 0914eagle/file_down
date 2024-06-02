
def solve(s, v1, v2):
    if s % (v1 - v2) == 0:
        return s // v1, s // (v1 - v2)
    else:
        return "Impossible"

s, v1, v2 = map(int, input().split())
print(solve(s, v1, v2))


def solve(l):
    return sum(l)

l = list(map(int, input().split()))
print(solve(l))


def solve(l):
    return sum(l)

l = list(map(int, input().split()))
print(solve(l))

