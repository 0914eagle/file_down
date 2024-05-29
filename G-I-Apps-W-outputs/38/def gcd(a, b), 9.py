
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_operations(a, b):
    if a == b:
        return 0
    
    common_divisor = gcd(a, b)
    a_operations = 0
    while a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        if a % 2 == 0:
            a //= 2
        elif a % 3 == 0:
            a = a // 3 * 2
        elif a % 5 == 0:
            a = a // 5 * 4
        a_operations += 1
    
    b_operations = 0
    while b % 2 == 0 or b % 3 == 0 or b % 5 == 0:
        if b % 2 == 0:
            b //= 2
        elif b % 3 == 0:
            b = b // 3 * 2
        elif b % 5 == 0:
            b = b // 5 * 4
        b_operations += 1
    
    if a != b:
        return -1
    
    return a_operations + b_operations

a, b = map(int, input().split())
print(get_operations(a, b))
```
