
import math

# Function to calculate the number of sets that can be split equally
def checkers_candy_sets(n, m):
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            candies = i ** 2 + j ** 2
            if candies % m == 0:
                count += 1
    return count

# Reading input
n, m = map(int, input().split())

# Calling the function and printing the result
print(checkers_candy_sets(n, m))
```
