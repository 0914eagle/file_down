
s = input()
q = int(input())

l = list(s)
for _ in range(q):
    q = list(input().split())
    if q[0] == '1':
        pos = int(q[1]) - 1
        c = q[2]
        l[pos] = c
    else:
        l1 = l[int(q[1]) - 1 : int(q[2])]
        s1 = ''.join(l1)
        s2 = ''
        for c in s1:
            if c not in s2:
                s2 += c
        print(len(s2))

