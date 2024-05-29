
def tower_of_hanoi_cost(t, n):
    def hanoi(n, src, dest, temp):
        if n == 1:
            return t[src][dest]
        return hanoi(n - 1, src, temp, dest) + t[src][dest] + hanoi(n - 1, temp, dest, src)

    return hanoi(n, 0, 2, 1)

# Input
t = [list(map(int, input().split())) for _ in range(3)]
n = int(input())

# Output
print(tower_of_hanoi_cost(t, n))
```
