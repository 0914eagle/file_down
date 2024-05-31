
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def is_good_integer(n, p, a):
    total_permutations = factorial(n)
    
    valid_permutations = 0
    for x in range(1, n+1):
        for i in range(n):
            if a[i] >= x:
                valid_permutations += nCr(n-1, i)
    
    if valid_permutations % p == 0:
        return False
    else:
        return True

n, p = map(int, input().split())
a = list(map(int, input().split()))

good_integers = []
for x in range(1, 2001):
    if is_good_integer(n, p, a):
        good_integers.append(x)

print(len(good_integers))
print(*good_integers)
