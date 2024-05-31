
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def f(x, n, a):
    freq = [0] * (n + 1)
    for i in range(1, n + 1):
        freq[min(i, a[i - 1]) + 1] += 1
    for i in range(2, n + 1):
        freq[i] += freq[i - 1]
    ans = 0
    for i in range(1, n + 1):
        if i * x > freq[n] + i:
            break
        if i % 2 == 1:
            ans += nCr(freq[n] + i - i * x, i)
        else:
            ans -= nCr(freq[n] + i - i * x, i)
    return ans

n, p = map(int, input().split())
a = list(map(int, input().split()))

good_numbers = []
for x in range(1, 2001):
    if f(x, n, a) % p != 0:
        good_numbers.append(x)

print(len(good_numbers))
print(*good_numbers)
