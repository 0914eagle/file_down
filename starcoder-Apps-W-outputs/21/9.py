
#!/usr/bin/env python
# coding=utf-8

def main():
    n, m = map(int, raw_input().split())
    a = map(int, raw_input().split())
    a.sort()

    res = 0
    for i in xrange(n):
        if a[i] % 2 == 1:
            res += (a[i] + 1) / 2
            res += m - a[i] / 2
        else:
            res += (a[i] + 2) / 2
            res += m - a[i] / 2
    print res

if __name__ == "__main__":
    main()
