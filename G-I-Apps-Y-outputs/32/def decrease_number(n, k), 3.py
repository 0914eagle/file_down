
def decrease_number(n, k):
    while k > 0:
        if n % 10 == 0:
            n /= 10
        else:
            n -= 1
        k -= 1
    return int(n)

# Read input
n, k = map(int, input().split())

result = decrease_number(n, k)
print(result)
```
