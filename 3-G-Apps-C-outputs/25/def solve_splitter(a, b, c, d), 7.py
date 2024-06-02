
def solve_splitter(a, b, c, d):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x * y // gcd(x, y)

    def build_splitter_network(a, b, c, d):
        if a == c and b == d:
            return 0, []

        ratio = a / b
        target_ratio = c / d
        lcm_ab = lcm(a, b)

        if ratio < target_ratio:
            left_ratio = a / lcm_ab
            right_ratio = b / lcm_ab
            left_count = c // left_ratio
            right_count = d // right_ratio

            if left_count * left_ratio == c and right_count * right_ratio == d:
                return 1, [[-2, -1]]

        return 3, [[-1, 1], [2, 1], [0, -2]]

    num_splitters, splitters = build_splitter_network(a, b, c, d)
    print(num_splitters)
    for splitter in splitters:
        print(*splitter)

# Input parsing
a, b = map(int, input().split())
c, d = map(int, input().split())

solve_splitter(a, b, c, d)
