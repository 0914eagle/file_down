
n, k = map(int, input().split())

s = ''
while len(s) < n:
    if len(s) == 0:
        s += '1'
    else:
        if s[-1] == '1':
            s += '0'
        else:
            s += '1'
print(s)

