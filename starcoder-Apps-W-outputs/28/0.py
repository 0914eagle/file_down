
t = int(input())
while t:
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    t -= 1
    if x > y:
        x,y = y,x
    cnt = 0
    cnt += b*(x//2 + y//2)
    x %= 2
    y %= 2
    cnt += a * (x + y)
    print(cnt)
