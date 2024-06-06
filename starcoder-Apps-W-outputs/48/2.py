
def main():
    v = int(input())
    a = [int(i) for i in input().split()]
    for i in range(9,-1,-1):
        if v < a[i]:
            continue
        n = v // a[i]
        v -= n * a[i]
        if n > 0:
            print(i * n, end='')
    else:
        if v != 0:
            print(-1)

main()
