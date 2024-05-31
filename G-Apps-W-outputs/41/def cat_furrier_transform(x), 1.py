
def cat_furrier_transform(x):
    operations = []

    while x % 2 == 0:
        x //= 2

    if x == 1:
        print(0)
    else:
        t = 0
        while (x+1) & x != 0:
            t += 1
            if t % 2 == 1:
                for i in range(30):
                    if x < 2**i:
                        operations.append(i)
                        x ^= 2**i - 1
                        break
            else:
                x += 1

        print(t)
        for i in range(0, t, 2):
            print(operations[i], end=' ')

# Input
x = int(input())
cat_furrier_transform(x)
