
t = int(input())
for _ in range(t):
    s = input()
    count0 = 0
    count1 = 0
    for ch in s:
        if ch == '0':
            count0 += 1
        else:
            count1 += 1
    print(min(count0, count1))

