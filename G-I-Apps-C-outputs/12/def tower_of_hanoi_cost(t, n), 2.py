
import sys

def tower_of_hanoi_cost(t, n):
    def hanoi_cost(n, i, j, k):
        if n == 1:
            return t[i][j]
        return min(hanoi_cost(n-1, i, k, j) + t[i][j] + hanoi_cost(n-1, k, j, i), hanoi_cost(n-1, i, j, k) + t[i][k] + hanoi_cost(n-1, j, i, k) + t[k][j] + hanoi_cost(n-1, i, j, k))
    
    return hanoi_cost(n, 0, 2, 1)

# Read input values
t = [list(map(int, input().split())) for _ in range(3)]
n = int(input())

# Calculate and print the minimum cost
print(tower_of_hanoi_cost(t, n))
```
