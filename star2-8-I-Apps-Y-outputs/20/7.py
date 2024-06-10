
n = int(input())
max_times = 0
answer = 0
for i in range(1, n+1):
    times = 0
    tmp = i
    while tmp % 2 == 0:
        times += 1
        tmp //= 2
    if times > max_times:
        max_times = times
        answer = i
print(answer)

