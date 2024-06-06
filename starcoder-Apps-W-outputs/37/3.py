
p, x = map(int, input().split())
num = []
a = 1
for i in range(p):
    a *= x
    num.append(a%10)
    a //= 10
num = num[::-1]

if num[0] == 0:
    print('Impossible')
else:
    print(''.join(map(str, num)))
