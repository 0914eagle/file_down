
def max_kagami_layers(N, mochi_diameters):
    mochi_diameters.sort(reverse=True)
    unique_diameters = list(set(mochi_diameters))
    return len(unique_diameters)

# Input processing
N = int(input())
mochi_diameters = []
for i in range(N):
    mochi_diameters.append(int(input()))

# Call the function and output the result
print(max_kagami_layers(N, mochi_diameters))
