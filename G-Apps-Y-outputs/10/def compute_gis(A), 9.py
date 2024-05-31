
def compute_gis(A):
    gis = []
    for a in A:
        if not gis or a > gis[-1]:
            gis.append(a)
    return gis

N = int(input())
A = list(map(int, input().split()))

gis = compute_gis(A)
print(len(gis))
print(' '.join(map(str, gis)))
