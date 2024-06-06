
#encoding=utf8
from sys import stdin
from sys import stdout
from sys import stderr

if __name__ == '__main__':
    X, A, B = stdin.readline().strip().split(' ')
    X = int(X)
    A = int(A)
    B = int(B)
    allowed = stdin.readline().strip()

    tot = 0
    for i in range(A, B + 1):
        if i % X != 0:
            continue
        tmp = i
        found = True
        while tmp != 0:
            if str(tmp % 10) not in allowed:
                found = False
                break
            tmp //= 10
        if found:
            tot += 1
    stdout.write(str(tot) + '\n')

