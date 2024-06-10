
for _ in range(int(input())):
    n = int(input())
    s = input()
    x, y = 0, 0
    for c in s:
        if c == "L":
            x -= 1
        elif c == "R":
            x += 1
        elif c == "U":
            y += 1
        elif c == "D":
            y -= 1
    
    if x == y == 0:
        print(-1)
    else:
        l = r = 1
        if s[0] == "L":
            x += 1
        elif s[0] == "R":
            x -= 1
        elif s[0] == "U":
            y -= 1
        elif s[0] == "D":
            y += 1
        
        while l <= n:
            if x == y == 0:
                print(l, r)
                break
            
            if r < n and (s[r] == "L" and x > 0 or s[r] == "R" and x < 0 or s[r] == "U" and y > 0 or s[r] == "D" and y < 0):
                r += 1
                if s[r-1] == "L":
                    x -= 1
                elif s[r-1] == "R":
                    x += 1
                elif s[r-1] == "U":
                    y += 1
                elif s[r-1] == "D":
                    y -= 1
            else:
                if s[l-1] == "L":
                    x += 1
                elif s[l-1] == "R":
                    x -= 1
                elif s[l-1] == "U":
                    y -= 1
                elif s[l-1] == "D":
                    y += 1
                l += 1

