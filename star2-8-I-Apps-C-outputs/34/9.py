
def solve(s):
    s = list(set(s))
    s.sort()
    d_max = -1
    for i in range(len(s) - 3):
        for j in range(i + 1, len(s) - 2):
            for k in range(j + 1, len(s) - 1):
                d = s[i] + s[j] + s[k]
                if d in s:
                    d_max = max(d_max, d)
    if d_max == -1:
        print("No solution")
    else:
        print(d_max)

n = int(input())
s = []
for _ in range(n):
    s.append(int(input()))

solve(s)

