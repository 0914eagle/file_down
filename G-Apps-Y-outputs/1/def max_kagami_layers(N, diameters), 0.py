
def max_kagami_layers(N, diameters):
    unique_diameters = set(diameters)
    return len(unique_diameters)

# Read input
N = int(input())
diameters = [int(input()) for _ in range(N)]

# Call the function and print the output
print(max_kagami_layers(N, diameters))
