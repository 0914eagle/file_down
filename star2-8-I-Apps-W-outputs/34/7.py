
for i in range(int(input())):
    s = input()
    n = len(s)
    
    c1, c2 = 0, 0
    
    for j in range(n):
        if s[j] == '0':
            c1 += 1
        else:
            c2 += 1
    
    print(min(c1, c2))

