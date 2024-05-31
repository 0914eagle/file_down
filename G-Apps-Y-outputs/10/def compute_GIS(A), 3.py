
def compute_GIS(A):
    n = len(A)
    gis = [A[0]]
    for i in range(1, n):
        if A[i] > gis[-1]:
            gis.append(A[i])
    return gis

# Input
N = int(input())
A = list(map(int, input().split()))

# Compute GIS
gis = compute_GIS(A)

# Output
print(len(gis))
print(*gis)
