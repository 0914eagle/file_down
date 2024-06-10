
A, B = map(int, input().split())
L = int(input())

def check_guard(x, y, A, B):
    if (y == -A and x > 0) or (y == B and x < L):
        return True
    else:
        return False

def check_vault(x, y, A, B, L):
    for i in range(1, L+1):
        if check_guard(i, -A, A, B) and check_guard(x-i, y, A, B):
            return True
        if check_guard(i, B, A, B) and check_guard(x-i, y, A, B):
            return True
    
    return False

insecure = 0
secure = 0
super_secure = 0

for x in range(1, L+1):
    for y in range(-A, B+1):
        if check_vault(x, y, A, B, L):
            super_secure += 1
        elif check_guard(x, y, A, B) or check_guard(0, y, A, B):
            secure += 1
        else:
            insecure += 1

print(insecure)
print(secure)
print(super_secure)

