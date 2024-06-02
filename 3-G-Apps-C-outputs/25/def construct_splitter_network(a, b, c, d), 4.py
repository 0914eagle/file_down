
def construct_splitter_network(a, b, c, d):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def simplify_fraction(num, den):
        common_divisor = gcd(num, den)
        return num // common_divisor, den // common_divisor

    def construct_splitter(a, b, c, d):
        if a == c and b == d:
            return []

        if a == 0 or b == 0:
            return []

        if a == c:
            return [(0, -1, -1)]

        if b == d:
            return [(0, -2, -2)]

        if a < b:
            a, b, c, d = b, a, d, c

        x, y = simplify_fraction(c, d)
        if x == 1:
            return [(0, 1, 2)]

        return [(0, 1, -1), (0, 2, -2)]

    result = construct_splitter(a, b, c, d)
    n = len(result)
    print(n)
    for i in range(n):
        print(result[i][1], result[i][2])

# Input
a, b = map(int, input().split())
c, d = map(int, input().split())

# Output
construct_splitter_network(a, b, c, d)
