
def choose_transport(x, y, z, t1, t2, t3):
    stairs_time = abs(x - y) * t1
    elevator_time = abs(x - z) * t2 + abs(z - y) * t2 + 3 * t3
    
    if elevator_time <= stairs_time:
        return "YES"
    else:
        return "NO"

# Input
x, y, z, t1, t2, t3 = map(int, input().split())

# Output
print(choose_transport(x, y, z, t1, t2, t3))
```
