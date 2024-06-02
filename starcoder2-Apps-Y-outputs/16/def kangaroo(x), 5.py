
def kangaroo(x):
    i = 0
    while i <= x:
        if i * (i + 1) >= 2 * x:
            return i
        i += 1

print(kangaroo(int(input())))

