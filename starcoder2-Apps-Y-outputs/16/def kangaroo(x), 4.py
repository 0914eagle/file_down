
def kangaroo(x):
    t = 0
    while True:
        if x % 2 == 0:
            x = x / 2
        else:
            x = (x + 1) / 2
        t += 1
        if x == 1:
            return t

print(kangaroo(int(input())))

