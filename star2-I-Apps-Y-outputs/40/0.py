
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

def find_next_multiple(n, m):
    return n + (m - n % m)

time = 0
time = find_next_multiple(time, 10)
time += A
time = find_next_multiple(time, 10)
time += B
time = find_next_multiple(time, 10)
time += C
time = find_next_multiple(time, 10)
time += D
time = find_next_multiple(time, 10)
time += E

print(time)

