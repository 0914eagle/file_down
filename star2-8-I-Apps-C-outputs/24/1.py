
def dist(x1, y1, x2, y2):
  return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def solve():
  x_roost, y_roost = map(float, input().split())
  n = int(input())
  chickens = []
  for _ in range(n):
    x_hide, y_hide = map(float, input().split())
    chickens.append((x_hide, y_hide))
  chickens.sort(key=lambda c: dist(x_roost, y_roost, c[0], c[1]))
  min_dist = dist(x_roost, y_roost, chickens[0][0], chickens[0][1])
  for i in range(1, len(chickens)):
    min_dist += dist(chickens[i-1][0], chickens[i-1][1], chickens[i][0], chickens[i][1])
  return min_dist

print(solve())

