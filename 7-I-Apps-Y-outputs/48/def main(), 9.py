
import sys

def main():
    n = int(sys.stdin.readline())
    c = []
    s = []
    f = []
    for i in range(n):
        c.append(int(sys.stdin.readline()))
        s.append(int(sys.stdin.readline()))
        f.append(int(sys.stdin.readline()))
    for i in range(n):
        if i == 0:
            print(s[i] + c[i])
        else:
            print((s[i] - s[i - 1]) % f[i - 1] + s[i] + c[i])

main()

