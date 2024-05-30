
def masha_decision(x, y, z, t1, t2, t3):
    stairs_time = abs(x - y) * t1
    elevator_time = abs(x - z) * t2 + t3 + abs(z - y) * t2 + t3

    if stairs_time < elevator_time:
        print("YES")
    else:
        print("NO")

# Input
x, y, z, t1, t2, t3 = map(int, input().split())
masha_decision(x, y, z, t1, t2, t3)
```
