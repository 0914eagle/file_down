
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

def f(x, a):
    count = 0
    for i in range(1, x+1):
        if all(i >= ai for ai in a):
            count += 1
    return count

def is_good(x, p, a):
    return f(x, a) % p != 0

n, p = map(int, input().split())
a = list(map(int, input().split()))

good_numbers = []
for x in range(1, 2001):
    if is_good(x, p, a):
        good_numbers.append(x)

print(len(good_numbers))
print(*good_numbers)
