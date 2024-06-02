
def construct_splitter(a, b, c, d):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def reduce_ratio(x, y):
        g = gcd(x, y)
        return x // g, y // g

    def find_splitter_ratio(a, b, c, d):
        x = c
        y = d
        while x != a or y != b:
            if x / y > a / b:
                x, y = x - a, y - b
            else:
                x, y = x + a, y + b
        return x, y

    a, b = reduce_ratio(a, b)
    c, d = reduce_ratio(c, d)

    x, y = find_splitter_ratio(a, b, c, d)

    res = []
    while x != c or y != d:
        if x / y > c / d:
            res.append((-2, -1))
            x, y = x - c, y - d
        else:
            res.append((-1, -2))
            c, d = c - x, d - y

    return len(res), res

# Input
a, b = map(int, input().split())
c, d = map(int, input().split())

# Output
n, splitters = construct_splitter(a, b, c, d)
print(n)
for l, r in splitters:
    print(l, r)
