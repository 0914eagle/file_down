
def max_layers_of_kagami_mochi(N, mochi_diameters):
    unique_diameters = set(mochi_diameters)
    return len(unique_diameters)

N = int(input())
mochi_diameters = [int(input()) for _ in range(N)]
print(max_layers_of_kagami_mochi(N, mochi_diameters))
```
