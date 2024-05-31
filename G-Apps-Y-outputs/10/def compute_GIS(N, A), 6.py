
def compute_GIS(N, A):
    gis = [A[0]]
    for i in range(1, N):
        if A[i] > gis[-1]:
            gis.append(A[i])
    return len(gis), gis

# Read input
N = int(input())
A = list(map(int, input().split()))

# Compute GIS
length, gis = compute_GIS(N, A)

# Output result
print(length)
print(" ".join(map(str, gis)))
