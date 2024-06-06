
n, m = map(int, input().split())
f = list(map(int, input().split()))
b = list(map(int, input().split()))
f.append(0)

nums = [0] * (n + 1)
for i in range(1, n + 1):
    nums[i] = nums[f[i - 1]] + 1

cnt = 0
for i in range(m):
    cnt += (nums[b[i]] == i + 1)
if cnt == m:
    print('Possible')
    for i in range(m):
        print(f[b[i]], end=' ')
elif cnt > 1:
    print('Ambiguity')
else:
    print('Impossible')
