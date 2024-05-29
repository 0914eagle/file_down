
def max_convenience(n, stations):
    count = 0
    for i in range(1, n+1):
        x = i
        y = stations[i-1]
        while y != i:
            count += 1
            y = stations[y-1]
    
    return count + n

# Input handling
n = int(input())
stations = list(map(int, input().split()))

print(max_convenience(n, stations))
```
