
def solve(f,s,g,u,d):
  current_floor = s
  if current_floor > g:
    direction = -1
  else:
    direction = 1
  count = 0
  while current_floor != g:
    if direction == 1:
      current_floor += u
      count += 1
      if current_floor > f:
        return "use the stairs"
    else:
      current_floor -= d
      count += 1
      if current_floor < 1:
        return "use the stairs"
  return count

f,s,g,u,d = [int(x) for x in input().split()]
print(solve(f,s,g,u,d))

