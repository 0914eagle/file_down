
# 1030A. Alyona and Numbers
n, k = map(int, input().split())

if k == 1:
    print('a' * n)
elif k == 2:
    print('-1')
else:
    # print('a' * (n // k), end='')
    # print('bc' * (n % k), end='')
    print('a' * (n - k + 1) + 'bc' * (k - 1))
