
# Read input
N = int(input())
diameters = []
for _ in range(N):
    diameters.append(int(input()))

# Sort the diameters in descending order
diameters.sort(reverse=True)

# Count the number of unique diameters
unique_diameters = len(set(diameters))

print(unique_diameters)
```
