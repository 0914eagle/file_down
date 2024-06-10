
n, k = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
if set(p) != set(q):
    print("NO")
else:
    print("YES")
    a = [chr(ord('a') + i) for i in range(k)]
    s = ""
    for i in range(n):
        s += a[p[i] % k]
    print(s)

