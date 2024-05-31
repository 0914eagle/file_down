
def compute_gis(n, permutation):
    gis = []  # Initialize list to store GIS elements
    gis.append(permutation[0])  # Add the first element to GIS
    for i in range(1, n):
        if permutation[i] > gis[-1]:  # Check if current element is larger than last element in GIS
            gis.append(permutation[i])  # Add current element to GIS
    return gis

# Read input
n = int(input())
permutation = list(map(int, input().split()))

# Compute GIS
gis = compute_gis(n, permutation)

# Output the length of GIS and the GIS elements
print(len(gis))
print(*gis)
