
def choose_elevator_or_stairs(x, y, z, t1, t2, t3):
    stairs_time = abs(x - y) * t1
    elevator_time = abs(x - z) * t2 + abs(z - y) * t2 + 3 * t3
    return "YES" if elevator_time <= stairs_time else "NO"

x, y, z, t1, t2, t3 = map(int, input().split())
print(choose_elevator_or_stairs(x, y, z, t1, t2, t3))
```