
import sys
import math

def dist(x1, y1, x2, y2):
  return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def solve(roost_x, roost_y, hspots):
  res = 0
  for x, y in hspots:
    res += dist(roost_x, roost_y, x, y)
  return res

def main():
  roost_x, roost_y = map(float, input().split())
  n = int(input())
  hspots = []
  for _ in range(n):
    x, y = map(float, input().split())
    hspots.append((x, y))
  print(solve(roost_x, roost_y, hspots))

if __name__ == '__main__':
  main()

