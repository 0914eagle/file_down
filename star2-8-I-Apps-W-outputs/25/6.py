
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
buildings = [0] * (m + 1)
noise = [0] * (m + 1)
total_noise = 0
for _ in range(n):
    i = int(input())
    buildings[i] += 1
for i in range(1, m + 1):
    noise[i] = buildings[i]
for i in range(1, m + 1):
    total_noise += noise[i]
if k >= m:
    print(total_noise)
    exit()
for _ in range(k):
    max_idx = noise.index(max(noise))
    total_noise -= noise[max_idx]
    noise[max_idx] = 0
print(total_noise)

