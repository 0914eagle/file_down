
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def number_of_ways_to_make_two_round_dances(n):
    return factorial(n // 2 - 1) // 2

n = int(input())
print(number_of_ways_to_make_two_round_dances(n))
```
