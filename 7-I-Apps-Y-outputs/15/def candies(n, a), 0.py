
def candies(n, a):
    odd_sum = 0
    even_sum = 0
    for i in range(n-1):
        if i % 2 == 0:
            odd_sum += a[i]
            even_sum += a[i+1]
        else:
            odd_sum += a[i+1]
            even_sum += a[i]
        if odd_sum != even_sum:
            return 0
    return 1

