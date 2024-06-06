
p, x = map(int, input().split())
s = str(p)
if x == 9:
    print(s + '0')
else:
    l = len(s)
    num = ''
    for i in range(10):
        if x == 1:
            if int(s * i) > 10 ** l - 1:
                num = s * i
                break
        else:
            if int(s * i) > (10 ** l - 1) // (x - 1):
                num = s * i
                break
    print(num)
