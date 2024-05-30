
def candies(n, a):
    if n == 1:
        return 0
    if n == 2:
        return 1
    even_sum = 0
    odd_sum = 0
    for i in range(1, n):
        if i % 2 == 0:
            even_sum += a[i]
        else:
            odd_sum += a[i]
    if even_sum == odd_sum:
        return n - 1
    else:
        return 0



