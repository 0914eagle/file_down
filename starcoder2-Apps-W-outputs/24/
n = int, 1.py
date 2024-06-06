
n = int(input())

if n == 3:
    print('WBW')
    print('BBB')
    print('WBW')
else:
    for i in range(n):
        print('W' * (n // 2) + 'B' * (n // 2))
