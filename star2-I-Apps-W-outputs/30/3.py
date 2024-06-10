
def linear_function(a, b, x):
    return (a * x) + b


def g_function(a, b, n, x):
    result = x
    for i in range(n):
        result = linear_function(a, b, result)
    return result


def main():
    a, b, n, x = map(int, input().split())
    print(g_function(a, b, n, x) % (10 ** 9 + 7))


if __name__ == '__main__':
    main()


