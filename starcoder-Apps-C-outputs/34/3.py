
import sys

def main():
    n = int(sys.stdin.readline().strip())
    h = [0 for i in range(n)]
    t = [0 for i in range(n)]
    for i in range(n):
        h[i], t[i] = list(map(int, sys.stdin.readline().strip().split()))
    t.sort()
    ans = 200000
    for i in range(n):
        for j in range(i + 1, n):
            m = max(h)
            s = sum(t[0:i])
            if s >= m:
                m = s
            s = sum(t[i:j])
            if s >= m:
                m = s
            s = sum(t[j:])
            if s >= m:
                m = s
            ans = min(ans, m * max(h))
            h[h.index(max(h))] = 0
    print(ans)

main()
