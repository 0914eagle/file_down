
def compute_GIS(N, A):
    gis = []
    gis.append(A[0])
    
    for i in range(1, N):
        if A[i] > gis[-1]:
            gis.append(A[i])
    
    return gis

# Input
N = int(input())
A = list(map(int, input().split()))

# Compute GIS
gis = compute_GIS(N, A)

# Output
print(len(gis))
print(*gis)
