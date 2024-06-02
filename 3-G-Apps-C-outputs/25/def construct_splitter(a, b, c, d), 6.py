
def construct_splitter(a, b, c, d):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x * y // gcd(x, y)

    def find_factors(num):
        factors = []
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                factors.append(i)
                factors.append(num // i)
        return factors

    def construct_belt_network(a, b, c, d):
        ratio = c / d
        factors = find_factors(a + b)
        for factor in factors:
            if factor * ratio % 1 == 0:
                k = int(factor * ratio)
                if k <= a + b:
                    return factor, k

    factor, k = construct_belt_network(a, b, c, d)

    n = factor - 1
    print(n)
    for i in range(n):
        if i == 0:
            print(-2, -1)
        else:
            print(i - 1, i)

    for i in range(n):
        if i == k - 1:
            print(0, -2)
        else:
            print(i, i + 1)

# Input
a, b = map(int, input().split())
c, d = map(int, input().split())

construct_splitter(a, b, c, d)
