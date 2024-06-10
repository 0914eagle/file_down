
import math

def solve(X):
    for b in range(1, int(math.sqrt(X)) + 1):
        for p in range(2, int(math.log(X, b)) + 1):
            if b ** p <= X:
                max_power = b ** p
    return max_power

X = int(input())
print(solve(X))

