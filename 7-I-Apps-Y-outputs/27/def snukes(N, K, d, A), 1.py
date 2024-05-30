

def snukes(N, K, d, A):
    # Write your code here
    return 0


if __name__ == "__main__":
    N, K = list(map(int, input().split()))
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    print(snukes(N, K, d, A))

