
n, k = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
s = ""
i = 0
for ch in range(97, 97 + k):
    s += chr(ch)
    i += 1
    while i < n and p[i] != q[i]:
        s += chr(ch)
        i += 1
if i < n:
    print("NO")
else:
    print("YES")
    print(s)

