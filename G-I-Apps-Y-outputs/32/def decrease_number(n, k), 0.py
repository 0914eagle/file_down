
def decrease_number(n, k):
    for _ in range(k):
        if n % 10 != 0:
            n -= 1
        else:
            n //= 10
    return n

# Reading input from user
n, k = map(int, input().split())

# Calculating the result and printing it
result = decrease_number(n, k)
print(result)
```
