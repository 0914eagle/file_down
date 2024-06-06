
# coding=utf-8
# author=yphacker


def main():
    # n, t, c = [int(i) for i in input().split()]
    # a = [int(i) for i in input().split()]
    n, t, c = 11, 4, 2
    a = [2, 2, 0, 7, 3, 2, 2, 4, 9, 1, 4]
    res = 0
    b = a[:c]
    for i in range(n - c + 1):
        if max(b) <= t:
            res += 1
        if i + c < n:
            b.remove(a[i])
            b.append(a[i + c])
    print(res)


main()
