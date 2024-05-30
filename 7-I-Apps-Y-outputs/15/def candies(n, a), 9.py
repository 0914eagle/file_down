
def candies(n, a):
    even_sum = 0
    odd_sum = 0
    for i in range(n):
        if i % 2 == 0:
            even_sum += a[i]
        else:
            odd_sum += a[i]
    if even_sum == odd_sum:
        return n - 1
    else:
        return 0



