
s = input()

if s[0] in ['a','e','i','o','u']:
    print('NO')
else:
    for i in range(len(s)-1):
        if s[i] in ['a','e','i','o','u']:
            continue
        elif s[i+1] in ['a','e','i','o','u']:
            continue
        else:
            print('NO')
            break
    else:
        print('YES')
