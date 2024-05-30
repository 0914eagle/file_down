
def candies(n, a):
    odd, even = 0, 0
    for i in range(n):
        if i % 2 == 0:
            odd += a[i]
        else:
            even += a[i]
    if odd == even:
        return n - 1
    else:
        return 0

