
def tower_of_hanoi_cost(t, n):
    def hanoi(n, source, target, aux):
        if n == 1:
            return t[source][target]
        return hanoi(n - 1, source, aux, target) + t[source][target] + hanoi(n - 1, aux, target, source)

    return hanoi(n, 0, 2, 1)

# Input
t = []
for _ in range(3):
    t.append(list(map(int, input().split())))

n = int(input())

# Output
print(tower_of_hanoi_cost(t, n))
```
