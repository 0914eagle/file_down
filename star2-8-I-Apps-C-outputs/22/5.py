
A, B = map(int, input().split())
L = int(input())

insecure = 0
secure = 0
super_secure = 0

for x in range(1, L+1):
    for y in range(-A, B+1):
        if (y == -A or y == B):
            if (y != -A or y != B):
                insecure += 1
        else:
            super_secure += 1

print(insecure)
print(secure)
print(super_secure)

