
def compute_gis(A):
    n = len(A)
    gis = []
    gis.append(A[0])
    for i in range(1, n):
        if A[i] > gis[-1]:
            gis.append(A[i])
    return gis

# Input processing
N = int(input())
A = list(map(int, input().split()))

# Compute GIS
gis = compute_gis(A)

# Output result
print(len(gis))
print(*gis)
