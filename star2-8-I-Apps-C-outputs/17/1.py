
n, k = map(int, input().split())
s = ['0'] * n
l = 0
while k > 1:
    s[l] = '1'
    l += 2
    k -= 1
print(''.join(s))

