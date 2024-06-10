
from collections import deque

def main():
    n = int(input())
    def f(s):
        b = s.count("b")
        w = s.count("w")
        if b >= w:
            return b
        else:
            return w + 1
    q = deque([("www", 0), ("wbb", 0), ("bbb", 0)])
    p = [0] * n
    while q:
        s, i = q.popleft()
        p[i] += f(s)
        if i < n - 1:
            q.append((s[:i] + "b" + s[i + 1:], i + 1))
            q.append((s[:i] + "w" + s[i + 1:], i + 1))
    print(*[p[i] // 2 % 998244353 for i in range(n)])

main()

