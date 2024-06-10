
def maximumBling(d, b, f, t0, t1, t2):
  if d == 0:
    return b
  if f != 0:
    b += 100 * f
    f = 0
  b -= 400
  f += 1
  b += 100 * f
  f = 0
  if t0 != 0:
    f += 3 * t0
    t0 = 0
  if t1 != 0:
    f += 3 * t1
    t1 = 0
  if t2 != 0:
    f += 3 * t2
    t2 = 0
  return maximumBling(d - 1, b, f, t0, t1, t2)

d = int(input())
b = int(input())
f = int(input())
t0 = int(input())
t1 = int(input())
t2 = int(input())
print(maximumBling(d, b, f, t0, t1, t2))

