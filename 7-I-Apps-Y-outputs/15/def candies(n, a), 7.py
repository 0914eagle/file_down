
def candies(n, a):
    even_sum = 0
    odd_sum = 0
    even_candies = 0
    odd_candies = 0
    for i in range(n-1):
        if i % 2 == 0:
            even_sum += a[i]
            odd_candies += 1
        else:
            odd_sum += a[i]
            even_candies += 1
        if even_sum == odd_sum:
            even_candies += 1
            odd_candies += 1
            even_sum = 0
            odd_sum = 0
    return even_candies

print(candies(int(input()), list(map(int, input().split()))))

