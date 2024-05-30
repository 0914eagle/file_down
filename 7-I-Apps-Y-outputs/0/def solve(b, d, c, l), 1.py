
def solve(b, d, c, l):
    for i in range(b+1):
        for j in range(d+1):
            for k in range(c+1):
                if i*4+j*4+k*2==l:
                    print(i,j,k)

