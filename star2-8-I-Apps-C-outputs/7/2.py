
def f(s):
    t = {chr(i):"" for i in range(ord('a'),ord('z')+1)}
    for i,c in enumerate("abcde"):
        t[c] = input().strip()
    for i,c in enumerate("fghij"):
        t[c] = input().strip()
    for i,c in enumerate("klmno"):
        t[c] = input().strip()
    for i,c in enumerate("pqrst"):
        t[c] = input().strip()
    for i,c in enumerate("uvwxy"):
        t[c] = input().strip()
    t['z'] = input().strip()
    
    def f2(s):
        ret = ""
        for c in s:
            ret += t[c]
        return ret
    
    k = int(input())
    p = s
    for i in range(k):
        p = f2(p)
    return p

m = int(input())
mi = list(map(int,input().split()))

p = f(input())
for i in mi:
    print(p[i-1])

