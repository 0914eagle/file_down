


def candies(n, a):
    if n == 1:
        return 0
    odd = sum(a[0::2])
    even = sum(a[1::2])
    if odd == even:
        return n - 1
    else:
        return 0



