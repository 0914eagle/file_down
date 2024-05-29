
def is_simple_power(x, n):
    if x < 1 or n <= 1:
        return False
    if x == 1:
        return True
    power = 1
    while n ** power <= x:
        if n ** power == x:
            return True
        power += 1
    return False
```
