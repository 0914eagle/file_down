
import sys
input = sys.stdin.readline
N = int(input())
nums = [int(x) for x in input().split()]
count = 0
for i in range(N-2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
      if nums[i] + nums[j] == nums[k]:
        count += 1
print(count)

