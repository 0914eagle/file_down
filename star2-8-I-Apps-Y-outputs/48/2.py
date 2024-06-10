
n = int(input())
digit = n % 10
if digit in [2, 4, 5, 7, 9]:
    print('hon')
elif digit in [0, 1, 6, 8]:
    print('pon')
else:
    print('bon')

