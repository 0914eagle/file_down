
A, B = [int(x) for x in input().split()]
L = int(input())

vaults = [(x, y) for x in range(1, L+1) for y in range(-A, B+1)]

insecure = 0
secure = 0
super_secure = 0

for vault in vaults:
    if (0, -A) == vault or (0, B) == vault:
        continue
    
    if (0, -A) in line_segment(vault, (0, B)) or (0, B) in line_segment(vault, (0, -A)):
        continue
    
    if (0, -A) in line_segment(vault, (0, B)):
        insecure += 1
    
    elif (0, B) in line_segment(vault, (0, -A)):
        insecure += 1
    
    else:
        secure += 1
        super_secure += 1

print(insecure)
print(secure)
print(super_secure)

