
def count_round_dance_ways(n):
    def factorial(num):
        if num <= 1:
            return 1
        else:
            return num * factorial(num - 1)

    return factorial(n // 2 - 1) // (factorial(1) * factorial((n // 2) - 2))

n = int(input())
print(count_round_dance_ways(n))
```
