

n = int(input())
s = input()

def f(s):
    if s[0] == s[-1]:
        return s[0]*(len(s)//2)
    else:
        return s[:len(s)//2]
    
def g(s):
    if len(s)%4 != 0:
        return (len(s)//4)+1
    else:
        return len(s)//4
    
def a(s):
    if len(s)%4 != 0:
        return len(s)
    else:
        return len(s) + len(s)//4 - 1
    
def get_min_len(s):
    if len(s)%4 == 0:
        return a(s)
    else:
        cnt = 0
        for i in range(4):
            if i < len(s)%4:
                cnt += g(s)
            else:
                cnt += a(s)
        return cnt
    
def func(s):
    l = []
    for i in range(len(s)):
        if s[i] not in l:
            l.append(s[i])
    res = ""
    for i in range(len(l)):
        if s.count(l[i]) >= len(s)//4:
            res += f(s)
            s = s.replace(f(s),"")
    return res + s

print(get_min_len(func(s)))
