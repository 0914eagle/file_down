
def construct_network(a, b, c, d):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def simplify_fraction(num, den):
        common_divisor = gcd(num, den)
        return num // common_divisor, den // common_divisor

    def add_splitter(left, right):
        nonlocal splitter_count
        splitter_count += 1
        network.append((left, right))

    def build_network(a, b, c, d):
        if a == c and b == d:
            return

        if a * d > b * c:
            add_splitter(-2, -1)
            a, b = a + c, b + d
        else:
            p, q = simplify_fraction(c, d)
            add_splitter(-1, 0)
            build_network(a, b, p, q)
            add_splitter(0, -2)
            build_network(a, b, c - p, d - q)

    network = []
    splitter_count = 0
    build_network(a, b, c, d)

    print(splitter_count)
    for left, right in network:
        print(left, right)

# Input processing
a, b = map(int, input().split())
c, d = map(int, input().split())
construct_network(a, b, c, d)
