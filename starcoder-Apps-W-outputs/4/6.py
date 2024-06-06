
t = int(input())
for _ in range(t):
    s = input().strip()
    if s[-2:]=='po':
        print('FILIPINO')
    elif s[-4:]=='masu' or s[-4:]=='desu':
        print('JAPANESE')
    else:
        print('KOREAN')
