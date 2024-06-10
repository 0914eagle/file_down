
def solve(a, s):
    n = len(s)
    pref = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            pref[i][j] = int(s[i]) * int(s[j]) if i <= j else 0
    res = 0
    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for l in range(j, n):
                    cur = pref[i][j] + pref[i][l] + pref[k][j] + pref[k][l]
                    if cur == a:
                        res += 1
    return res

a = int(input())
s = input()
print(solve(a, s))

