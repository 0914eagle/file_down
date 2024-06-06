
r, m = map(int, input().split())
a = [r]
for i in range(1, 10000):
    a.append(a[i-1]+i)
    if a[i] == m:
        print(i+1)
        break
    if a[i] > m:
        if m in a:
            print(a.index(m)+1)
            break
        else:
            print(a.index(a[i-1])+1)
            break
