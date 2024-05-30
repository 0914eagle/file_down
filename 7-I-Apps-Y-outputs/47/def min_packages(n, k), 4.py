
def min_packages(n, k):
    if n == 1:
        return 1
    if n == k:
        return 1
    if n < k:
        return 1
    if n > k:
        return n // k + 1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(min_packages(n, k))

