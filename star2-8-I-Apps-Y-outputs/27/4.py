
N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]

h.sort()

diff_min = 10**9
for i in range(N - K + 1):
    diff = h[i + K - 1] - h[i]
    if diff < diff_min:
        diff_min = diff

print(diff_min)

