
def pages(n):
    if n % 2 == 0:
        return n / 2
    else:
        return (n // 2) + 1

print(pages(int(input())))
