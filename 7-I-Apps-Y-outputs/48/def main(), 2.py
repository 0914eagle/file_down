
import sys

def main():
    n = int(input())
    c, s, f = [], [], []
    for i in range(n-1):
        c.append(int(input()))
        s.append(int(input()))
        f.append(int(input()))
    c.append(0)
    s.append(0)
    f.append(0)
    time = [0]*n
    time[0] = s[0]
    for i in range(1, n):
        time[i] = time[i-1] + s[i-1] + c[i-1]
    for i in range(1, n):
        time[i] = time[i] + (time[i-1] - s[i-1]) % f[i-1]
    for i in time:
        print(i)

if __name__ == '__main__':
    main()

