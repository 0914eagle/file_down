
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def count_round_dance_ways(n):
    return factorial(n // 2 - 1) // 2

n = int(input())
print(count_round_dance_ways(n))
```
