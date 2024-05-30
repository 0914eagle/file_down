
def happy(D, N):
    i = 1
    while N > 0:
        if i % 100 == 0:
            N -= 1
        i += 1
    return i - 1

if __name__ == "__main__":
    D, N = map(int, input().split())
    print(happy(D, N))

