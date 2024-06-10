
from math import log10
n, p, k = map(int, input().split())
t = list(map(int, input().split()))

def time_to_speed(t):
return pow(1 + p / 100, t)

def speed_to_time(s):
return log10(s) / log10(1 + p / 100)

def calc_time(t):
return sum(map(speed_to_time, map(time_to_speed, t)))

left, right = 0, k
while right - left > 1e-6:
mid = (left + right) / 2
if calc_time([mid]) > k:
right = mid
else:
left = mid
print(left)

