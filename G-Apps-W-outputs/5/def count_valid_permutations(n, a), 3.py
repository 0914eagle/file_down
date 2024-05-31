
def count_valid_permutations(n, a):
    valid_permutations = 0
    for x in range(1, 2001):
        f_x = 1
        for i in range(n):
            if a[i] <= x:
                f_x *= (i + 1)
                f_x %= p
        if f_x % p != 0:
            valid_permutations += 1
    return valid_permutations

n, p = map(int, input().split())
a = list(map(int, input().split()))

good_integers = []
for x in range(1, 2001):
    f_x = 1
    for i in range(n):
        if a[i] <= x:
            f_x *= (i + 1)
            f_x %= p
    if f_x % p != 0:
        good_integers.append(x)

print(len(good_integers))
print(*good_integers)
