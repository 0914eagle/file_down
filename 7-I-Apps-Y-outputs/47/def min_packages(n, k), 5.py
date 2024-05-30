
def min_packages(n, k):
    if n == 1:
        return 1
    if n < 1 or k < 1:
        return 0
    if n == k:
        return 1
    if n < k:
        return 0
    if n % k == 0:
        return n // k
    else:
        return (n // k) + 1

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(min_packages(n, k))

if __name__ == '__main__':
    main()

