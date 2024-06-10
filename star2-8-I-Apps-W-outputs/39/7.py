
n, s = list(map(int, input().split()))

floors = [0]*(s+1)
for _ in range(n):
    f, t = list(map(int, input().split()))
    floors[f] += t

time = 0
for i in range(s, 0, -1):
    time += floors[i]
    time += i
print(time)

