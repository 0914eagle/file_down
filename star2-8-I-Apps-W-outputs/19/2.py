
from itertools import permutations

s = input()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if s.count('?') == 0:
    if len(s) == 26 and len(set(s)) == 26:
        print(s)
    else:
        print(-1)

else:
    if len(set(s)) == 26:
        print(s)
    else:
        p = permutations(alpha)
        for i in p:
            c = 0
            temp = s
            for j in i:
                if temp.find('?') != -1:
                    temp = temp.replace('?', j, 1)
                    c += 1
                if c == s.count('?'):
                    break
            if len(set(temp)) == 26:
                print(temp)
                break
        else:
            print(-1)

