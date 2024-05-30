
x, y, z, t1, t2, t3 = map(int, input().split())

stairs_time = abs(x - y) * t1

elevator_time = abs(x - z) * t2 + abs(z - y) * t2 + t3 * 3

if elevator_time <= stairs_time:
    print("YES")
else:
    print("NO")
