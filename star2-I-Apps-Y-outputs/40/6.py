
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

def ceil(a, b):
  return (a + b - 1) // b

time = 0
time = ceil(time, 10)
time += A
time = ceil(time, 10)
time += B
time = ceil(time, 10)
time += C
time = ceil(time, 10)
time += D
time = ceil(time, 10)
time += E
print(time)

