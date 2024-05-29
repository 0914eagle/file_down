
def is_prime(a):
    if a < 2:
        return 0
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return 0
    return 1

a = int(input())
print(is_prime(a))
```
