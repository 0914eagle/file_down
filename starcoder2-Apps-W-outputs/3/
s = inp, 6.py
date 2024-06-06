
s = input()

for i in range(len(s)):
    for j in range(i+1, len(s)):
        a = int(s[:i])
        b = int(s[i:j])
        c = int(s[j:])
        if a + b == c:
            print(str(a) + '+' + str(b) + '=' + str(c))
            break
