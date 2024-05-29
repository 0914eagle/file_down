
def tower_of_hanoi_cost(t, n):
    def move(disks, start, end, temp):
        if disks == 1:
            return t[start][end]
        return move(disks - 1, start, temp, end) + t[start][end] + move(disks - 1, temp, end, start)

    return move(n, 0, 2, 1)

# Parse input
t = [list(map(int, input().split())) for _ in range(3)]
n = int(input())

# Calculate and output the minimum cost
print(tower_of_hanoi_cost(t, n))
```
