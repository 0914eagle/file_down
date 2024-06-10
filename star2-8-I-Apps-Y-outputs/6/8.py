
n = int(input())
a = list(map(int, input().split()))

hash_map = {}
for i in range(n):
  if a[i] not in hash_map:
    hash_map[a[i]] = i

res = [0] * len(hash_map)
for k, v in hash_map.items():
  res[v] = k

print(len(hash_map))
print(" ".join(map(str, res)))

