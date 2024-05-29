
def tower_of_hanoi_cost(t, n):
    def hanoi(n, start, end, middle):
        if n == 1:
            return t[start][end]
        return hanoi(n-1, start, middle, end) + t[start][end] + hanoi(n-1, middle, end, start)

    return hanoi(n, 0, 2, 1)

# Input
t = []
for _ in range(3):
    t.append(list(map(int, input().split())))
n = int(input())

# Output
print(tower_of_hanoi_cost(t, n))
```
