
def max_kagami_mochi_layers(N, diameters):
    diameters.sort(reverse=True)
    unique_diameters = set(diameters)
    return len(unique_diameters)

N = int(input())
diameters = []
for _ in range(N):
    diameters.append(int(input()))

result = max_kagami_mochi_layers(N, diameters)
print(result)
