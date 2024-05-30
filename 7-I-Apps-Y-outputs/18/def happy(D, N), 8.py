
def happy(D, N):
    # write your code here
    if D == 0:
        return 100 * N
    elif D == 1:
        return 100 * (N - 1) + 1
    elif D == 2:
        return 100 * (N - 2) + 2


if __name__ == "__main__":
    D, N = map(int, input().split())
    print(happy(D, N))

