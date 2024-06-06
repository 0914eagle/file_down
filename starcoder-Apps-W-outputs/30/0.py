
s = input()
s = s.strip()
check = 0
vowel = ['a', 'e', 'i', 'o', 'u']
consonent = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

if len(s) <= 0:
    check = 0
else:
    for i in s:
        if i not in vowel and i not in consonent:
            check = 0
            break
        if i in consonent:
            if s[s.index(i)+1] not in vowel:
                if i == 'n':
                    if s.index(i)+1 < len(s)-1:
                        if s[s.index(i)+2] not in vowel:
                            check = 0
                            break
                else:
                    check = 0
                    break

if check == 0:
    print("NO")
else:
    print("YES")

