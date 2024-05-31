
def count_sequences(x, y):
    mod = 10**9 + 7
    if y % x != 0:
        return 0

    y //= x

    def power(a, b, c):
        res = 1
        while b > 0:
            if b % 2 == 1:
                res = (res * a) % c
            a = (a * a) % c
            b //= 2
        return res

    def count_divisors(n):
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if n // i == i:
                    count += 1
                else:
                    count += 2
        return count

    result = 0
    divisor_count = count_divisors(y)
    
    for i in range(1, int(y**0.5) + 1):
        if y % i == 0 and count_divisors(i) == x:
            result = (result + power(2, divisor_count - 1, mod)) % mod

        if y % (y // i) == 0 and count_divisors(y // i) == x and i * i != y:
            result = (result + power(2, divisor_count - 1, mod)) % mod

    return result

x, y = map(int, input().split())
print(count_sequences(x, y))
