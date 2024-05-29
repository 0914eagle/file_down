
def tower_of_hanoi_cost(t, n):
    def hanoi(n, source, target, auxiliary):
        if n == 1:
            return t[source][target]
        return hanoi(n-1, source, auxiliary, target) + t[source][target] + hanoi(n-1, auxiliary, target, source)

    return hanoi(n, 0, 2, 1)

# Input processing
matrix_t = [list(map(int, input().split())) for _ in range(3)]
n = int(input())

# Output
print(tower_of_hanoi_cost(matrix_t, n))
```
