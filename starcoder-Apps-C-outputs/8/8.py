
import sys

def solution(n, m, p, r, ct, tt):
  num, time, t, cloth = 0, 0, 0, 0
  for i in range(n):
    if tt[i] >= time:
      if ct[i] != cloth:
        t += p[ct[i]-1]
        time += t
        cloth = ct[i]
      num += 1
      time += tt[i]
    else:
      if ct[i] == cloth:
        num += 1
        time += tt[i]
      else:
        if time > tt[i]:
          cloth = ct[i]
          t += r[ct[i]-1]
          time += t + tt[i]
          num += 1
        else:
          num = i
          time = tt[i]
          cloth = ct[i]
          t += p[ct[i]-1]
    if i == n-1:
      time += r[ct[i]-1]
  return num


n, m = list(map(int, sys.stdin.readline().split()))
p = list(map(int, sys.stdin.readline().split()))
r = list(map(int, sys.stdin.readline().split()))
ct = []
tt = []
for i in range(n):
  c, t = list(map(int, sys.stdin.readline().split()))
  ct.append(c)
  tt.append(t)
print(solution(n, m, p, r, ct, tt))
