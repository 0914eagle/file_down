
f, s, g, u, d = map(int, input().split())

if u == 0 and d == 0:
    print("use the stairs")
elif u == 0:
    if g > s:
        print("use the stairs")
    else:
        print(s - g)
elif d == 0:
    if g < s:
        print("use the stairs")
    else:
        print(g - s)
else:
    curr = s
    count = 0
    while curr != g:
        curr += u
        count += 1
        if curr > f:
            print("use the stairs")
            break
        elif curr == g:
            print(count)
            break
        curr -= d
        count += 1
        if curr < 1:
            print("use the stairs")
            break
        elif curr == g:
            print(count)
            break


