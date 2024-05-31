
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def f(x, a):
    count = 0
    for perm in permutations(a):
        valid = True
        for i in range(len(perm)):
            if sum(a[j] <= a[perm[i]-1] for j in range(i+1)) < i + 1:
                valid = False
                break
        if valid:
            count += 1
    return count

def permutations(a):
    if len(a) == 1:
        yield [a[0]]
    else:
        for i in range(len(a)):
            sub = a[:i] + a[i+1:]
            for p in permutations(sub):
                yield [a[i]] + p

def good_integers(n, p, a):
    good_nums = []
    for x in range(1, n+1):
        if f(x, a) % p != 0:
            good_nums.append(x)
    return len(good_nums), good_nums

# Input Parsing
n, p = map(int, input().split())
a = list(map(int, input().split()))

# Calculate and Output
count, good_nums = good_integers(n, p, a)
print(count)
print(*good_nums)
