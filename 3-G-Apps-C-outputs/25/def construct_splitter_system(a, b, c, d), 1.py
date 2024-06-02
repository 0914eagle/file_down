
def construct_splitter_system(a, b, c, d):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def simplify_fraction(num, den):
        divisor = gcd(num, den)
        return num // divisor, den // divisor

    def add_splitter(left, right):
        nonlocal splitter_count
        splitter_count += 1
        splitters.append((left, right))

    def build_splitter_system(num, den):
        if num == 0:
            return
        if num == den:
            add_splitter(-2, -1)
            return
        ratio = num / den
        if ratio > 0.5:
            add_splitter(-2, splitter_count + 1)
            build_splitter_system(num - den // 2, den // 2)
        else:
            add_splitter(-2, splitter_count + 1)
            add_splitter(splitter_count, -1)
            build_splitter_system(num, den - num)

    a, b = simplify_fraction(a, b)
    c, d = simplify_fraction(c, d)
    splitter_count = 0
    splitters = []

    build_splitter_system(c, c + d)

    print(len(splitters))
    for left, right in splitters:
        print(left, right)

# Input parsing
a, b = map(int, input().split())
c, d = map(int, input().split())

construct_splitter_system(a, b, c, d)
