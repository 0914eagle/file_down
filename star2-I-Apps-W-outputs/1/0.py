
n, l, r = map(int, input().split())

def get_sum(n, l, r):
    if l == r:
        return sum([1] * n)
    elif l == 1:
        return sum([2 ** i for i in range(n)])
    else:
        return sum([1] * (n - l + 1)) + sum([2 ** i for i in range(l - 1)])

print(get_sum(n, l, r), get_sum(n, 1, r))

