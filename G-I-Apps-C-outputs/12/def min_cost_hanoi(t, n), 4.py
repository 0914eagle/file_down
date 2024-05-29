
def min_cost_hanoi(t, n):
    def hanoi(n, source, target, auxiliary):
        if n == 1:
            return t[source][target]
        return hanoi(n-1, source, auxiliary, target) + t[source][target] + hanoi(n-1, auxiliary, target, source)

    return hanoi(n, 0, 2, 1)

# Input processing
matrix = [list(map(int, input().split())) for _ in range(3)]
n = int(input())

# Calculate and print the minimum cost of solving SmallY's puzzle
print(min_cost_hanoi(matrix, n))
```
