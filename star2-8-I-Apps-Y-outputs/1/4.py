
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
s = set(a)
if k < len(s):
    print("NO")
else:
    print("YES")
    for i in a:
        print(a.index(i) % k + 1, end=" ")

