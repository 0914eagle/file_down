
def valeras_positions(a, d, n):
    x = 0.0
    y = 0.0
    for i in range(1, n+1):
        x += min(d, a)
        if x >= a:
            y = min(x - a, d)
            x = a
        print("{:.10f} {:.10f}".format(x, y))

# Input
a, d = map(float, input().split())
n = int(input())

# Output
valeras_positions(a, d, n)
[/PYTHON