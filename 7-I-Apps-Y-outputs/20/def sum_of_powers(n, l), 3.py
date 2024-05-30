
def sum_of_powers(n, l):
    result = 0
    for i in range(n):
        result += l[i] ** (i + 1)
    return result


def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    print(sum_of_powers(n, l))


if __name__ == '__main__':
    main()

