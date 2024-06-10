
def solve(t, s):
    n, m = len(t), len(s)
    pos = [[] for _ in range(26)]
    for i, (l, c) in enumerate(t):
        pos[ord(c) - ord('a')].append(i)
    res = 0
    j = 0
    for i, (l, c) in enumerate(s):
        c = ord(c) - ord('a')
        if not pos[c]:
            return 0
        while j < len(pos[c]) and pos[c][j] < i:
            j += 1
        if j == len(pos[c]):
            return 0
        res += pos[c][j] - i + 1
    return res

n, m = map(int, input().split())
t = [tuple(map(int, input().split('-'))) for _ in range(n)]
s = [tuple(map(int, input().split('-'))) for _ in range(m)]
print(solve(t, s))

