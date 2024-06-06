
s = input()
n = len(s)
l = ['a', 'o', 'u', 'i', 'e', 'n']
if n == 1:
    if s in l:
        print("YES")
    else:
        print("NO")
else:
    if n == 2:
        if s in l:
            print("NO")
        else:
            print("YES")
    else:
        for i in range(n):
            if i == 0:
                if s[i] not in l:
                    print("NO")
                    break
            elif i != n-1:
                if s[i] not in l and s[i-1] != 'n':
                    print("NO")
                    break
            else:
                if s[i] not in l:
                    print("NO")
                    break
        else:
            print("YES")
