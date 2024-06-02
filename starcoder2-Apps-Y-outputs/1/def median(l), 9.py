

def median(l):
    l.sort()
    if len(l) % 2 == 1:
        return l[len(l)//2]
    else:
        return (l[len(l)//2-1]+l[len(l)//2])/2

n = int(input())
x = list(map(int, input().split()))

for i in range(n):
    l = x[:i] + x[i+1:]
    print(median(l))


