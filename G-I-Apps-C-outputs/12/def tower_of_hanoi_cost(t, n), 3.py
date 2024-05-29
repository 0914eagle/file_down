
def tower_of_hanoi_cost(t, n):
    def min_cost(n, start, target, aux):
        if n == 1:
            return t[start][target]
        return min(min_cost(n-1, start, aux, target) + t[start][target] + min_cost(n-1, aux, target, start), 2 * min_cost(n-1, start, target, aux) + t[start][aux] + t[aux][target])

    return min_cost(n, 0, 2, 1)

# Input parsing
t = [list(map(int, input().strip().split())) for _ in range(3)]
n = int(input().strip())

result = tower_of_hanoi_cost(t, n)
print(result)
```
