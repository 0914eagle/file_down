
def decrease_number(n, k):
    for _ in range(k):
        if n % 10 != 0:
            n -= 1
        else:
            n //= 10
    return n

# Take input
n, k = map(int, input().split())

# Call the function and print the result
print(decrease_number(n, k))
```
