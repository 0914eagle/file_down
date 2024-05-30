

def candies(n, a):
    odd_sum = 0
    even_sum = 0
    for i in range(1, n):
        if i % 2 == 1:
            odd_sum += a[i]
        else:
            even_sum += a[i]
    if odd_sum == even_sum:
        return n - 1
    else:
        return 0



