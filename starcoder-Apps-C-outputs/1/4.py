
#Reference: https://www.youtube.com/watch?v=kW1Z07fV3lM
L, R = map(int, input().split())

a = [0]*9

for i in range(L, R + 1):
    number = i
    while number > 9:
        number = sum(list(map(int, list(str(number)))))

    if number != 0:
        a[number - 1] += 1

print(*a)
