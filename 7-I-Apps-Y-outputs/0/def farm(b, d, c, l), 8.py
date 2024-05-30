
def farm(b, d, c, l):
    if l < b + d + c:
        print("impossible")
    else:
        for i in range(l - b - d + 1):
            for j in range(l - b - d + 1 - i):
                k = l - b - d - i - j
                if i + j + k == b + d + c:
                    print(i, j, k)

