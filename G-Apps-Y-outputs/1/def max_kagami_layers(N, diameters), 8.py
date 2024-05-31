
def max_kagami_layers(N, diameters):
    diameters.sort(reverse=True)  # Sort the mochi diameters in descending order
    unique_diameters = list(set(diameters))  # Get unique diameters
    return len(unique_diameters)

# Read input
N = int(input())
diameters = [int(input()) for _ in range(N)]

# Call the function and print the output
print(max_kagami_layers(N, diameters))
