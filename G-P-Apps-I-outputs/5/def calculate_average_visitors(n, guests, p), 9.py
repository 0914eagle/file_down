
import math

def calculate_average_visitors(n, guests, p):
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)

    def count_visitors(perm):
        total = 0
        current_total = 0
        for guest in perm:
            current_total += guest
            if current_total <= p:
                total += 1
            else:
                break
        return total

    all_permutations = math.factorial(n)
    total_visitors = 0
    for perm in itertools.permutations(guests):
        total_visitors += count_visitors(perm)

    return total_visitors / all_permutations

# Input reading
n = int(input())
guests = list(map(int, input().split()))
p = int(input())

result = calculate_average_visitors(n, guests, p)
print(result)
```
