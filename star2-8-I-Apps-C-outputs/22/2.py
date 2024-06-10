
def count_vaults(A, B, L):
    insecure = 0
    secure = 0
    super_secure = 0
    for x in range(1, L+1):
        for y in range(-A, B+1):
            if y != -A and y != B:
                super_secure += 1
            elif y == -A:
                secure += 1
            else:
                insecure += 1
    return insecure, secure, super_secure


A, B = map(int, input().split())
L = int(input())
insecure, secure, super_secure = count_vaults(A, B, L)
print(insecure)
print(secure)
print(super_secure)

