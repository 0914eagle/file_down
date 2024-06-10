
def solve(a, s):
    n = len(s)
    b = [[int(s[i]) * int(s[j]) for j in range(n)] for i in range(n)]
    res = 0
    for x in range(n):
        for y in range(x, n):
            for z in range(n):
                for t in range(z, n):
                    s = 0
                    for i in range(x, y + 1):
                        for j in range(z, t + 1):
                            s += b[i][j]
                    if s == a:
                        res += 1
    return res

a = int(input())
s = input()
print(solve(a, s))

