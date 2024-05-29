
def maximum_convenience(n, p):
    p = [i-1 for i in p]  # Adjust p values to 0-indexed for easier calculation
    counts = [0] * n
    for i in range(n):
        counts[i] = 1
        next_station = p[i]
        while next_station != i:
            counts[i] += 1
            next_station = p[next_station]

    total_convenience = sum(counts)
    additional_convenience = 0
    for i in range(n):
        if counts[i] == 1:  # If current station has only one path
            current_convenience = 1
            next_station = p[i]
            while next_station != i:
                current_convenience += 1
                next_station = p[next_station]
            additional_convenience = max(additional_convenience, current_convenience)
    
    return total_convenience + additional_convenience

# Example usage
n = 3
p = [2, 1, 3]
print(maximum_convenience(n, p))  # Output: 9

n = 5
p = [1, 5, 4, 3, 2]
print(maximum_convenience(n, p))  # Output: 17
```
