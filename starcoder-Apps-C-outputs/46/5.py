
N, L, R = map(int, input().split())
n = bin(N)[2:]
ans = 0
for i in range(L-1, R):
    if n[i] == '1':
        ans += 1
print(ans)
