
def farm(b, d, c, l):
    if b + d + c == l:
        print(b, d, c)
    elif b + d + c < l:
        for i in range(1, l - b - d):
            if b + d + i == l:
                print(b, d, i)
            elif b + d + i < l:
                for j in range(1, l - b - d - i):
                    if b + d + i + j == l:
                        print(b, d, j)
                    elif b + d + i + j < l:
                        for k in range(1, l - b - d - i - j):
                            if b + d + i + j + k == l:
                                print(b, d, k)

b, d, c, l = map(int, input().split())
farm(b, d, c, l)

