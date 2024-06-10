
a, b, c = [int(x) for x in input().split()]
m = int(input())
cost = []
for i in range(m):
  val, port = input().split()
  cost.append([int(val), port])
cost.sort(key=lambda x: x[0])

count = 0
total_cost = 0
i = 0
while count < a+b+c and i < len(cost):
  if cost[i][1] == "USB" and a > 0:
    a -= 1
  elif cost[i][1] == "PS/2" and b > 0:
    b -= 1
  elif cost[i][1] == "PS/2" and cost[i][1] == "USB" and c > 0:
    c -= 1
  else:
    i += 1
    continue
  count += 1
  total_cost += cost[i][0]
  i += 1
print(count, total_cost)

