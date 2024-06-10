
A = int(input().split()[0])
B = int(input().split()[1])
L = int(input())

def is_secure(x, y):
    if (x == 0 and y == -A) or (x == 0 and y == B):
        return 0 # insecure
    elif (x == 0 and y != -A and y != B):
        return 1 # secure
    else:
        return 2 # super-secure

insecure = 0
secure = 0
super_secure = 0
for x in range(1, L+1):
    for y in range(-A, B+1):
        if is_secure(x, y) == 0:
            insecure += 1
        elif is_secure(x, y) == 1:
            secure += 1
        elif is_secure(x, y) == 2:
            super_secure += 1

print(insecure)
print(secure)
print(super_secure)

