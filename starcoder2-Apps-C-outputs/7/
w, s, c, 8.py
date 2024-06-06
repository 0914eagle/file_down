
w, s, c, k = map(int, input().split())

if w == 0 and s == 0 and c == 0:
    print('YES')
elif w == 0 and s == 0 and c != 0:
    print('NO')
elif w == 0 and s != 0 and c == 0:
    print('NO')
elif w != 0 and s == 0 and c == 0:
    print('NO')
elif w == 0 and s != 0 and c != 0:
    if c > k:
        print('NO')
    else:
        print('YES')
elif w != 0 and s == 0 and c != 0:
    if c > k:
        print('NO')
    else:
        print('YES')
elif w != 0 and s != 0 and c == 0:
    if s > k:
        print('NO')
    else:
        print('YES')
elif w != 0 and s != 0 and c != 0:
    if s > k or c > k:
        print('NO')
    else:
        print('YES')
