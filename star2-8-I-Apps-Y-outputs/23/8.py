
s = input()
q = int(input())
for _ in range(q):
    t, *lr = map(int, input().split())
    if t == 1:
        s = s[:lr[0] - 1] + chr(lr[1]) + s[lr[0]:]
    else:
        l, r = lr
        print(len(set(s[l - 1:r])))

