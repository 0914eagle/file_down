
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

def ceil(x, y):
  return (x + y - 1) // y

def calc_time(order):
  time = 0
  for dish in order:
    if dish == "A":
      time = ceil(time, A) * A
    elif dish == "B":
      time = ceil(time, B) * B
    elif dish == "C":
      time = ceil(time, C) * C
    elif dish == "D":
      time = ceil(time, D) * D
    elif dish == "E":
      time = ceil(time, E) * E
  return time

order = "ABCDE"
min_time = calc_time(order)
for i in range(1, 5):
  for j in range(i + 1, 6):
    for k in range(j + 1, 7):
      for l in range(k + 1, 8):
        for m in range(l + 1, 9):
          order = "ABCDE"
          order = order[:i] + order[i:j] + order[j:k] + order[k:l] + order[l:m] + order[m:]
          time = calc_time(order)
          if time < min_time:
            min_time = time

print(min_time)

