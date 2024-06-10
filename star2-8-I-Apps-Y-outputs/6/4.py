
n = int(input())
arr = list(map(int, input().split()))
s = set()
ans = []
for x in reversed(arr):
  if x not in s:
    ans.append(x)
    s.add(x)
print(len(ans))
print(*reversed(ans))

