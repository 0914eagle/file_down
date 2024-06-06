
N = int(input())
L = [input() for _ in range(2*N)]

ans = 0
for i in range(N):
    for j in range(N):
        if L[i] == L[N+j]:
            ans += abs(i-j)

print(ans//2)
