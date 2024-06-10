
A, B = map(int, input().split())
L = int(input())
def num_vaults(A, B, L):
    return L * (A + 1 + B)
def num_insecure(A, B, L):
    insecure = 0
    for x in range(1, L+1):
        for y in range(-A, B+1):
            dist1 = abs(y + A)
            dist2 = abs(y - B)
            if dist1 < x and dist2 < x:
                insecure += 1
    return insecure
def num_secure(A, B, L):
    secure = 0
    for x in range(1, L+1):
        for y in range(-A, B+1):
            dist1 = abs(y + A)
            dist2 = abs(y - B)
            if (dist1 < x and dist2 >= x) or (dist1 >= x and dist2 < x):
                secure += 1
    return secure
def num_super_secure(A, B, L):
    return num_vaults(A, B, L) - num_insecure(A, B, L) - num_secure(A, B, L)
print(num_insecure(A, B, L))
print(num_secure(A, B, L))
print(num_super_secure(A, B, L))

