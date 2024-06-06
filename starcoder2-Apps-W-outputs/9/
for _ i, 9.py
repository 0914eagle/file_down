
for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(1, n+1):
        if n % i == 0:
            l.append(n//i)
    print(len(l))
    print(*l)
