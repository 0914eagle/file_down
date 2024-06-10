
def drink(t):
  n = int(input())
  people = []
  for _ in range(n):
    people.append(list(map(int, input().split())))
  best = 0
  for a in range(10001):
    for b in range(10001 - a):
      c = 10000 - a - b
      count = 0
      for person in people:
        if person[0] <= a and person[1] <= b and person[2] <= c:
          count += 1
      best = max(best, count)
  print(f"Case #{t}: {best}")

t = int(input())
for i in range(t):
  drink(i + 1)

