
def main():
    n, m, k = map(int, input().split())
    print(n * m * (k - 1))
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print('(', i, ', ', j, ')', sep='', end=' ')
        print()

main()
