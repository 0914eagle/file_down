
A,B = map(int,input().split())
L = int(input())
count_insecure = 0
count_secure = 0
count_super_secure = 0
for i in range(1,L+1):
    for j in range(-A,B+1):
        if (i,j) != (0,-A) and (i,j) != (0,B):
            if (i,j) == (0,-A) or (i,j) == (0,B):
                count_secure += 1
            else:
                count_insecure += 1
print(count_insecure)
print(count_secure)
print(count_super_secure)

