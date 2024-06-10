
from sys import stdin
def main():
    input = stdin.readline
    n = int(input())
    f, h = [], []
    for _ in range(n):
        fi, hi = map(int, input().split())
        f.append(fi)
        h.append(hi)
    q = []
    ans = []
    for i in range(n):
        for _ in range(f[i]):
            q.pop(0)
        for _ in range(h[i]):
            q.append(i+1)
        ans.append(q[0])
    print(len(set(ans)))
    print(*ans)
main()

