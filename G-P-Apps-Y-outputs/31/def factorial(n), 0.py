
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def number_of_ways(n):
    return factorial(n//2 - 1) // 2

n = int(input())
result = number_of_ways(n)
print(result)
```
