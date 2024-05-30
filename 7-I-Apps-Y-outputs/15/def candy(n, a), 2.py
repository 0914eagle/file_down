
def candy(n, a):
    a.sort()
    odd = 0
    even = 0
    for i in range(n-1):
        if i % 2 == 0:
            odd += a[i]
        else:
            even += a[i]
    if odd == even:
        return n-1
    else:
        return 0



