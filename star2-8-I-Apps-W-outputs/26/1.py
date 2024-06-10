
n = int(input())
arr = list(map(int, input().split()))
freq = {}
for i in range(n):
  if arr[i] not in freq:
    freq[arr[i]] = [0, 0]
  freq[arr[i]][0] += 1
for i in range(n-1, -1, -1):
  freq[arr[i]][1] += 1
ans = 0
for k, v in freq.items():
  ans += v[0] * (v[0] - 1) // 2
  ans += v[1] * (v[1] - 1) // 2
  ans -= v[0] * v[1]
print(ans)

