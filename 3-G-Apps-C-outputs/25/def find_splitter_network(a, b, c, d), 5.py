
def find_splitter_network(a, b, c, d):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    def get_ratio(x, y):
        g = gcd(x, y)
        return x // g, y // g

    def build_network(a, b, c, d):
        if a == 0:
            return []

        ratio = get_ratio(c, d)
        if a == ratio[0]:
            return [(-2, -1)]

        if a < ratio[0]:
            network = build_network(a, b, ratio[0] - a, ratio[1])
            return [(network[0][0], -1)] + network

        network = build_network(a - ratio[0], b, c, d)
        return [(network[0][0], -1), (network[0][1], -1)] + network[1:]

    network = build_network(a, b, c, d)
    n = len(network)
    print(n)
    for i in range(n):
        print(network[i][0], network[i][1])

# Input parsing
a, b = map(int, input().split())
c, d = map(int, input().split())

find_splitter_network(a, b, c, d)
