
x,y,x0,y0 = map(int,input().split())
s = input()

def check(x,y,x0,y0):
    if x0 == x and y0 == y:
        return 1
    else:
        return 0

def move(x,y,x0,y0,s):
    if s == 'L':
        if x0 == 1:
            return 0
        else:
            return x0-1
    elif s == 'R':
        if x0 == x:
            return 0
        else:
            return x0+1
    elif s == 'U':
        if y0 == 1:
            return 0
        else:
            return y0-1
    elif s == 'D':
        if y0 == y:
            return 0
        else:
            return y0+1

ans = [0]*(len(s)+1)
for i in range(len(s)):
    x0 = move(x,y,x0,y0,s[i])
    y0 = move(x,y,x0,y0,s[i])
    ans[i+1] = check(x,y,x0,y0)

for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i])
    else:
        print(ans[i],end = ' ')
