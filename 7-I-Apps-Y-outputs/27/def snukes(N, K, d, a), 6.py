
def snukes(N, K, d, a):
    # Write your code here
    # return the number of snukes who have no snacks
    snukes = [0] * N
    for i in range(K):
        for j in range(d[i]):
            snukes[a[i][j] - 1] += 1
    return sum(1 for i in snukes if not i)

if __name__ == '__main__':
    N, K = map(int, input().split())
    d = [int(input()) for _ in range(K)]
    a = [[int(i) for i in input().split()] for _ in range(K)]
    print(snukes(N, K, d, a))

