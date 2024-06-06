
n, l = map(int, input().split())

k = list(map(int, input().split()))
s = list(map(int, input().split()))

for i in range(n):
    if k[i] != s[i]:
        print("NO")
        break
else:
    print("YES")
