
def decrease_number(n, k):
    while k > 0:
        if n % 10 != 0:
            n -= 1
        else:
            n //= 10
        k -= 1
    return n

n, k = map(int, input().split())
result = decrease_number(n, k)
print(result)
```
