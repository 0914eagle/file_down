
def compute_GIS(N, permutation):
    gis = []
    
    current_max = permutation[0]
    gis.append(current_max)
    
    for i in range(1, N):
        if permutation[i] > current_max:
            current_max = permutation[i]
            gis.append(current_max)
    
    return len(gis), gis

# Input
N = int(input())
permutation = list(map(int, input().split()))

# Compute GIS
length, gis_sequence = compute_GIS(N, permutation)

# Output
print(length)
print(*gis_sequence)
