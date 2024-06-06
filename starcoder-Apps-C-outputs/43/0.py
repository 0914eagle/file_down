
a = input()

if '0' in a:
    a = a.replace('0', '')

if len(a) < 4:
    print(0)

else:
    for i in ['6', '8', '9']:
        if i not in a:
            print(0)
        else:
            if len(a) % 3 == 0:
                if i == '6':
                    print(str(a).replace('6', '16', 1))
                if i == '8':
                    print(str(a).replace('8', '18', 1))
                if i == '9':
                    print(str(a).replace('9', '19', 1))
            if len(a) % 3 == 1:
                if i == '6':
                    print(str(a).replace('6', '16', 1))
                if i == '8':
                    print(str(a).replace('8', '18', 1))
                if i == '9':
                    print(str(a).replace('9', '19', 1))
            if len(a) % 3 == 2:
                if i == '6':
                    print(str(a).replace('6', '16', 1))
                if i == '8':
                    print(str(a).replace('8', '18', 1))
                if i == '9':
                    print(str(a).replace('9', '19', 1))

