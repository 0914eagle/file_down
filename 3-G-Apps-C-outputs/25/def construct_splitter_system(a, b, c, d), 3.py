
def construct_splitter_system(a, b, c, d):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def simplify_fraction(num, denom):
        divisor = gcd(num, denom)
        return num // divisor, denom // divisor

    def construct_splitter(a, b, c, d):
        if a == c and b == d:
            return []

        if a == 0:
            return construct_splitter(b, a, d, c)

        x, y = simplify_fraction(c, d)
        if a < b:
            return [(0, -2), (-1, 0)]
        else:
            return [(0, -1), (-2, 0)]

    splitters = construct_splitter(a, b, c, d)
    n = len(splitters)
    print(n)
    for splitter in splitters:
        print(splitter[0], splitter[1])

# Input parsing
a, b = map(int, input().split())
c, d = map(int, input().split())

construct_splitter_system(a, b, c, d)
