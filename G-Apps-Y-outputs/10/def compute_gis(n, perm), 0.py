
def compute_gis(n, perm):
    gis = [perm[0]]
    for i in range(1, n):
        if perm[i] > gis[-1]:
            gis.append(perm[i])
    return len(gis), gis

# Read input
n = int(input())
perm = list(map(int, input().split()))

# Compute the GIS
length, gis = compute_gis(n, perm)

# Output the result
print(length)
print(*gis)
