
def solve(l):
    l_bin = bin(l)[2:]
    count = 0
    for i in range(len(l_bin)):
        if l_bin[i] == '1':
            count += 2 ** i
    return count % (10 ** 9 + 7)

l = int(input(), 2)
print(solve(l))

