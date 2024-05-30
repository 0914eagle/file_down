
def binary_reverse(n):
    return int(str(bin(n))[2:][::-1], 2)

print(binary_reverse(int(input())))

