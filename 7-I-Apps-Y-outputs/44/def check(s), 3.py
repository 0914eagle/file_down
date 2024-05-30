

n = int(input())
s = input()

def check(s):
    if len(s) % 2 == 1:
        return False
    else:
        return s[0:len(s)//2].count('a') == s[0:len(s)//2].count('b') and s[len(s)//2:].count('a') == s[len(s)//2:].count('b')


if check(s):
    print(0)
    print(s)
else:
    count = 0
    for i in range(1, len(s), 2):
        if s[i] == s[i-1]:
            count += 1
    print(count)
    for i in range(1, len(s), 2):
        if s[i] == s[i-1]:
            s = s[:i] + 'b' + s[i+1:]
            break
    print(s)

