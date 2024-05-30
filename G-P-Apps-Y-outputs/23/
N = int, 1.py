
N = int(input())
mochi_diameters = []
for _ in range(N):
    mochi_diameters.append(int(input()))
    
unique_diameters = set(mochi_diameters)
max_layers = len(unique_diameters)
print(max_layers)
```
