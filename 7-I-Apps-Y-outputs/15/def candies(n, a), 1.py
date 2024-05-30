
def candies(n, a):
    a.sort()
    odd = sum(a[1::2])
    even = sum(a[::2])
    cnt = 0
    for i in range(1, n):
        if odd - a[i] == even - a[i - 1]:
            cnt += 1
    return cnt

