
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_sequences(x, y):
    MOD = 10**9 + 7

    if y % x != 0:
        return 0

    y //= x
    divisors = []
    for i in range(1, int(y**0.5)+1):
        if y % i == 0:
            if i != y // i:
                divisors.extend([i, y // i])
            else:
                divisors.append(i)

    result = 0
    for d in divisors:
        if d % x == 0:
            result = (result + pow(2, d-1, MOD)) % MOD

    return result

x, y = map(int, input().split())
print(count_sequences(x, y))
