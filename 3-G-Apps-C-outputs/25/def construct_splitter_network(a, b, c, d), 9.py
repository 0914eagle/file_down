
def construct_splitter_network(a, b, c, d):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def simplify_fraction(num, denom):
        common_divisor = gcd(num, denom)
        return num // common_divisor, denom // common_divisor

    def add_splitter(left, right):
        nonlocal splitter_count
        splitter_count += 1
        splitters.append((left, right))

    def build_network(a, b, c, d):
        if a == c:
            add_splitter(-2, -1)
            return
        if a == d:
            add_splitter(-1, -2)
            return
        if b == c:
            add_splitter(-1, -2)
            return
        if b == d:
            add_splitter(-2, -1)
            return

        if a * d < b * c:
            add_splitter(-1, splitter_count + 1)
            build_network(a, b, c - a, d)
            add_splitter(splitter_count - 1, -2)
            build_network(a, b, a, d)
        else:
            add_splitter(splitter_count + 1, -2)
            build_network(a - b, b, c, d)
            add_splitter(-1, splitter_count - 1)
            build_network(b, b, c, d)

    a, b = simplify_fraction(a, b)
    c, d = simplify_fraction(c, d)

    splitter_count = 0
    splitters = []

    build_network(a, b, c, d)

    print(splitter_count)
    for left, right in splitters:
        print(left, right)

# Input
a, b = map(int, input().split())
c, d = map(int, input().split())

# Output
construct_splitter_network(a, b, c, d)
