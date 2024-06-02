
def construct_splitter_system(a, b, c, d):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def simplify_ratio(x, y):
        g = gcd(x, y)
        return x // g, y // g

    def construct_splitter(a, b, c, d):
        if a == c and b == d:
            return [(0, -2, -1)]
        
        if a * d < b * c:
            return [(0, -2, -1)]
        
        if a * d > b * c:
            return [(0, -1, -2)]
        
        x, y = simplify_ratio(a, b)
        return [(0, 1, 2), (-1, 0, -2), (-2, 0, -1)]

    splitters = construct_splitter(a, b, c, d)
    n = len(splitters)
    print(n)
    for splitter in splitters:
        print(" ".join(map(str, splitter)))

# Input parsing
a, b = map(int, input().split())
c, d = map(int, input().split())

construct_splitter_system(a, b, c, d)
