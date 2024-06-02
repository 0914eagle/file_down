
N = int(input())
h = list(map(int, input().split()))

ans = 0
for i in range(N):
    if h[i] != 0:
        ans += 1
        for j in range(i, N):
            if h[j] != 0:
                h[j] -= 1

print(ans)

