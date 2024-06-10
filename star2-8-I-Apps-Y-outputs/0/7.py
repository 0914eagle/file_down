
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    l, r = -1, -1

    for i in range(n):
        if s[i] == 'L':
            l = i
            break

    for i in range(n-1, -1, -1):
        if s[i] == 'R':
            r = i
            break
    
    if l != -1 and r != -1:
        print(l+1, r+1)
    else:
        print(-1)

