
n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
a.sort()
ans = []
for i in q:
    s = sum(a[:i])
    s += sum(a[i:n])
    ans.append(s)
for i in ans:
    print(i)

