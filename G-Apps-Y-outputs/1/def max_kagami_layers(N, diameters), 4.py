
def max_kagami_layers(N, diameters):
    diameters.sort(reverse=True)
    unique_diameters = list(set(diameters))
    return len(unique_diameters)

# Read input
N = int(input())
diameters = [int(input()) for _ in range(N)]

# Call the function and print the result
print(max_kagami_layers(N, diameters))
