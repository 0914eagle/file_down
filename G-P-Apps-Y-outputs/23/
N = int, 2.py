
N = int(input())
diameters = [int(input()) for _ in range(N)]

unique_diameters = set(diameters)
max_layers = len(unique_diameters)

print(max_layers)
```
