

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    for i in range(n):
        for j in range(i+2, n):
            if a[i] == a[j]:
                print("YES")
                exit(0)
    
    print("NO")


