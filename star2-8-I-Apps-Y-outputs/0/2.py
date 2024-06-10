
for _ in range(int(input())):
    n = int(input())
    s = input()
    x, y = 0, 0
    for c in s:
        if c == 'L':
            x -= 1
        elif c == 'R':
            x += 1
        elif c == 'U':
            y += 1
        else:
            y -= 1
    if x == 0 and y == 0:
        print(-1)
        continue
    start = 0
    while s[start] != 'L' and s[start] != 'R':
        start += 1
    end = len(s) - 1
    while s[end] != 'L' and s[end] != 'R':
        end -= 1
    left, right = start, end
    while left < right:
        if s[left] == 'L':
            x -= 1
        elif s[left] == 'R':
            x += 1
        elif s[left] == 'U':
            y += 1
        else:
            y -= 1
        if x == 0 and y == 0:
            break
        left += 1
    while right > left:
        if s[right] == 'L':
            x -= 1
        elif s[right] == 'R':
            x += 1
        elif s[right] == 'U':
            y += 1
        else:
            y -= 1
        if x == 0 and y == 0:
            break
        right -= 1
    print(left+1, right+1)

