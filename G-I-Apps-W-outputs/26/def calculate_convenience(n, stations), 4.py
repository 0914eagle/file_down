
def calculate_convenience(n, stations):
    num_pairs = 0
    for i in range(1, n+1):
        j = stations.index(i) + 1
        num_pairs += 1 + 2*(j-1)*(n-j)  # calculate the number of pairs for each station
    return num_pairs

# Input reading
n = int(input())
stations = list(map(int, input().split()))

# Output
print(calculate_convenience(n, stations))
```
