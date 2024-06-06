
n, t, c = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if A[i] <= t:
        cnt += 1
    else:
        cnt = 0
    if cnt == c:
        break

for i in range(n-1, -1, -1):
    if A[i] <= t:
        cnt += 1
    else:
        cnt = 0
    if cnt == c:
        break
print(n-i)
