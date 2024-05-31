
a, d = map(float, input().split())
n = int(input())

for i in range(1, n+1):
    meters_covered = i * d
    x = min(meters_covered % (4*a), a)
    y = min((meters_covered - x) % (4*a), a)

    if meters_covered <= a:
        print("{:.10f} {:.10f}".format(x, y))
    elif meters_covered <= 2*a:
        print("{:.10f} {:.10f}".format(a, y))
    elif meters_covered <= 3*a:
        print("{:.10f} {:.10f}".format(a, a - x))
    else:
        print("{:.10f} {:.10f}".format(0, a - y))
