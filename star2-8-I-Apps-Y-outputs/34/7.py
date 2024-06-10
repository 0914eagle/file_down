
def solve(h, w, a):
    return "#" * (w + 2) + "\n" + "\n".join(map(lambda s: "#" + s + "#", a)) + "\n" + "#" * (w + 2)

h, w = map(int, input().split())
a = [input() for _ in range(h)]
print(solve(h, w, a))

