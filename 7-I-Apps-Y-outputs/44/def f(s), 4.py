
def f(s):
    n = len(s)
    a = 0
    b = 0
    for i in range(n):
        if s[i] == 'a':
            a += 1
        else:
            b += 1
    if a == b:
        return 0, s
    else:
        if a > b:
            c = a - b
            for i in range(c):
                s = s[:i+1] + 'b' + s[i+1:]
            return c, s
        else:
            c = b - a
            for i in range(c):
                s = s[:i+1] + 'a' + s[i+1:]
            return c, s



n = int(input())
s = input()

c, s = f(s)
print(c)
print(s)

