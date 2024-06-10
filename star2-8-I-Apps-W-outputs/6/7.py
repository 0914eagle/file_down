
n, m = map(int, input().split())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

def solve(s1, s2):
    if s1[0] > 0 and s2[0] > 0:
        if s1[0] > s2[0]:
            return 0
        elif s1[0] < s2[0]:
            return 1
        else:
            return solve(s1[1:], s2[1:])
    elif s1[0] == 0 and s2[0] == 0:
        return 1
    elif s1[0] == 0:
        return solve(s1[1:], s2)
    else:
        return solve(s1, s2[1:])

res = solve(s1, s2)
print(res)

