
def choose_transport(x, y, z, t1, t2, t3):
    stairs_time = abs(x - y) * t1
    elevator_time = 0

    if x < z and y < z:
        elevator_time = abs(x - z) * t2 + abs(y - z) * t2 + 3 * t3
    elif x > z and y > z:
        elevator_time = abs(x - z) * t2 + abs(y - z) * t2 + 3 * t3
    else:
        elevator_time = (abs(x - z) + abs(y - z)) * t2 + 5 * t3

    if elevator_time <= stairs_time:
        return "YES"
    else:
        return "NO"

# Input
x, y, z, t1, t2, t3 = map(int, input().split())
print(choose_transport(x, y, z, t1, t2, t3))
```
