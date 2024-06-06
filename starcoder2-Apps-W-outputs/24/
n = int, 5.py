
n = int(input())

for i in range(n):
    if i % 2 == 0:
        print('WB' * (n // 2))
    else:
        print('BW' * (n // 2))
