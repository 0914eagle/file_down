
while True:
    try:
        a,b = map(int,input().split())
        w = {}
        for i in range(a):
            id,s,h = map(int,input().split())
            w[id] = [s,h]
        while b:
            x = int(input())
            b -= 1
            r = []
            for k,v in w.items():
                if v[0] > w[x][0] and v[1] >= w[x][1]:
                    r.append(k)
            if len(r) == 0:
                print(0,0)
                continue
            r.sort()
            print(r[0],len(r))
    except:
        break
