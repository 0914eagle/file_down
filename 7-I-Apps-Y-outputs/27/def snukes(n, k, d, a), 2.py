
def snukes(n, k, d, a):
    # Write your code here
    # print(n, k, d, a)
    snack = [0] * k
    for i in range(n):
        for j in range(d[i]):
            snack[a[i][j] - 1] += 1
    return sum(snack)

