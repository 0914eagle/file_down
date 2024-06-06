
import math

t = int(input())

for i in range(t):
    s = input().split('_')
    c = s[-1]
    if c == 'po':
        print('FILIPINO')
    elif c == 'desu' or c == 'masu':
        print('JAPANESE')
    else:
        print('KOREAN')
        
