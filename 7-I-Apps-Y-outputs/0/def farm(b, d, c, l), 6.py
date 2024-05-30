
def farm(b, d, c, l):
    if b+d+c == l:
        print(b, d, c)
    elif b+d+c < l:
        for i in range(b+1):
            j = l-b-i
            if j > 0 and j <= d+c:
                print(i, j, l-b-i-j)
farm(int(input()), int(input()), int(input()), int(input()))

