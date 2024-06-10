
def linear_function(a, b, x):
    return a * x + b


def g_function(a, b, n, x):
    result = x
    for _ in range(n):
        result = linear_function(a, b, result)
    return result


def solve(a, b, n, x):
    return g_function(a, b, n, x) % (10 ** 9 + 7)


a, b, n, x = map(int, input().split())
print(solve(a, b, n, x))

