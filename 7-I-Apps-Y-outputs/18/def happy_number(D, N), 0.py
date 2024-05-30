
def happy_number(D, N):
    # Write your code here
    if D == 0:
        return 1
    elif D == 1:
        return 100
    elif D == 2:
        return 10000
    else:
        return 0


if __name__ == '__main__':
    D, N = map(int, input().split())
    print(happy_number(D, N))

