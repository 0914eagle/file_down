
def calculate_convenience(n, stations):
    count = 0
    for x in range(1, n+1):
        y = stations[x-1]
        while y != x:
            count += 1
            y = stations[y-1]
    return count + n

# Input handling
n = int(input())
stations = list(map(int, input().split()))

# Calculate maximum convenience
max_convenience = calculate_convenience(n, stations)
print(max_convenience)
```
