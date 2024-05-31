
def max_kagami_layers(N, mochi_diameters):
    unique_diameters = set(mochi_diameters)
    return len(unique_diameters)

# Read input
N = int(input())
mochi_diameters = [int(input()) for _ in range(N)]

# Call function and print output
result = max_kagami_layers(N, mochi_diameters)
print(result)
