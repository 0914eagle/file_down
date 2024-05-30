
def sum_of_powers(n, l):
    x = 0
    for i in range(len(l)):
        x += l[i] ** n[i]
    return x

n = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
print(sum_of_powers(n, l))

