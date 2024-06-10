
N, K = map(int, input().split())
heights = [int(input()) for _ in range(N)]
heights.sort()
diff_min = 10**9+7
for i in range(N-K+1):
  diff = heights[i+K-1] - heights[i]
  diff_min = min(diff_min, diff)
print(diff_min)

