
from functools import cmp_to_key
from itertools import accumulate

def cmp(a, b):
    return len(b[1]) - len(a[1])

def main():
    n, s, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(s):
        l, r = map(int, input().split())
        b.append((l, r))
    b.sort(key=cmp_to_key(cmp))
    c = [[] for _ in range(n+1)]
    for l, r in b:
        for i in range(l, r+1):
            c[i].append(a[i-1])
    d = [list(accumulate(sorted(i))) for i in c]
    mn = a[0]
    for i in range(1, n+1):
        if d[i] and d[i][-1] >= k:
            mn = min(mn, d[i][k-1])
    if mn == a[0]:
        print(-1)
    else:
        print(mn)

if __name__ == "__main__":
    main()
