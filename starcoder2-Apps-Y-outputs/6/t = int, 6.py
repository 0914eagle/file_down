
t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    k -= 1
    a = n - 2
    b = 2
    s = ''
    while a > 0:
        if k >= a:
            s += 'b'
            k -= a
            b -= 1
        else:
            s += 'a'
            a -= 1
    while b > 0:
        s += 'b'
        b -= 1
    print(s)

