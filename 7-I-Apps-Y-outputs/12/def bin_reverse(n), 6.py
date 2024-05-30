
def bin_reverse(n):
    return int(str(bin(n))[2:][::-1], 2)

print(bin_reverse(int(input())))

