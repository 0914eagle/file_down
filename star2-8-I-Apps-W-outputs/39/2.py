
n, s = map(int, input().split())

def solve(n, s, passengers):
  time = 0
  time += s
  for floor, arrival in passengers:
    time += floor
    time += max(0, time - arrival)
  return time

passengers = [list(map(int, input().split())) for _ in range(n)]
passengers.sort(key=lambda x: x[1])
print(solve(n, s, passengers))

