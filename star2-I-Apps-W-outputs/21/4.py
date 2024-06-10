
x = int(input())
x = x % 360
if x < 0:
    x += 360
if x == 0:
    print(0)
elif x == 90:
    print(1)
elif x == 180:
    print(2)
elif x == 270:
    print(3)
else:
    print(x // 90)

