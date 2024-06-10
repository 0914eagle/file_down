
from collections import deque

def fire(fired):
  fired.append(len(HR)+1)
  HR.append(fired.popleft())
  return fired

def hire(new):
  new.append(len(HR)+1)
  HR.append(new.popleft())
  return new

n = int(input())
HR = deque()
for i in range(n):
  f, h = map(int, input().split())
  while len(HR) < f+h:
    HR.append(len(HR)+1)
  for j in range(f):
    HR.popleft()
  for j in range(h):
    HR.append(HR.popleft())
  print(HR[0], end=" ")

