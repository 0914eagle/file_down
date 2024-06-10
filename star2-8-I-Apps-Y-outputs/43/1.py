
def elevator(f,s,g,u,d):
    if g<s:
        u,d=d,u
    if u<d:
        print("use the stairs")
        return
    q=[s]
    dist={s:0}
    while q:
        v=q.pop(0)
        if v==g:
            print(dist[v])
            return
        for w in (v+u,v-d):
            if 1<=w<=f and w not in dist:
                dist[w]=dist[v]+1
                q.append(w)
    print("use the stairs")

