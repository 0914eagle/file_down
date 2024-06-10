
n, c, k = map(int, input().split())
colors = list(map(int, input().split()))
colors.sort()

current = 0
machines = 0

while current < n:
    machines += 1
    current += c
print(machines)

