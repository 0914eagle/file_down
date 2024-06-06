
h, m, s, t_1, t_2 = map(int, input().split())

h, m, s, t_1, t_2 = h*5, m*5/60, s*5/3600, t_1*5, t_2*5

if t_1 - t_2 == 60 or t_2 - t_1 == 60:
    print('YES')
elif abs(t_1 - h) <= 5 and abs(t_2 - m) <= 5:
    print('YES')
elif abs(t_1 - m) <= 5 and abs(t_2 - s) <= 5:
    print('YES')
elif abs(t_1 - s) <= 5 and abs(t_2 - h) <= 5:
    print('YES')
else:
    print('NO')
