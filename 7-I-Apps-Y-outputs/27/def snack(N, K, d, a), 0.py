
def snack(N, K, d, a):
    count = 0
    for i in range(N):
        if len(set(a[i])) < d[i]:
            count += 1
    return count

if __name__ == '__main__':
    N, K = map(int, input().split())
    d = [int(input()) for _ in range(K)]
    a = [list(map(int, input().split())) for _ in range(K)]
    print(snack(N, K, d, a))

