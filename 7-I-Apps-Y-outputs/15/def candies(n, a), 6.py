
def candies(n, a):
    if n == 1:
        return 0
    a.sort()
    odd, even = 0, 0
    for i in range(1, n):
        if a[i] - a[i - 1] == 1:
            odd += a[i - 1]
            even += a[i]
        else:
            break
    if odd == even:
        return n - 1
    return 0



