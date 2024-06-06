
n = int(input())
first = second = 0
for _ in range(n):
    point = int(input())
    if point > 0:
        first += point
    else:
        second += abs(point)
if first > second:
    print('first')
elif second > first:
    print('second')
else:
    print('second')
