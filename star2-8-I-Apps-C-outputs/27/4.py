
n = int(input())
integers = list(map(int, input().split()))
sums = [0]
for i in integers:
  sums.append(sums[-1] + i)

count = 0
for i in range(n):
  for j in range(i + 1, n + 1):
    if sums[j] - sums[i] == integers[i] * (j - i):
      count += 1

print(count)

