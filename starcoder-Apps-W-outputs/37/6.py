
def digit_cnt(n):
    return len(str(n))

if __name__ == '__main__':
    p, x = map(int, input().split())

    for i in range(10**(p-1), 10**p):
        if (i*x) % 10**p == i:
            print(i)
            break
    else:
        print('Impossible')
