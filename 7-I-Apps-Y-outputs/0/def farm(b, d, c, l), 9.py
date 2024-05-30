
def farm(b, d, c, l):
    if l < b+d+c:
        print("impossible")
    else:
        for i in range(l-b-d+1):
            for j in range(l-b-d+1-i):
                k = l - b - d - i - j
                if b+d+c == i+j+k:
                    print(i, j, k)

