
n = int(input())
a = list(map(int, input().split()))

index = {}
for i, x in enumerate(a):
  if x not in index:
    index[x] = i

res = [x for x in index]
print(len(res))
print(*res)

