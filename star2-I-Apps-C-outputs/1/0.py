
import math

def solve(n, schedule):
    pass

n = int(input())
schedule = []
for _ in range(n-1):
    t, g, r = map(int, input().split())
    schedule.append((t, g, r))

print(solve(n, schedule))

