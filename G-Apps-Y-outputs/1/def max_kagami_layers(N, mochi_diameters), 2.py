
def max_kagami_layers(N, mochi_diameters):
    mochi_diameters.sort(reverse=True)
    unique_diameters = set(mochi_diameters)
    return len(unique_diameters)

# Input
N = int(input())
mochi_diameters = []
for _ in range(N):
    mochi_diameters.append(int(input()))

# Output
print(max_kagami_layers(N, mochi_diameters))
