
n = int(input())
cafes = [int(i) for i in input().split()]
last = [0] * (2 * 10 ** 5 + 1)
for i in range(n):
    last[cafes[i]] = i
ans = -1
mx = n + 1
for i in range(1, len(last)):
    if last[i] != 0 and last[i] < mx:
        mx = last[i]
        ans = i
print(ans)

