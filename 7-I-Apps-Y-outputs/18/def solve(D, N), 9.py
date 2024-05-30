
def solve(D, N):
    if D == 0:
        return 1
    elif D == 1:
        return 2 * N
    else:
        return 2 * N - 1


if __name__ == '__main__':
    D, N = map(int, input().split())
    print(solve(D, N))

